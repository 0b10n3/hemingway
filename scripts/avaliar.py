#!/usr/bin/env python3
"""Fase E do épico de revisão editorial: o pipeline novo deixa o autor com menos edição?

  python3 scripts/avaliar.py retro <slug-repo> <post-novo.md>
      Compara o post.md antigo (o que serviu de base à publicação) e o post.md que o pipeline
      novo gerou para o mesmo rascunho, os dois contra o texto publicado. Grava
      evals/editorial/<slug>/avaliacao.json. ATENÇÃO: os 16 posts atuais foram evidência na Fase D;
      a comparação retrospectiva mede mecânica, não generalização.

  python3 scripts/avaliar.py prospectivo
      Para os posts publicados depois do épico (data no slug > 2026-11-16), compara a edição que o
      autor fez no site com a linha de base dos 16 posts anteriores. É a medida limpa.

Métrica principal: similaridade por palavra post.md -> site e edições de estilo por mil palavras
(quanto menor a edição, melhor). Secundárias: distância nas métricas de forma, construções com
travessão, bloqueantes e avisos do checar_post. Só stdlib.
"""
import json
import re
import statistics
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "estilo" / "scripts"))
import checar_post as K  # noqa: E402
import diagnostico_edicoes as G  # noqa: E402
import diff_edicoes as D  # noqa: E402
import estratos as E  # noqa: E402

RAIZ = D.RAIZ
FIM_DO_EPICO = "2026-11-16"
FORMA = ["paragrafo_media", "pct_paragrafo_1_frase", "travessao_por_mil", "negrito_por_mil",
         "italico_por_mil", "perguntas_por_mil", "aspas_simples_por_mil"]
ESTILO = {"estilo"}


def edicao(post_md, site_md):
    """Quanto o autor teria de editar: similaridade e operações de estilo por mil palavras."""
    post = D.tokens(G.corpo_post(post_md))[0]
    site = D.tokens(D.ler_texto(site_md)[1])[0]
    ops = [o for o in D.operacoes([], post, site, set()) if o["natureza"] in ESTILO]
    palavras = sum(t["pal"] for t in post) or 1
    return {"similaridade": D.similaridade(post, site), "ops_estilo": len(ops),
            "ops_estilo_por_mil": round(1000 * len(ops) / palavras, 1)}


def forma(md, eh_post):
    corpo = G.corpo_post(md) if eh_post else D.ler_texto(md)[1]
    m = E.metricas(corpo)
    m["travessao_construcao_por_mil"] = round(
        1000 * len(re.findall(r"—\s+(?:não|a|o)\b", corpo, re.I)) / (m["palavras"] or 1), 2)
    return m


def distancia_forma(a, b):
    """Soma das diferenças relativas nas métricas de forma (0 = mesma forma)."""
    total = 0.0
    for k in FORMA:
        if a.get(k) is None or b.get(k) is None:
            continue
        total += abs(a[k] - b[k]) / (abs(b[k]) + 1)
    return round(total, 2)


def checagem(md):
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "post.md"
        p.write_text(md)
        bloq, aviso = K.checar(p)
    # a checagem roda numa pasta temporária, sem graficos.md/diagramas.md ao lado: o par
    # placeholder <-> spec não se mede aqui (o checar_post do próprio post mede)
    bloq = [b for b in bloq if "placeholder" not in b and "bloco de spec" not in b]
    return {"bloqueantes": len(bloq), "avisos": len(aviso)}


def comparar(antigo_md, novo_md, site_md):
    site_forma = forma(site_md, eh_post=False)
    linhas = {}
    for nome, md in (("antigo", antigo_md), ("novo", novo_md)):
        f = forma(md, eh_post=True)
        linhas[nome] = {**edicao(md, site_md), "distancia_forma_do_site": distancia_forma(f, site_forma),
                        "travessao_construcao_por_mil": f["travessao_construcao_por_mil"], **checagem(md)}
    return linhas


def retro(slug, novo):
    item = next(i for i in G.MAPA if i["slug_repo"] == slug)
    ed = json.loads((D.SAIDA / f"{slug}.json").read_text())
    antigo = G.mostrar(ed["post_md_base"]["commit"], f"posts/{slug}/post.md")
    site = (RAIZ / "estilo" / "corpus" / "publicados" / f"{item['slug_site']}.md").read_text()
    r = comparar(antigo, Path(novo).read_text(), site)
    destino = RAIZ / "evals" / "editorial" / slug
    destino.mkdir(parents=True, exist_ok=True)
    (destino / "avaliacao.json").write_text(json.dumps({"slug": slug, "contaminado_pela_fase_d": True, **r},
                                                       ensure_ascii=False, indent=1) + "\n")
    print(f"{slug} (contaminado: evidência da Fase D)")
    for k in r["antigo"]:
        print(f"  {k:32} antigo={r['antigo'][k]!s:>8}  novo={r['novo'][k]!s:>8}")


def prospectivo():
    resumo = []
    for f in sorted(D.SAIDA.glob("2026-*.json")):
        ed = json.loads(f.read_text())
        palavras = ed["palavras"]["post_md"] or 1
        ops = sum(1 for o in ed["operacoes"] if o["natureza"] in ESTILO)
        resumo.append((ed["slug_repo"], ed["similaridade"]["post_md_publicado"], round(1000 * ops / palavras, 1)))
    base = [r for r in resumo if r[0][:10] <= FIM_DO_EPICO]
    novos = [r for r in resumo if r[0][:10] > FIM_DO_EPICO]
    sims, taxas = [r[1] for r in base], [r[2] for r in base]
    print(f"linha de base ({len(base)} posts até {FIM_DO_EPICO}): similaridade mediana "
          f"{statistics.median(sims):.3f} (faixa {min(sims):.3f}–{max(sims):.3f}); edições de estilo por mil "
          f"palavras: mediana {statistics.median(taxas):.1f} (faixa {min(taxas):.1f}–{max(taxas):.1f})")
    if not novos:
        print("nenhum post publicado depois do épico ainda; rode /forja-de-voz colher depois de publicar")
    for slug, sim, taxa in novos:
        print(f"  {slug}: similaridade {sim:.3f}, edições de estilo {taxa:.1f} por mil palavras")


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "retro":
        retro(sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 2 and sys.argv[1] == "prospectivo":
        prospectivo()
    else:
        raise SystemExit(__doc__)
