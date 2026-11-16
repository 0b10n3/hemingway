"""Testes das triplas de edição (rascunho -> post.md -> publicado).

  python3 -m unittest scripts/test_diff_edicoes.py
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import diff_edicoes as D  # noqa: E402

COMUM = ("Esta frase longa existe nas três versões e serve de âncora para o alinhamento funcionar "
         "direito em todos os casos de teste que vêm a seguir.")


def ops(rascunho, post, publicado):
    t = lambda s: D.tokens(s)[0]  # noqa: E731
    return D.operacoes(t(rascunho), t(post), t(publicado), vocab_unico=set())


def classes(lista):
    return [o["classe"] for o in lista]


class Triplas(unittest.TestCase):
    def test_divisao_nova_e_divisao_que_restaura_o_rascunho(self):
        nova = ops(f"{COMUM} Uma frase. Outra frase.", f"{COMUM} Uma frase. Outra frase.",
                   f"{COMUM} Uma frase.\n\nOutra frase.")
        self.assertEqual(classes(nova), ["divisao_paragrafo"])
        self.assertIs(nova[0]["restaurou_rascunho"], False)
        restaura = ops(f"{COMUM} Uma frase.\n\nOutra frase.", f"{COMUM} Uma frase. Outra frase.",
                       f"{COMUM} Uma frase.\n\nOutra frase.")
        self.assertEqual(restaura[0]["sinais"], ["reversao"])

    def test_negrito_que_o_pipeline_tirou_e_o_autor_devolveu(self):
        r = ops(f"{COMUM} Olhe a **derivada**, não o nível.", f"{COMUM} Olhe a derivada, não o nível.",
                f"{COMUM} Olhe a **derivada**, não o nível.")
        self.assertEqual(classes(r), ["negrito_adicionado"])
        self.assertTrue(r[0]["restaurou_rascunho"])

    def test_autor_corta_texto_que_o_pipeline_inseriu(self):
        r = ops(f"{COMUM} Fim do argumento.",
                f"{COMUM} Um levantamento recente mostra outra coisa. Fim do argumento.",
                f"{COMUM} Fim do argumento.")
        self.assertEqual(classes(r), ["remocao"])
        self.assertEqual(r[0]["origem_antes"], "pipeline")
        self.assertIn("reversao", r[0]["sinais"])

    def test_autor_devolve_a_palavra_do_rascunho(self):
        r = ops(f"{COMUM} O coqueiro seria o símbolo do nativo.", f"{COMUM} O coqueiro é o símbolo do nativo.",
                f"{COMUM} O coqueiro seria o símbolo do nativo.")
        self.assertEqual(classes(r), ["substituicao"])
        self.assertTrue(r[0]["restaurou_rascunho"])
        self.assertNotIn("acrescimo_autoral", r[0]["sinais"])

    def test_acrescimo_autoral_longo(self):
        r = ops(f"{COMUM} Fim.", f"{COMUM} Fim.",
                f"{COMUM} Fim. Uma frase inteiramente nova escrita só no editor do site.")
        self.assertEqual(r[0]["sinais"], ["acrescimo_autoral"])

    def test_aspas_tipograficas_nao_sao_substituicao(self):
        r = ops(f"{COMUM} A 'mesa' decide, can't.", f"{COMUM} A 'mesa' decide, can't.",
                f"{COMUM} A ‘mesa’ decide, can’t.")
        self.assertEqual(classes(r), ["tipografia_aspas"])
        self.assertEqual(r[0]["ocorrencias"], 2)

    def test_imagem_formula_e_tabela_sao_blocos_especiais(self):
        r = ops("", f"{COMUM}\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\n$$ M = C\\,(1+i) $$",
                f"{COMUM}\n\n![Legenda](img-01)\n\n$$ M = C(1+i) $$")
        self.assertEqual(sorted(classes(r)), ["imagem", "tabela"])  # fórmula igual a menos de espaço


class Preferencias(unittest.TestCase):
    def test_agrupa_conta_por_linha_e_ignora_layout(self):
        op = lambda classe, natureza="estilo", sinais=(), antes="x", origem="rascunho": {  # noqa: E731
            "classe": classe, "natureza": natureza, "sinais": list(sinais), "antes": antes, "depois": "",
            "palavras_antes": 3, "palavras_depois": 0, "origem_antes": origem, "contexto": "a [[…]] b"}
        eds = [{"slug_repo": "p1", "linha_editorial": "Spoiler",
                "operacoes": [op("divisao_paragrafo"), op("remocao", sinais=["reversao"]), op("imagem", "layout-substack")]},
               {"slug_repo": "p2", "linha_editorial": "Notas de um Professor",
                "operacoes": [op("divisao_paragrafo"), op("remocao", "conteúdo/fato", origem="pipeline")]}]
        linhas = {x["preferencia"]: x for x in D.linhas_preferencias(eds)}
        self.assertEqual(set(linhas), {"Divide parágrafo", "Corta trecho",
                                       "Corta dado ou trecho de conteúdo que o pipeline trouxe"})
        self.assertEqual((linhas["Divide parágrafo"]["vezes"], linhas["Divide parágrafo"]["spoiler"],
                          linhas["Divide parágrafo"]["notas"]), (2, 1, 1))
        self.assertEqual(linhas["Corta trecho"]["desfaz_pipeline"], 1)


if __name__ == "__main__":
    unittest.main()
