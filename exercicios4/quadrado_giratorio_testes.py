from quadrado_giratorio import *
import unittest

class Test(unittest.TestCase):

    def test_quadrado(self):
        self.assertEqual(quadrado(QUADRADO_INICIAL), \
                         ((QUADRADO_INICIAL.angulo + VELOCIDADE_ANGULO),(QUADRADO_INICIAL.tamanho + VELOCIDADE_TAMANHO)))
        self.assertEqual(quadrado(QUADRADO_2), \
                         ((QUADRADO_2.angulo + VELOCIDADE_ANGULO),(QUADRADO_2.tamanho + VELOCIDADE_TAMANHO)))
        self.assertEqual(quadrado(QUADRADO_FINAL), (QUADRADO_INICIAL.angulo, QUADRADO_FINAL.tamanho + VELOCIDADE_TAMANHO))


unittest.main()