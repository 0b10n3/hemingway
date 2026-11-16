"""Testes da checagem mecânica de post.

  python3 -m unittest scripts/test_checar_post.py
"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import checar_post as C  # noqa: E402

FM = "---\ntitulo: Um título\nsubtitulo: Um subtítulo\ndata: 2026-11-20\nlinha_editorial: Spoiler\nstatus: aprovado\n---\n\n"
CURTO = "Uma frase curta e limpa aqui.\n\nOutra frase, também curta."


def checar(corpo, frontmatter=FM, extras=None, nome="post.md"):
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / nome
        p.write_text(frontmatter + corpo)
        for arq, conteudo in (extras or {}).items():
            (Path(d) / arq).write_text(conteudo)
        return C.checar(p)


class Bloqueantes(unittest.TestCase):
    def test_post_limpo_passa(self):
        self.assertEqual(checar(CURTO), ([], []))

    def test_marcadores_do_processo(self):
        bloq, _ = checar(CURTO + "\n\nUm dado [VERIFICAR: fonte]. Um link [LINK: post] e [PREENCHER: memória].")
        self.assertEqual(len(bloq), 3)

    def test_marcador_de_botao_do_site_nao_conta(self):
        self.assertEqual(checar(CURTO + "\n\n[[CTA: Compartilhar → https://x]]", nome="publicado.md")[0], [])

    def test_jargao_do_pipeline(self):
        bloq, _ = checar(CURTO + "\n\nIsso vale checar na etapa de pesquisa do próximo post.")
        self.assertTrue(any("jargão" in b for b in bloq))

    def test_pipelines_de_dados_nao_e_jargao(self):
        self.assertEqual(checar(CURTO + "\n\nA planilha migrou para *pipelines* que processam séries.")[0], [])

    def test_frontmatter_minimo(self):
        bloq, _ = checar(CURTO, frontmatter="---\ntitulo: X\n---\n\n")
        self.assertEqual(sorted(b.split("`")[1] for b in bloq), ["data", "linha_editorial", "status", "subtitulo"])

    def test_placeholder_orfao_nos_dois_sentidos(self):
        corpo = CURTO + "\n\n![Gráfico: algo](graf-01)"
        spec = "## graf-01\nrangemode='tozero'\n\n## graf-02\nrangemode='tozero'\n"
        bloq, _ = checar(corpo, extras={"graficos.md": spec})
        self.assertEqual(bloq, ["bloco de spec sem placeholder no post: graf-02"])
        bloq, _ = checar(corpo + "\n\n![Diagrama: x](diag-01)", extras={"graficos.md": "## graf-01\nrangemode\n"})
        self.assertEqual(bloq, ["placeholder sem bloco de spec: diag-01"])


class Avisos(unittest.TestCase):
    def test_paragrafo_longo(self):
        _, aviso = checar(CURTO + "\n\n" + "palavra " * 95)
        self.assertTrue(any("parágrafo de 95 palavras" in a for a in aviso))

    def test_travessao_acima_do_teto_e_em_subtitulo(self):
        _, aviso = checar("Um texto — com travessão — em cada canto — de novo.\n\nE mais um — aqui.",
                          frontmatter=FM.replace("Um subtítulo", "Um subtítulo — e por que"))
        self.assertTrue(any("por mil" in a for a in aviso))
        self.assertTrue(any("título ou subtítulo" in a for a in aviso))

    def test_rotulo_de_movimento_e_exclamacao(self):
        _, aviso = checar(CURTO + "\n\n## Fechamento: sem rede\n\nQue texto!")
        self.assertTrue(any("rótulo de movimento" in a for a in aviso))
        self.assertTrue(any("exclamação" in a for a in aviso))

    def test_antitese_acima_do_teto_na_secao(self):
        um = "## Seção\n\nIsso não é sorte. É método."
        self.assertEqual(checar(um)[1], [])
        _, aviso = checar(um + " Também não é talento. É repetição.")
        self.assertTrue(any("antíteses" in a for a in aviso))

    def test_tufte_sem_rangemode(self):
        _, aviso = checar(CURTO + "\n\n![G](graf-01)", extras={"graficos.md": "## graf-01\nfig.show()\n"})
        self.assertTrue(any("Tufte" in a for a in aviso))


if __name__ == "__main__":
    unittest.main()
