from pong_v1 import *
import unittest

class Test(unittest.TestCase):

    def test_colidirem(self):
        self.assertEqual(colidirem(Bola(300,200,1,1), Raquete(310, 200)), True)
        self.assertEqual(colidirem(Bola(400,300,1,1), Raquete(410, 300)), True)
        self.assertEqual(colidirem(Bola(100,200,1,1), Raquete(300, 200)), False)

    def test_trata_mouse(self):
        self.assertEqual(trata_mouse(JOGO_1, 400, 200, pg.MOUSEMOTION), Jogo(JOGO_1.bola, Raquete(400,JOGO_1.raquete.y)))
        self.assertEqual(trata_mouse(JOGO_3, 100, 200, pg.MOUSEMOTION), Jogo(JOGO_3.bola, Raquete(100,JOGO_3.raquete.y)))