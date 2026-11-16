#!/usr/bin/env python3
"""Corpus publicado: captura os posts do site da Syntaxis e gera o Markdown normalizado.

  python3 scripts/corpus_publicado.py              # capturar + normalizar
  python3 scripts/corpus_publicado.py capturar     # baixa só o que é novo ou mudou
  python3 scripts/corpus_publicado.py normalizar   # regera estilo/corpus/ a partir de _arquivo/publicados/

Captura: JSON bruto de GET /api/v1/posts/<slug>, sem o campo `comments` (traz nome, handle e
foto de leitores; o repositório é público). Grava em _arquivo/publicados/AAAA-MM-DD_<slug>.json
e nunca sobrescreve: se o `updated_at` mudou no site, grava AAAA-MM-DD_<slug>__cap-<hoje>.json.
Sem autenticação, User-Agent genérico, uma requisição por segundo, nenhuma imagem baixada.

Normalização: a captura mais recente de cada post vira estilo/corpus/publicados/<slug>.md, e o
mapa site <-> repo <-> rascunho vai para estilo/corpus/mapa-publicados.json (fonte única).
Só stdlib.
"""

import datetime as dt
import difflib
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
SITE = "https://syntaxis.substack.com"
ARQ = RAIZ / "_arquivo" / "publicados"
SAIDA = RAIZ / "estilo" / "corpus" / "publicados"
MAPA = RAIZ / "estilo" / "corpus" / "mapa-publicados.json"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
# Rascunhos que são transcrição de áudio ditado, não texto do autor (ver _arquivo/MANIFESTO.md).
TRANSCRICOES = {
    "2026-08-10-o-mundo-invertido-dos-investimentos",
    "2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos",
    "2026-08-17-o-mundo-invertido-das-carreiras-em-financas",
}


# ---------------------------------------------------------------- captura

def _get(url, tentativas=3):
    for i in range(tentativas):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                dados = json.load(r)
            time.sleep(1)
            return dados
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
            if i == tentativas - 1:
                raise
            time.sleep(10 * (i + 1))


def listar_slugs():
    slugs, cursor = [], None
    while True:
        url = f"{SITE}/api/v1/archive?sort=new" + (f"&cursor={cursor}" if cursor else "")
        d = _get(url)
        posts = d["posts"] if isinstance(d, dict) else d
        slugs += [p["slug"] for p in posts]
        cursor = d.get("nextCursor") if isinstance(d, dict) else None
        if not cursor or not posts:
            return slugs


def capturas(slug):
    """Capturas de um post, da mais antiga para a mais recente."""
    base = sorted(ARQ.glob(f"????-??-??_{slug}.json"))
    return base + sorted(ARQ.glob(f"????-??-??_{slug}__cap-*.json"))


def capturar():
    ARQ.mkdir(parents=True, exist_ok=True)
    novos, mudados, iguais = [], [], 0
    for slug in listar_slugs():
        d = _get(f"{SITE}/api/v1/posts/{slug}")
        d.pop("comments", None)
        anteriores = capturas(slug)
        if anteriores:
            if json.loads(anteriores[-1].read_text())["updated_at"] == d["updated_at"]:
                iguais += 1
                continue
            prefixo = anteriores[0].name[:10]
            destino = ARQ / f"{prefixo}_{slug}__cap-{dt.date.today().isoformat()}.json"
            mudados.append(destino.name)
        else:
            destino = ARQ / f"{d['post_date'][:10]}_{slug}.json"
            novos.append(destino.name)
        if destino.exists():  # nunca sobrescreve, nem duas capturas no mesmo dia
            raise SystemExit(f"já existe: {destino}")
        destino.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
    print(f"capturar: {len(novos)} novos, {len(mudados)} mudados, {iguais} sem mudança")
    for n in novos + mudados:
        print("  +", n)
    return novos + mudados


# ---------------------------------------------------------------- HTML -> Markdown

VAZIAS = {"img", "br", "hr", "source", "input", "meta", "link", "wbr"}


class _Arvore(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.raiz = {"tag": "raiz", "attrs": {}, "filhos": []}
        self.pilha = [self.raiz]

    def handle_starttag(self, tag, attrs):
        no = {"tag": tag, "attrs": dict(attrs), "filhos": []}
        self.pilha[-1]["filhos"].append(no)
        if tag not in VAZIAS:
            self.pilha.append(no)

    def handle_startendtag(self, tag, attrs):
        self.pilha[-1]["filhos"].append({"tag": tag, "attrs": dict(attrs), "filhos": []})

    def handle_endtag(self, tag):
        for i in range(len(self.pilha) - 1, 0, -1):
            if self.pilha[i]["tag"] == tag:
                del self.pilha[i:]
                return

    def handle_data(self, data):
        self.pilha[-1]["filhos"].append(data)


def _classes(no):
    return no["attrs"].get("class", "").split()


def _dados(no):
    try:
        return json.loads(no["attrs"].get("data-attrs") or "{}")
    except json.JSONDecodeError:
        return {}


def _texto(no):
    if isinstance(no, str):
        return no
    return "".join(_texto(f) for f in no["filhos"])


def _achar(no, pred):
    if isinstance(no, str):
        return None
    if pred(no):
        return no
    for f in no["filhos"]:
        r = _achar(f, pred)
        if r is not None:
            return r
    return None


def _envolve(s, marca):
    if not marca or not s.strip():
        return s
    ini, fim = s[: len(s) - len(s.lstrip())], s[len(s.rstrip()):]
    return f"{ini}{marca}{s.strip()}{marca}{fim}"


def _inline(nos, em_titulo=False):
    out = []
    for n in nos:
        if isinstance(n, str):
            out.append(re.sub(r"\s+", " ", n))
            continue
        t = n["tag"]
        if t in ("strong", "b"):  # negrito em título é artefato de colagem, não ênfase
            out.append(_envolve(_inline(n["filhos"], em_titulo), "" if em_titulo else "**"))
        elif t in ("em", "i"):
            out.append(_envolve(_inline(n["filhos"], em_titulo), "*"))
        elif t in ("s", "del", "strike"):
            out.append(_envolve(_inline(n["filhos"], em_titulo), "~~"))
        elif t == "code":
            out.append(f"`{_texto(n)}`")
        elif t == "a":
            txt, href = _inline(n["filhos"], em_titulo), n["attrs"].get("href")
            out.append(f"[{txt.strip()}]({href})" if href and txt.strip() else txt)
        elif t == "br":
            out.append("\n")
        elif t in ("button", "svg", "picture", "source", "img", "script", "style"):
            continue
        else:
            out.append(_inline(n["filhos"], em_titulo))
    return "".join(out)


def _limpa(s):
    s = re.sub(r"[ \t]*\n[ \t]*", "\n", s)
    s = re.sub(r"[ \t]{2,}", " ", s)
    return s.strip()


def _cta(no):
    a = _achar(no, lambda x: x["tag"] == "a" and "button" in _classes(x))
    d = _dados(no)
    txt = _limpa(_texto(a)) if a else d.get("text", "")
    href = (a["attrs"].get("href") if a else None) or d.get("url", "")
    leg = _achar(no, lambda x: "cta-caption" in _classes(x))
    sufixo = f" | {_limpa(_inline(leg['filhos']))}" if leg else ""
    return f"[[CTA: {txt} → {href}{sufixo}]]"


def _blocos(nos, ctx, desconhecidos):
    out = []
    for n in nos:
        if isinstance(n, str):
            if n.strip():
                out.append(_limpa(n))
            continue
        t, c = n["tag"], _classes(n)
        if t == "p":
            s = _cta(n) if "button-wrapper" in c else _limpa(_inline(n["filhos"]))
            if s:
                out.append(s)
        elif re.fullmatch(r"h[1-6]", t):
            s = _limpa(_inline(n["filhos"], em_titulo=True)).replace("\n", " ")
            if s:
                out.append("#" * int(t[1]) + " " + s)
        elif t in ("ul", "ol"):
            itens = [f for f in n["filhos"] if isinstance(f, dict) and f["tag"] == "li"]
            linhas = []
            for i, li in enumerate(itens, 1):
                txt = " ".join(_blocos(li["filhos"], ctx, desconhecidos)).replace("\n", " ")
                linhas.append(("- " if t == "ul" else f"{i}. ") + txt)
            if linhas:
                out.append("\n".join(linhas))
        elif t == "blockquote":
            dentro = _blocos(n["filhos"], ctx, desconhecidos)
            if dentro:
                out.append("\n>\n".join("> " + b.replace("\n", "\n> ") for b in dentro))
        elif t == "hr":
            out.append("* * *")
        elif t == "pre":
            out.append(f"```\n{_texto(n).rstrip()}\n```")
        elif t == "figure" or "captioned-image-container" in c:
            ctx["img"] += 1
            leg = _achar(n, lambda x: x["tag"] == "figcaption")
            out.append(f"![{_limpa(_inline(leg['filhos'])) if leg else ''}](img-{ctx['img']:02d})")
        elif "latex-rendered" in c:
            out.append(f"$$ {_dados(n).get('persistentExpression', '').strip()} $$")
        elif "captioned-button-wrap" in c:
            out.append(_cta(n))
        elif "pullquote" in c:
            out.append("[[PULLQUOTE: " + " ".join(_blocos(n["filhos"], ctx, desconhecidos)) + "]]")
        elif "highlighted_code_block" in c:
            out.append(f"```{_dados(n).get('language', '')}\n{_texto(n).rstrip()}\n```")
        elif "youtube-wrap" in c or "youtube-inner" in c:
            vid = _dados(n).get("videoId")
            if vid is None:
                f = _achar(n, lambda x: x["tag"] == "iframe")
                vid = f["attrs"].get("src", "") if f else ""
            out.append(f"[[VIDEO: {vid}]]")
        elif "poll-embed" in c:
            out.append("[[ENQUETE]]")
        elif t == "iframe":
            out.append(f"[[EMBED: {n['attrs'].get('src', '')}]]")
        elif t == "div":
            if c and c[0] not in ("pencraft", "image2-inset", "image-link-expand", "preamble"):
                desconhecidos.add("div." + c[0])
            out.extend(_blocos(n["filhos"], ctx, desconhecidos))
        else:
            s = _limpa(_inline([n]))
            if s:
                out.append(s)
    return out


def html_para_md(html, desconhecidos=None):
    arv = _Arvore()
    arv.feed(html or "")
    desconhecidos = set() if desconhecidos is None else desconhecidos
    return "\n\n".join(_blocos(arv.raiz["filhos"], {"img": 0}, desconhecidos)) + "\n"


PALAVRA = re.compile(r"[0-9A-Za-zÀ-ÖØ-öø-ÿ]+(?:[-'’][0-9A-Za-zÀ-ÖØ-öø-ÿ]+)*")


def contar_palavras(md):
    """Texto visível do .md, como o `wordcount` do Substack conta: inclui legenda de imagem,
    de CTA e código; exclui URLs e LaTeX. Serve para conferir a fidelidade do parser."""
    corpo = re.sub(r"\$\$.*?\$\$", " ", md, flags=re.S)
    corpo = re.sub(r"\]\([^)]*\)", "]", corpo)
    corpo = re.sub(r"https?://\S+|img-\d+|\[\[(CTA|PULLQUOTE|VIDEO|ENQUETE|EMBED)", " ", corpo)
    return len(PALAVRA.findall(corpo))


# ---------------------------------------------------------------- mapa site <-> repo <-> rascunho

def _sem_acento(s):
    return "".join(ch for ch in unicodedata.normalize("NFD", s) if unicodedata.category(ch) != "Mn")


def _frontmatter(texto):
    m = re.match(r"---\n(.*?)\n---\n", texto, re.S)
    campos = {}
    for linha in (m.group(1).splitlines() if m else []):
        k, _, v = linha.partition(":")
        campos[k.strip()] = v.strip().strip('"').strip("'")
    return campos


def montar_mapa(publicados):
    """publicados: {slug_site: json_da_api}. Devolve a lista do mapa, um item por post do site."""
    repo = {}
    for p in sorted((RAIZ / "posts").glob("*/post.md")):
        url = _frontmatter(p.read_text()).get("url_publicada", "")
        repo[p.parent.name] = url.rstrip("/").rsplit("/p/", 1)[-1] if "/p/" in url else None
    site_para_repo = {v: k for k, v in repo.items() if v}
    fonte = {k: "url_publicada" for k in site_para_repo}
    for slug_repo, slug_site in repo.items():  # posts sem url_publicada: data + slug parecido
        if slug_site:
            continue
        data, sufixo = slug_repo[:10], slug_repo[11:]
        candidatos = [
            s for s, d in publicados.items()
            if s not in site_para_repo and 0 <= (dt.date.fromisoformat(d["post_date"][:10])
                                                 - dt.date.fromisoformat(data)).days <= 10
            and (s.startswith(sufixo) or sufixo.startswith(s)
                 or difflib.SequenceMatcher(None, s, sufixo).ratio() >= 0.6)
        ]
        if len(candidatos) == 1:
            site_para_repo[candidatos[0]] = slug_repo
            fonte[candidatos[0]] = "inferido (data + slug)"

    rascunhos = {}
    for f in (RAIZ / "_arquivo" / "drafts").glob("*.md"):
        digitos = re.sub(r"\D", "", f.name)[:8]
        rascunhos[f"{digitos[:4]}-{digitos[4:6]}-{digitos[6:8]}"] = f.relative_to(RAIZ).as_posix()

    amostras = {}
    for f in (RAIZ / "_arquivo" / "amostras" / "proprias" / "substack").glob("*.md"):
        chave = _sem_acento(f.stem.removeprefix("syntaxis_")).replace("_", "-").lower()
        melhor = max(publicados, key=lambda s: difflib.SequenceMatcher(None, chave, s).ratio())
        if difflib.SequenceMatcher(None, chave, melhor).ratio() >= 0.7:
            amostras[melhor] = f.relative_to(RAIZ).as_posix()

    itens = []
    for slug, d in sorted(publicados.items(), key=lambda kv: kv[1]["post_date"]):
        slug_repo = site_para_repo.get(slug)
        itens.append({
            "slug_site": slug,
            "url": d.get("canonical_url"),
            "post_date": d["post_date"][:10],
            "titulo": d.get("title"),
            "section_name": d.get("section_name"),
            "epoca": "pipeline" if slug_repo else "pre-pipeline",
            "slug_repo": slug_repo,
            "fonte_mapa": fonte.get(slug),
            "rascunho": rascunhos.get(slug_repo[:10]) if slug_repo else None,
            "rascunho_tipo": (("transcricao" if slug_repo in TRANSCRICOES else "rascunho")
                              if slug_repo else None),
            "amostra_v1": amostras.get(slug),
            "captura": capturas(slug)[-1].relative_to(RAIZ).as_posix(),
        })
    sem_par = sorted(set(repo) - {i["slug_repo"] for i in itens})
    if sem_par:
        print("AVISO: posts do repo sem par no site:", ", ".join(sem_par))
    return itens


# ---------------------------------------------------------------- normalizar

def normalizar():
    slugs = sorted({re.sub(r"^\d{4}-\d{2}-\d{2}_|__cap-.*$|\.json$", "", f.name)
                    for f in ARQ.glob("*.json")})
    publicados = {s: json.loads(capturas(s)[-1].read_text()) for s in slugs}
    mapa = montar_mapa(publicados)
    SAIDA.mkdir(parents=True, exist_ok=True)
    desconhecidos = set()
    for item in mapa:
        d = publicados[item["slug_site"]]
        corpo = html_para_md(d.get("body_html"), desconhecidos)
        meta = {
            "titulo": d.get("title"),
            "subtitulo": d.get("subtitle"),
            "slug_site": item["slug_site"],
            "url": item["url"],
            "post_date": item["post_date"],
            "section_name": item["section_name"],
            "wordcount_api": d.get("wordcount"),
            "palavras_md": contar_palavras(corpo),
            "slug_repo": item["slug_repo"],
            "rascunho": item["rascunho"],
            "epoca": item["epoca"],
            "captura": item["captura"],
        }
        fm = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())
        (SAIDA / f"{item['slug_site']}.md").write_text(f"---\n{fm}\n---\n\n{corpo}")
    MAPA.write_text(json.dumps(mapa, ensure_ascii=False, indent=1) + "\n")
    print(f"normalizar: {len(mapa)} posts -> {SAIDA.relative_to(RAIZ)}/, mapa em {MAPA.relative_to(RAIZ)}")
    if desconhecidos:
        print("AVISO: classes de div não tratadas:", ", ".join(sorted(desconhecidos)))


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "tudo"
    if modo in ("capturar", "tudo"):
        capturar()
    if modo in ("normalizar", "tudo"):
        normalizar()
    if modo not in ("capturar", "normalizar", "tudo"):
        raise SystemExit(__doc__)
