"""Teste da avaliação da Fase E.

  python3 -m unittest scripts/test_avaliar.py
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import avaliar as A  # noqa: E402

SITE = "---\ntitulo: x\n---\n\nA gravação aconteceu no meio de uma crise.\n\nA banda trocou de empresário.\n"
POST = "---\ntitulo: x\n---\n\nA gravação aconteceu — no meio de uma crise — e a banda trocou de empresário.\n"


class Comparar(unittest.TestCase):
    def test_post_igual_ao_site_nao_pede_edicao(self):
        r = A.comparar(POST, SITE, SITE)
        self.assertEqual(r["novo"]["similaridade"], 1.0)
        self.assertEqual(r["novo"]["ops_estilo"], 0)
        self.assertGreater(r["antigo"]["ops_estilo"], 0)
        self.assertLess(r["antigo"]["similaridade"], 1.0)


if __name__ == "__main__":
    unittest.main()
