"""Testes do kit de distribuição (scripts/kit.py) contra o config/esteira.yaml real.

  python3 -m unittest scripts/test_kit.py
"""
import copy
import datetime as dt
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kit as K  # noqa: E402

CFG = K.ler_config()
POST = """---
titulo: Você está contando os dias úteis errado
linha_editorial: Notas de um Professor
---

Uma LTN comprada a 12% ao ano, com liquidação no primeiro dia útil de 2026, vence em 1º de janeiro
de 2027. Entrega 11,85% no período. 2026 tem 249 dias úteis. A taxa vale para cada 252. O valor de
face é R$ 1.000.
"""
FONTES = K.numeros(POST)
CATALOGO = {
    "substack:inscrever": {"tipo": "nativo", "titulo": "Botão de inscrição", "citavel": True},
    "oferta:fvdt": {"tipo": "curso", "titulo": "Fundamentos do Valor do Dinheiro no Tempo (FVDT)", "citavel": False,
                    "termos": ["FVDT"]},
    "oferta:brinde-assinatura": {"tipo": "brinde", "titulo": "Brinde de assinatura", "citavel": False,
                                 "termos": ["brinde"]},
    "post:rascunho": {"tipo": "post", "titulo": "Um post", "citavel": False},
}
NOTAS = [
    ("N1", "note-d0", "substack-notes", "Uma LTN comprada a 12% ao ano entrega 11,85% no período. Ninguém errou "
     "a conta: 2026 tem 249 dias úteis, e a taxa vale para cada 252.\n\nQual foi a última conta sua que não bateu "
     "por causa do calendário?\n{{URL_POST}}"),
    ("L1", "video-d1", "linkedin", "2026 tem 249 dias úteis, e isso muda a conta da LTN.\n\nNa sua mesa, quem "
     "confere o calendário?\n{{URL_POST}}"),
    ("L2", "video-d1", "instagram-reels", "2026 tem 249 dias úteis. Texto completo: link na bio. Você confere a "
     "régua antes da taxa?"),
    ("L3", "video-d1", "youtube-shorts-titulo", "2026 tem 249 dias úteis"),
    ("L4", "video-d1", "youtube-shorts-descricao", "A taxa vale para cada 252 dias úteis. Você já conferiu a sua?"),
    ("N2", "note-d2", "substack-notes", "Uma taxa de juros, sozinha, não é informação completa. É um número "
     "esperando uma régua. Qual régua você usa?"),
    ("L5", "carrossel-d6", "linkedin", "Uma taxa sem régua não é informação.\n\nQual peça mais confunde quem "
     "chega na mesa?\nhttps://syntaxis.substack.com/subscribe"),
    ("L6", "carrossel-d6", "instagram", "Uma taxa sem régua não é informação. Link na bio. Qual peça te confunde?"),
]
SPOILER = [
    ("N1", "note-d0", "substack-notes", "Ficar custou caro. Sair também. Qual foi a sua data?\n{{URL_POST}}"),
    ("P1", "post-linkedin-d2", "linkedin", "Ficar custou caro. Sair também.\n\nVocê já escolheu a sua data?\n"
     "{{URL_POST}}"),
    ("N2", "note-d2", "substack-notes", "Clima ruim não é motivo para sair. Trabalho que parou de trabalhar por "
     "você, é. Qual é o seu caso?"),
    ("L1", "carrossel-d6", "linkedin", "Ficar custou caro. Que sinal você esperou demais para ler?"),
    ("L2", "carrossel-d6", "instagram", "Ficar custou caro. Link na bio. Que sinal você ignorou?"),
]


def kit(linha="Notas de um Professor", data=dt.date(2026, 12, 1)):
    return K.montar_kit(CFG, "teste", {"titulo": "Teste", "linha_editorial": linha}, data)


def md(blocos):
    return "".join(f"## {i} · {p} · {c}\n\n{t}\n\n" for i, p, c, t in blocos)


def trocar(blocos, id_, texto):
    return [(i, p, c, texto if i == id_ else t) for i, p, c, t in blocos]


def erros(k=None, blocos=NOTAS, catalogo=CATALOGO):
    return K.checar(k or kit(), md(blocos), CFG, FONTES, catalogo)


class Checar(unittest.TestCase):
    def assertReprova(self, trecho, **kw):
        e = erros(**kw)
        self.assertTrue(any(trecho in x for x in e), f"esperava {trecho!r} em {e}")

    def test_notas_valido(self):
        self.assertEqual(erros(), [])

    def test_spoiler_valido(self):
        self.assertEqual(erros(kit("Spoiler", dt.date(2026, 12, 4)), SPOILER), [])

    def test_esquema(self):
        k = kit()
        k["pecas"][0].pop("retorno")
        self.assertReprova("esquema 1.0", k=k)
        k = kit()
        k["pecas"][0]["situacao"] = "publicado"
        self.assertReprova("esquema 1.0", k=k)

    def test_falta_peca(self):
        k = kit()
        k["pecas"].pop(1)
        self.assertReprova("falta a peça video-d1", k=k)

    def test_peca_sobrando(self):
        k = kit()
        extra = copy.deepcopy(k["pecas"][0])
        extra["id"] = "note-d4"
        k["pecas"].append(extra)
        self.assertReprova("note-d4 não está prevista", k=k)

    def test_dia_de_publicacao_errado(self):
        self.assertReprova("cai numa segunda", k=kit(data=dt.date(2026, 11, 30)))

    def test_data_antecipada(self):
        k = kit()
        k["pecas"][1]["data"] = k["post"]["data_publicacao"]
        self.assertReprova("antes de data_publicacao", k=k)

    def test_data_adiada_passa(self):
        k = kit()
        k["pecas"][1]["data"] = (dt.date.fromisoformat(k["pecas"][1]["data"]) + dt.timedelta(1)).isoformat()
        self.assertEqual(erros(k=k), [])

    def test_sabado(self):
        # Spoiler numa quinta: a peça D+2 cai no sábado.
        self.assertReprova("sabado, dia sem publicação", k=kit("Spoiler", dt.date(2026, 12, 3)), blocos=SPOILER)

    def test_limite_de_caracteres(self):
        # 590 + "?" + quebra + {{URL_POST}} contado como 80 = 672 > 600
        self.assertReprova("limite 600", blocos=trocar(NOTAS, "N1", "a" * 590 + "?\n{{URL_POST}}"))
        self.assertReprova("limite 100", blocos=trocar(NOTAS, "L3", "a" * 101))

    def test_sem_pergunta(self):
        self.assertReprova("N2: não termina com uma pergunta", blocos=trocar(NOTAS, "N2", "A taxa precisa de régua."))
        self.assertReprova("N1: não termina com uma pergunta",
                           blocos=trocar(NOTAS, "N1", "Qual foi? Leia o texto completo: {{URL_POST}}"))

    def test_note_d0_sem_link(self):
        self.assertReprova("N1: falta {{URL_POST}}", blocos=trocar(NOTAS, "N1", "2026 tem 249 dias úteis. E você?"))

    def test_note_d2_com_link(self):
        self.assertReprova("N2: não pode ter URL", blocos=trocar(NOTAS, "N2", "Qual régua você usa?\n{{URL_POST}}"))

    def test_instagram_com_link(self):
        self.assertReprova("L6: não pode ter URL",
                           blocos=trocar(NOTAS, "L6", "Qual peça te confunde?\nhttps://syntaxis.substack.com/subscribe"))

    def test_post_linkedin_sem_link(self):
        self.assertReprova("P1: falta {{URL_POST}}", k=kit("Spoiler", dt.date(2026, 12, 4)),
                           blocos=trocar(SPOILER, "P1", "Ficar custou caro. E você?"))

    def test_url_fora_da_esteira(self):
        self.assertReprova("URL fora da esteira", blocos=trocar(NOTAS, "N1", "Qual foi?\nhttps://bit.ly/x"))

    def test_emoji(self):
        self.assertReprova("N2: contém emoji", blocos=trocar(NOTAS, "N2", "Qual régua você usa? 📈"))

    def test_hashtag(self):
        self.assertReprova("hashtag", blocos=trocar(NOTAS, "L6", "#rendafixa Qual peça te confunde?"))

    def test_numero_sem_fonte(self):
        self.assertReprova("número '87'", blocos=trocar(NOTAS, "N2", "87% erram a régua. E você?"))

    def test_numero_normalizado(self):
        self.assertEqual(erros(blocos=trocar(NOTAS, "N2", "Face de R$ 1.000, taxa de 11,850% no período. E você?")), [])

    def test_oferta_indisponivel(self):
        self.assertReprova("menciona 'brinde'", blocos=trocar(NOTAS, "L6", "Assine e ganhe o brinde. Quer?"))
        self.assertReprova("menciona 'FVDT'", blocos=trocar(NOTAS, "N2", "Está no FVDT. Quer?"))
        cat = copy.deepcopy(CATALOGO)
        cat["oferta:brinde-assinatura"]["citavel"] = True
        self.assertEqual(erros(blocos=trocar(NOTAS, "L6", "Assine e ganhe o brinde. Quer?"), catalogo=cat), [])

    def test_texto_faltando(self):
        self.assertReprova("falta o texto de video-d1 · youtube-shorts-titulo",
                           blocos=[b for b in NOTAS if b[0] != "L3"])

    def test_texto_repetido(self):
        self.assertReprova("repete note-d2", blocos=NOTAS + [("N9", "note-d2", "substack-notes", "De novo?")])

    def test_canal_nao_previsto(self):
        self.assertReprova("não está previsto", blocos=NOTAS + [("N9", "note-d2", "linkedin", "Outro canal?")])

    def test_esqueleto_vazio_reprova(self):
        e = K.checar(kit(), K.esqueleto(kit(), CFG), CFG, FONTES, CATALOGO)
        self.assertEqual(len([x for x in e if "texto vazio" in x]), 8)


class Datas(unittest.TestCase):
    def test_proximo_dia(self):
        seg = dt.date(2026, 11, 23)
        self.assertEqual(K.proximo_dia(CFG, "notas-de-um-professor", seg), dt.date(2026, 11, 24))
        self.assertEqual(K.proximo_dia(CFG, "spoiler", seg), dt.date(2026, 11, 27))
        self.assertEqual(K.proximo_dia(CFG, "notas-de-um-professor", dt.date(2026, 11, 24)), dt.date(2026, 11, 24))

    def test_datas_do_kit(self):
        datas = {p["id"]: p["data"] for p in kit()["pecas"]}
        self.assertEqual(datas, {"note-d0": "2026-12-01", "video-d1": "2026-12-02", "note-d2": "2026-12-03",
                                 "carrossel-d6": "2026-12-07"})

    def test_esqueleto_numera_por_data(self):
        ids = [(i, p, c) for i, p, c, _ in K.ler_textos(K.esqueleto(kit("Spoiler", dt.date(2026, 12, 4)), CFG))]
        self.assertEqual(ids, [("N1", "note-d0", "substack-notes"), ("P1", "post-linkedin-d2", "linkedin"),
                               ("N2", "note-d2", "substack-notes"), ("L1", "carrossel-d6", "linkedin"),
                               ("L2", "carrossel-d6", "instagram")])


class Arquivos(unittest.TestCase):
    """montar, url e validar num post de mentira, em pasta temporária."""

    def setUp(self):
        self.dir = Path(tempfile.mkdtemp())
        (self.dir / "post.md").write_text(POST, encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.dir)

    def quieto(self, f, *a, **kw):
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            return f(*a, **kw)

    def test_montar_nao_sobrescreve(self):
        self.quieto(K.montar, str(self.dir), "2026-12-01")
        dist = self.dir / "distribuicao"
        self.assertEqual(json.loads((dist / "kit.json").read_text())["pecas"][0]["situacao"], "aguarda-url")
        self.assertIn("## N1 · note-d0 · substack-notes", (dist / "textos.md").read_text())
        with self.assertRaises(SystemExit):
            self.quieto(K.montar, str(self.dir), "2026-12-01")
        self.quieto(K.montar, str(self.dir), "2026-12-08", substituir=True)
        self.assertEqual(json.loads((dist / "kit.json").read_text())["post"]["data_publicacao"], "2026-12-08")

    def test_url_troca_o_marcador_e_revalida(self):
        self.quieto(K.montar, str(self.dir), "2026-12-01")
        dist = self.dir / "distribuicao"
        (dist / "textos.md").write_text(md(NOTAS), encoding="utf-8")
        with self.assertRaises(SystemExit):  # sem url_publicada
            self.quieto(K.url, str(self.dir))
        u = "https://syntaxis.substack.com/p/teste"
        (self.dir / "post.md").write_text(POST.replace("---\n\n", f"url_publicada: {u}\n---\n\n"), encoding="utf-8")
        self.assertEqual(self.quieto(K.url, str(self.dir)), 0)
        textos = (dist / "textos.md").read_text()
        self.assertNotIn(K.MARCADOR, textos)
        self.assertIn(u, textos)
        k = json.loads((dist / "kit.json").read_text())
        self.assertEqual(k["post"]["url"], u)
        self.assertNotIn("aguarda-url", {p["situacao"] for p in k["pecas"]})
        self.assertIn("Kit válido", (dist / "kit.md").read_text())


class Guarda(unittest.TestCase):
    def rodar(self, caminho):
        entrada = json.dumps({"tool_input": {"file_path": caminho}})
        return subprocess.run([sys.executable, str(Path(K.__file__)), "guarda"], input=entrada,
                              capture_output=True, text=True).returncode

    def test_so_textos_md(self):
        self.assertEqual(self.rodar("/x/hemingway/posts/2026-12-01-a/distribuicao/textos.md"), 0)
        self.assertEqual(self.rodar("/x/hemingway/posts/2026-12-01-a/distribuicao/kit.json"), 2)
        self.assertEqual(self.rodar("/x/hemingway/posts/2026-12-01-a/post.md"), 2)

    def test_roteiro_e_storyboard_do_video(self):
        self.assertEqual(self.rodar("/x/hemingway/posts/2026-12-01-a/distribuicao/video/roteiro.md"), 0)
        self.assertEqual(self.rodar("/x/hemingway/posts/2026-12-01-a/distribuicao/video/storyboard.json"), 0)
        self.assertEqual(self.rodar("/x/hemingway/posts/2026-12-01-a/distribuicao/video/storyboard.md"), 2)


if __name__ == "__main__":
    unittest.main()
