"""Gera marketing/catalogo.json: a lista única do que o parecer de marketing pode citar.

Fontes: frontmatter de posts/*/post.md, marketing/legado.yaml, marketing/ofertas.yaml e
marketing/clusters.yaml. O modelo nunca escreve no catálogo; rode de novo sempre que
uma fonte mudar:  python3 scripts/gerar_catalogo.py
"""
import json
import re
import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
MKT = RAIZ / "marketing"


def ler_post(caminho):
    """Devolve (frontmatter: dict, corpo: str, deslocamento do corpo no arquivo)."""
    texto = Path(caminho).read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?\n)---\n", texto, re.S)
    if not m:
        return {}, texto, 0
    return yaml.safe_load(m.group(1)) or {}, texto[m.end():], m.end()


def _yaml(nome):
    return yaml.safe_load((MKT / nome).read_text(encoding="utf-8")) or []


def gerar():
    itens, erros = [], []

    for f in sorted((RAIZ / "posts").glob("*/post.md")):
        fm, _, _ = ler_post(f)
        url = fm.get("url_publicada") or None
        itens.append({
            "id": f"post:{f.parent.name}",
            "tipo": "post",
            "titulo": fm.get("titulo") or fm.get("título"),
            "data": str(fm.get("data", "")),
            "linha_editorial": fm.get("linha_editorial"),
            "resumo": fm.get("resumo"),
            "url": url,
            "situacao": "disponível" if url else "não publicado",
        })

    for p in _yaml("legado.yaml"):
        itens.append({"id": p["id"], "tipo": "post", "titulo": p["titulo"], "data": str(p["data"]),
                      "linha_editorial": None, "resumo": p.get("resumo") or None,
                      "url": p["url_publicada"], "situacao": "disponível"})

    for o in _yaml("ofertas.yaml"):
        itens.append({"id": o["id"], "tipo": o["tipo"], "titulo": o["nome"], "url": o.get("url"),
                      "situacao": o["situacao"], "estagio": o.get("estagio"),
                      "segmento": o.get("segmento") or []})

    por_id = {}
    for i in itens:
        if i["id"] in por_id:
            erros.append(f"id duplicado: {i['id']}")
        por_id[i["id"]] = i

    clusters = _yaml("clusters.yaml")
    for c in clusters:
        if c.get("pilar") and c["pilar"] not in c["membros"]:
            erros.append(f"cluster {c['id']}: pilar fora dos membros")
        for m in c["membros"]:
            if m not in por_id:
                erros.append(f"cluster {c['id']}: membro inexistente {m}")
            elif "cluster" in por_id[m]:
                erros.append(f"{m} está em dois clusters")
            else:
                por_id[m]["cluster"] = c["id"]
                por_id[m]["pilar"] = m == c.get("pilar")

    for i in itens:
        i["citavel"] = i["situacao"] == "disponível" and bool(i["url"] or i["tipo"] == "nativo")

    return {"itens": itens, "clusters": clusters}, erros


if __name__ == "__main__":
    catalogo, erros = gerar()
    if erros:
        sys.exit("catálogo não gerado:\n- " + "\n- ".join(erros))
    (MKT / "catalogo.json").write_text(
        json.dumps(catalogo, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    n = sum(i["citavel"] for i in catalogo["itens"])
    print(f"marketing/catalogo.json: {len(catalogo['itens'])} itens, {n} citáveis")
