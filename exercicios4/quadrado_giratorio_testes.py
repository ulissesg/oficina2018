from quadrado_giratorio import *
import unittest

class Test(unittest.TestCase):

    def test_fn_quadrado(self):
        self.assertEqual(fn_quadrado(QUADRADO_INICIAL), \
                         ((QUADRADO_INICIAL.angulo + VELOCIDADE_ANGULO),(QUADRADO_INICIAL.tamanho + VELOCIDADE_TAMANHO)))
        self.assertEqual(fn_quadrado(QUADRADO_2), \
                         ((QUADRADO_2.angulo + VELOCIDADE_ANGULO),(QUADRADO_2.tamanho + VELOCIDADE_TAMANHO)))
        self.assertEqual(fn_quadrado(QUADRADO_FINAL), (QUADRADO_INICIAL.angulo, QUADRADO_FINAL.tamanho + VELOCIDADE_TAMANHO))
        self.assertEqual(fn_quadrado(Quadrado(0, -1)), MSG_ERRO)
        self.assertEqual(fn_quadrado(Quadrado(-1, 0)), MSG_ERRO)

    def test_trata_tecla(self):
        self.assertEqual(trata_tecla(QUADRADO_2, pg.K_SPACE), QUADRADO_INICIAL)
        self.assertEqual(trata_tecla(QUADRADO_2, pg.K_l), QUADRADO_2)

unittest.main()