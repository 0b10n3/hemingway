"""Testes do validador e do aplicador do parecer de marketing.

  python3 -m unittest scripts/test_parecer.py
"""
import copy
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import parecer as P  # noqa: E402

PARAGRAFOS = [
    "Abertura do post com o gancho logo de cara.",
    "Segundo parágrafo, ainda no primeiro quarto do texto.",
    "Terceiro parágrafo, em que o leitor encontra o texto sobre dias úteis e segue.",
    "Quarto parágrafo do meio do argumento.",
    "Quinto parágrafo do meio do argumento.",
    "Sexto parágrafo do meio do argumento.",
    "Sétimo parágrafo com a pergunta: qual foi a sua pior conta?",
    "Fecho do post, com 249 dias úteis em 2026.",
]
CORPO = "\n\n".join(PARAGRAFOS) + "\n\n## Para continuar aprendendo\n\n- Um livro qualquer.\n"
CATALOGO = {
    "substack:inscrever": {"tipo": "nativo", "url": None, "situacao": "disponível", "citavel": True, "titulo": "Inscrever"},
    "substack:comentar": {"tipo": "nativo", "url": None, "situacao": "disponível", "citavel": True, "titulo": "Comentar"},
    "oferta:skill-check": {"tipo": "captura", "url": "https://exemplo/skill", "situacao": "disponível", "citavel": True, "titulo": "Skill Check"},
    "oferta:fvdt": {"tipo": "curso", "url": None, "situacao": "em produção", "citavel": False, "titulo": "FVDT"},
    "post:du252": {"tipo": "post", "url": "https://exemplo/du252", "situacao": "disponível", "citavel": True, "titulo": "DU252"},
    "post:rascunho": {"tipo": "post", "url": None, "situacao": "não publicado", "citavel": False, "titulo": "Rascunho"},
    "legado:tesouro-selic": {"tipo": "post", "url": "https://exemplo/selic", "situacao": "disponível", "citavel": True, "titulo": "Selic"},
}
VALIDO = {
    "post": "teste",
    "diagnostico": {
        "linha_editorial": "Notas de um Professor", "voz": "explicativa", "segmento": "#GENZ-GREED",
        "eixo": "GREED", "estagio": "topo gratuito", "cluster": "matematica-financeira",
        "justificativas": [{"escolha": "gancho técnico", "trecho": "Abertura do post"}],
    },
    "alinhamento": [
        {"id": "A1", "criterio": "gancho-na-abertura", "veredito": "passa", "evidencia": "abre com gancho"},
        {"id": "A2", "criterio": "conformidade", "veredito": "não passa", "evidencia": "x",
         "trecho": "Quarto parágrafo", "o_que_mudaria": "tirar o nome do emissor"},
    ],
    "ctas": [
        {"id": "C1", "papel": "inscricao", "tipo": "inscricao", "formato": "botao_nativo",
         "ancora": "Segundo parágrafo", "destino_id": "substack:inscrever", "motivo": "primeiro quarto"},
        {"id": "C2", "papel": "inscricao", "tipo": "inscricao", "formato": "botao_nativo",
         "ancora": "Fecho do post", "destino_id": "substack:inscrever", "motivo": "fim"},
        {"id": "C3", "papel": "principal", "tipo": "skill_check", "formato": "texto",
         "ancora": "Sexto parágrafo", "texto_sugerido": "Se quiser medir onde você está, faça o Syntaxis Skill Check.",
         "texto_link": "Syntaxis Skill Check", "destino_id": "oferta:skill-check", "motivo": "próximo passo"},
        {"id": "C4", "papel": "secundario", "tipo": "comentar", "formato": "botao_nativo",
         "ancora": "qual foi a sua pior conta?", "destino_id": "substack:comentar", "motivo": "pergunta ao leitor"},
    ],
    "referencias": [
        {"id": "R1", "ancora": "o texto sobre dias úteis", "texto_link": "texto sobre dias úteis",
         "destino_id": "post:du252", "pergunta_do_leitor": "que texto?"},
    ],
    "backlinks_sugeridos": [
        {"id": "B1", "origem_id": "legado:tesouro-selic", "ancora_na_origem": None,
         "texto_link": "contagem de dias úteis", "motivo": "mesmo cluster"},
    ],
    "riscos": [],
}


def erros(mutacao=None):
    p = copy.deepcopy(VALIDO)
    if mutacao:
        mutacao(p)
    return P.checar(p, CORPO, CATALOGO, "teste", "")


def cta(i):
    return lambda p: p["ctas"][i]


class Validar(unittest.TestCase):
    def assertReprova(self, mutacao, trecho):
        e = erros(mutacao)
        self.assertTrue(any(trecho in x for x in e), f"esperava {trecho!r} em {e}")

    def test_valido(self):
        self.assertEqual(erros(), [])

    def test_nenhuma_sugestao_e_valido(self):
        self.assertEqual(erros(lambda p: (p["referencias"].clear(), p["backlinks_sugeridos"].clear())), [])

    def test_esquema(self):
        self.assertReprova(lambda p: p.pop("riscos"), "esquema")
        self.assertReprova(lambda p: p["ctas"][0].update(papel="banner"), "esquema")
        self.assertReprova(lambda p: p["ctas"][2].pop("texto_sugerido"), "esquema")
        self.assertReprova(lambda p: p["alinhamento"][1].pop("o_que_mudaria"), "esquema")

    def test_ancora_inexistente(self):
        self.assertReprova(lambda p: p["referencias"][0].update(ancora="frase que não existe"), "aparece 0 vez")

    def test_ancora_repetida(self):
        self.assertReprova(lambda p: p["ctas"][2].update(ancora="parágrafo do meio do argumento"), "aparece 3 vez")

    def test_trecho_do_diagnostico_inventado(self):
        self.assertReprova(lambda p: p["diagnostico"]["justificativas"][0].update(trecho="citação inventada"),
                           "trecho não aparece")

    def test_destino_fora_do_catalogo(self):
        self.assertReprova(lambda p: p["referencias"][0].update(destino_id="post:inventado"), "não existe no catálogo")

    def test_destino_sem_url(self):
        self.assertReprova(lambda p: p["referencias"][0].update(destino_id="post:rascunho"), "não é citável")

    def test_oferta_indisponivel(self):
        self.assertReprova(lambda p: p["ctas"][2].update(destino_id="oferta:fvdt"), "não é citável")

    def test_link_para_si_mesmo(self):
        self.assertReprova(lambda p: p["referencias"][0].update(destino_id="post:teste"), "não existe no catálogo")

    def test_dois_principais(self):
        self.assertReprova(lambda p: p["ctas"][3].update(papel="principal"), "papel principal")

    def test_tres_secundarios(self):
        def m(p):
            for i in (0, 1, 2):
                extra = copy.deepcopy(p["ctas"][3])
                extra["id"] = f"C{9 + i}"
                p["ctas"].append(extra)
        self.assertReprova(m, "papel secundario")

    def test_falta_inscricao_no_primeiro_quarto(self):
        self.assertReprova(lambda p: p["ctas"][0].update(ancora="Quinto parágrafo"), "primeiro quarto")

    def test_falta_inscricao_no_fim(self):
        self.assertReprova(lambda p: p["ctas"][1].update(ancora="Quarto parágrafo"), "fim do post")

    def test_mais_de_quatro_referencias(self):
        def m(p):
            for i in range(4):
                r = copy.deepcopy(p["referencias"][0])
                r["id"] = f"R{i + 2}"
                p["referencias"].append(r)
        self.assertReprova(m, "máximo 4")

    def test_link_generico(self):
        for g in ("clique aqui", "Aqui", "leia mais", "Saiba mais.", "este link"):
            with self.subTest(g):
                self.assertReprova(lambda p: p["referencias"][0].update(
                    ancora="Terceiro parágrafo", frase_nova=f"Veja {g}.", texto_link=g), "genérico")

    def test_texto_link_fora_da_ancora(self):
        self.assertReprova(lambda p: p["referencias"][0].update(texto_link="curva de juros"), "dentro de ancora")

    def test_emoji(self):
        self.assertReprova(lambda p: p["ctas"][2].update(
            texto_sugerido="Faça o Syntaxis Skill Check 🚀"), "emoji")
        self.assertReprova(lambda p: p["ctas"][2].update(
            texto_sugerido="Faça o Syntaxis Skill Check ❤"), "emoji")

    def test_numero_sem_fonte(self):
        self.assertReprova(lambda p: p["ctas"][2].update(
            texto_sugerido="87% dos analistas fazem o Syntaxis Skill Check."), "sem fonte")
        self.assertEqual(erros(lambda p: p["ctas"][2].update(
            texto_sugerido="Os 249 dias úteis de 2026 cabem no Syntaxis Skill Check.")), [])

    def test_botao_nativo_com_destino_externo(self):
        self.assertReprova(lambda p: p["ctas"][3].update(destino_id="oferta:skill-check"), "botão nativo")

    def test_cta_com_url_sem_texto_link(self):
        self.assertReprova(lambda p: p["ctas"][2].pop("texto_link"), "texto_link")

    def test_backlink_de_origem_inexistente(self):
        self.assertReprova(lambda p: p["backlinks_sugeridos"][0].update(origem_id="post:inventado"), "não é outro post")

    def test_id_repetido(self):
        self.assertReprova(lambda p: p["ctas"][3].update(id="C1"), "id repetido")


class Aplicar(unittest.TestCase):
    """Usa o catálogo real (marketing/catalogo.json)."""

    def setUp(self):
        self.dir = Path(tempfile.mkdtemp())
        self.post = self.dir / "post.md"
        self.post.write_text("---\ntitulo: Teste\n---\n" + CORPO, encoding="utf-8")
        p = copy.deepcopy(VALIDO)
        p["ctas"][2]["destino_id"] = "oferta:skill-check"
        p["referencias"][0]["destino_id"] = "post:2026-10-30-du252-contagem-de-dias"
        (self.dir / "marketing.json").write_text(json.dumps(p, ensure_ascii=False), encoding="utf-8")
        self.cat = P._catalogo()

    def tearDown(self):
        shutil.rmtree(self.dir)

    def rodar(self, *ids):
        saida = io.StringIO()
        antigo, sys.stdout = sys.stdout, saida
        try:
            P.aplicar(str(self.dir), list(ids))
        finally:
            sys.stdout = antigo
        return self.post.read_text(encoding="utf-8"), saida.getvalue()

    def test_so_muda_os_itens_aceitos(self):
        novo, saida = self.rodar("C3", "R1", "C1")
        skill = self.cat["oferta:skill-check"]["url"]
        du = self.cat["post:2026-10-30-du252-contagem-de-dias"]["url"]
        esperado = ("---\ntitulo: Teste\n---\n" + CORPO
                    .replace("texto sobre dias úteis", f"[texto sobre dias úteis]({du})")
                    .replace("Sexto parágrafo do meio do argumento.",
                             "Sexto parágrafo do meio do argumento.\n\nSe quiser medir onde você está, "
                             f"faça o [Syntaxis Skill Check]({skill})."))
        self.assertEqual(novo, esperado)
        self.assertIn("botão de inscrição depois do 2º parágrafo da abertura", saida)

    def test_texto_do_autor_substitui_o_sugerido(self):
        novo, _ = self.rodar("C3=Quer saber onde está? Syntaxis Skill Check.")
        self.assertIn("Quer saber onde está? [Syntaxis Skill Check](", novo)

    def test_itens_de_redacao_nao_mexem_no_texto(self):
        novo, saida = self.rodar("A2", "B1")
        self.assertEqual(novo, "---\ntitulo: Teste\n---\n" + CORPO)
        self.assertIn("etapa 4", saida)


class Guarda(unittest.TestCase):
    def rodar(self, caminho):
        entrada = json.dumps({"tool_input": {"file_path": caminho}})
        return subprocess.run([sys.executable, str(Path(P.__file__)), "guarda"], input=entrada,
                              capture_output=True, text=True).returncode

    def test_so_marketing_json(self):
        self.assertEqual(self.rodar("/x/hemingway/posts/2026-11-02-a/marketing.json"), 0)
        self.assertEqual(self.rodar("/x/hemingway/posts/2026-11-02-a/post.md"), 2)
        self.assertEqual(self.rodar("/x/hemingway/marketing/catalogo.json"), 2)


if __name__ == "__main__":
    unittest.main()
