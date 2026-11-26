"""Testes do validador do storyboard do vídeo (scripts/storyboard.py) contra o config/esteira.yaml real.

  python3 -m unittest scripts/test_storyboard.py
"""
import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kit as K  # noqa: E402
import storyboard as SB  # noqa: E402

CFG = K.ler_config()
POST = ("Em 13 de outubro, o Tesouro Prefixado 2029 custava R$ 773,74, a 12,40% ao ano. "
        "A Selic estava em 13,75%. Na tela, 3,6% a menos que em 13 de outubro.")
FONTES = K.numeros(POST)
KIT = {"pecas": [{"id": "video-d1", "tipo": "video", "data": "2026-11-25"}]}
BASE = {
    "versao_esquema": "1.0",
    "post": {"slug": "x", "linha": "notas-de-um-professor", "titulo": "X", "data_video": "2026-11-25"},
    "estrategia": {"segmento": "#GENZ-GREED", "eixo": "GREED", "estagio_funil": "topo gratuito", "cta": "o texto completo"},
    "formato": {"largura": 1080, "altura": 1920, "fps": 30, "duracao_alvo_s": [5, 90]},
    "tomadas": [{"id": "T1", "bloco": "gancho",
                 "fala": "Em cinco semanas, o Tesouro Prefixado 2029 perdeu 3,6%.\nE a Selic nem se mexeu.\nComo assim?"}],
    "cenas": [{"id": "S1", "tomada": "T1", "ancora_inicio": "Em cinco semanas", "ancora_fim": "Como assim?",
               "visual": "camera",
               "cartao": {"id": "C1", "modo": "sobreposto", "chassi": "B", "eyebrow": "TESOURO PREFIXADO 2029",
                          "texto": "Selic: 13,75% → 13,75%", "destaque": "−3,6%"},
               "numeros": [{"valor": "3,6%", "fonte": "Na tela, 3,6% a menos que em 13 de outubro."}]}],
    "capa": {"chassi": "B", "eyebrow": "TESOURO PREFIXADO 2029", "texto": "com a Selic parada", "destaque": "−3,6%"},
    "legenda": {"palavras_por_bloco_max": 4, "destaque_palavra_falada": False},
    "fechamento": {"pergunta": "Qual foi o motivo do seu primeiro prefixado?", "convite": "o texto completo está na Syntaxis"},
}


def erros(sb, md=None):
    return SB.checar(sb, KIT, CFG, FONTES, POST, md)


def com(**mud):
    sb = copy.deepcopy(BASE)
    for caminho, valor in mud.items():
        alvo = sb
        partes = caminho.split("__")
        for p in partes[:-1]:
            alvo = alvo[int(p)] if p.isdigit() else alvo[p]
        alvo[partes[-1]] = valor
    return sb


class Valido(unittest.TestCase):
    def test_storyboard_base_passa(self):
        self.assertEqual(erros(BASE, SB.renderizar(BASE, CFG)), [])

    def test_storyboard_real_do_primeiro_video_passa(self):
        self.assertEqual(SB.validar("2026-11-23-a-peca-mais-simples"), 0)


class Reprova(unittest.TestCase):
    def test_esquema(self):
        e = erros(com(versao_esquema="2.0"))
        self.assertTrue(e and "esquema" in e[0])

    def test_campo_desconhecido(self):
        self.assertTrue(any("esquema" in x for x in erros(com(cenas__0__cartao__cor="lime"))))

    def test_data_diferente_do_kit(self):
        self.assertTrue(any("data_video" in x for x in erros(com(post__data_video="2026-11-26"))))

    def test_ancora_nao_literal(self):
        self.assertTrue(any("ancora_fim" in x for x in erros(com(cenas__0__ancora_fim="como assim, gente?"))))

    def test_duracao_fora_da_faixa(self):
        self.assertTrue(any("duração estimada" in x for x in erros(com(formato__duracao_alvo_s=[45, 90]))))

    def test_tomada_longa_sem_excecao(self):
        longa = " ".join(["palavra"] * 70) + ". Em cinco semanas, Como assim?"
        self.assertTrue(any("acima de 20 s" in x for x in erros(com(tomadas__0__fala=longa))))
        self.assertFalse(any("acima de 20 s" in x for x in erros(com(tomadas__0__fala=longa, tomadas__0__excecao="motivo"))))

    def test_cartao_com_palavras_demais(self):
        texto = " ".join(["palavra"] * 16)
        self.assertTrue(any("C1" in x and "palavras" in x for x in erros(com(cenas__0__cartao__texto=texto))))

    def test_numero_fora_do_post(self):
        self.assertTrue(any("99" in x for x in erros(com(cenas__0__cartao__texto="Selic: 99%"))))

    def test_fonte_do_numero_nao_literal(self):
        e = erros(com(cenas__0__numeros=[{"valor": "3,6%", "fonte": "caiu 3,6%"}]))
        self.assertTrue(any("fonte de 3,6%" in x for x in e))

    def test_emoji(self):
        self.assertTrue(any("emoji" in x for x in erros(com(capa__texto="com a Selic parada 📉"))))

    def test_fechamento_sem_pergunta_ou_convite(self):
        self.assertTrue(any("pergunta" in x for x in erros(com(fechamento__pergunta="Leia o texto."))))
        self.assertTrue(any("convite" in x for x in erros(com(fechamento__convite="  "))))

    def test_md_editado_a_mao(self):
        md = SB.renderizar(BASE, CFG).replace("Gancho", "gancho editado")
        self.assertTrue(any("storyboard.md" in x for x in erros(BASE, md + "\nlinha a mais")))


if __name__ == "__main__":
    unittest.main()
