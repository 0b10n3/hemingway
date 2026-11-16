"""Testes do conversor HTML -> Markdown do corpus publicado e checagem de volume.

  python3 -m unittest scripts/test_corpus_publicado.py

As fixtures são HTML escrito à mão, no formato que o Substack emite (não é texto de terceiros).
A checagem de volume compara cada estilo/corpus/publicados/*.md com o `wordcount` da API.
"""
import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_publicado as C  # noqa: E402

TOLERANCIA = 0.03


class Conversor(unittest.TestCase):
    def md(self, html):
        return C.html_para_md(html).strip()

    def test_paragrafos_e_enfase(self):
        self.assertEqual(
            self.md("<p>Um <strong>forte </strong>e um <em>leve</em>.</p><p></p><p>Dois.</p>"),
            "Um **forte** e um *leve*.\n\nDois.")

    def test_negrito_em_titulo_nao_vira_enfase(self):
        self.assertEqual(self.md("<h2><strong>Título</strong></h2><h3>Sub</h3>"), "## Título\n\n### Sub")

    def test_latex(self):
        html = ('<div class="latex-rendered" data-attrs="{&quot;persistentExpression&quot;:'
                '&quot;M = C\\\\,(1 + i\\\\,t)&quot;,&quot;id&quot;:&quot;X&quot;}"></div>')
        self.assertEqual(self.md(html), "$$ M = C\\,(1 + i\\,t) $$")

    def test_imagem_com_e_sem_legenda(self):
        html = ('<div class="captioned-image-container"><figure><a class="image-link"><div>'
                '<picture><img src="x.png" alt="alt"></picture><button><svg></svg></button>'
                '</div></a><figcaption class="image-caption">Risco <em>crescente</em>.</figcaption>'
                '</figure></div><div class="captioned-image-container"><figure><img src="y"></figure></div>')
        self.assertEqual(self.md(html), "![Risco *crescente*.](img-01)\n\n![](img-02)")

    def test_cta_simples_e_com_legenda(self):
        html = ('<p class="button-wrapper" data-attrs="{}"><a class="button primary" href="https://s/p/x">'
                '<span>Compartilhar</span></a></p>'
                '<div class="captioned-button-wrap"><div class="preamble"><p class="cta-caption">'
                'Obrigado por ler!</p></div><p class="button-wrapper"><a class="button primary" '
                'href="https://s/subscribe"><span>Assine</span></a></p></div>')
        self.assertEqual(self.md(html),
                         "[[CTA: Compartilhar → https://s/p/x]]\n\n"
                         "[[CTA: Assine → https://s/subscribe | Obrigado por ler!]]")

    def test_pullquote_lista_citacao_link_risco(self):
        html = ('<div class="pullquote"><p>Frase de destaque.</p></div>'
                '<ul><li><p>um</p></li><li><p>dois <a href="https://e.com">link</a></p></li></ul>'
                '<ol><li><p>a</p></li></ol><blockquote><p>cit 1</p><p>cit 2</p></blockquote>'
                '<p><s>Quase</s> Ninguém.</p><div><hr></div>')
        self.assertEqual(self.md(html),
                         "[[PULLQUOTE: Frase de destaque.]]\n\n- um\n- dois [link](https://e.com)\n\n"
                         "1. a\n\n> cit 1\n>\n> cit 2\n\n~~Quase~~ Ninguém.\n\n* * *")

    def test_codigo_e_enquete(self):
        html = ('<div class="highlighted_code_block" data-attrs="{&quot;language&quot;:&quot;python&quot;}">'
                '<pre class="shiki"><code>x = 1\n</code></pre></div><div class="poll-embed"></div>')
        self.assertEqual(self.md(html), "```python\nx = 1\n```\n\n[[ENQUETE]]")

    def test_contagem_inclui_legendas_e_exclui_url_e_latex(self):
        md = "Duas palavras.\n\n![Uma legenda](img-01)\n\n$$ a = b $$\n\n[[CTA: Assine → https://x.com/a | Obrigado]]"
        self.assertEqual(C.contar_palavras(md), 6)


class Volume(unittest.TestCase):
    def test_palavras_batem_com_a_api(self):
        arquivos = sorted(C.SAIDA.glob("*.md"))
        if not arquivos:
            self.skipTest("corpus ainda não normalizado")
        fora = []
        for f in arquivos:
            api = int(re.search(r"^wordcount_api: (\d+)", f.read_text(), re.M).group(1))
            md = int(re.search(r"^palavras_md: (\d+)", f.read_text(), re.M).group(1))
            if abs(md - api) > TOLERANCIA * api:
                fora.append(f"{f.stem}: api={api} md={md}")
        self.assertEqual(fora, [], "posts fora da tolerância de ±3%")


if __name__ == "__main__":
    unittest.main()
