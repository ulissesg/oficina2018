from pong_v2 import *
import unittest

class Test(unittest.TestCase):

    def test_mover_raquete(self):
        self.assertEqual(mover_raquete(RAQ_1), Raquete2(RAQ_1.x + RAQ_1.dx, RAQ_1.y, RAQ_1.dx))
        self.assertEqual(mover_raquete(RAQ_2), Raquete2(RAQ_2.x + RAQ_2.dx, RAQ_2.y, RAQ_2.dx))
        self.assertEqual(mover_raquete(RAQ_3), Raquete2(RAQ_3.x + RAQ_3.dx, RAQ_3.y, RAQ_3.dx))

    def test_contador_pontos(self):
        self.assertEqual(contador_pontos(Jogo(Bola(30,30,1,1), JOGO_4.raquete, JOGO_4.raquete2, JOGO_4.player1, JOGO_4.player2, JOGO_4.game_over)),
                         Jogo(Bola(LARGURA // 2, ALTURA // 2, 1, 1), JOGO_4.raquete, JOGO_4.raquete2, JOGO_4.player1 + AUMENTO_PLACAR, JOGO_4.player2, JOGO_4.game_over))

        self.assertEqual(contador_pontos(Jogo(Bola(30,370,1,1), JOGO_4.raquete, JOGO_4.raquete2, JOGO_4.player1, JOGO_4.player2, JOGO_4.game_over)),
                         Jogo(Bola(LARGURA // 2, ALTURA // 2, 1, 1), JOGO_4.raquete, JOGO_4.raquete2, JOGO_4.player1, JOGO_4.player2 + AUMENTO_PLACAR, JOGO_4.game_over))

        self.assertEqual(contador_pontos(Jogo(BOLA_2, JOGO_4.raquete, JOGO_4.raquete2, JOGO_4.player1, JOGO_4.player2, JOGO_4.game_over)),
                         Jogo(BOLA_2, JOGO_4.raquete, JOGO_4.raquete2, JOGO_4.player1, JOGO_4.player2, JOGO_4.game_over))

    def test_verifica_placar(self):
        self.assertEqual(verifica_placar(JOGO_4), JOGO_4)
        self.assertEqual(verifica_placar(JOGO_2), JOGO_2)

        self.assertEqual(verifica_placar(Jogo(BOLA_1, RAQUETE_3, RAQ_2, PLACAR_MAX, 0, False)),
                         Jogo(BOLA_1, RAQUETE_3, RAQ_2, PLACAR_MAX, 0, True))

        self.assertEqual(verifica_placar(Jogo(BOLA_1, RAQUETE_3, RAQ_2, 0, PLACAR_MAX, False)),
                         Jogo(BOLA_1, RAQUETE_3, RAQ_2, 0, PLACAR_MAX, True))

    def test_mover_jogo_2(self):
        self.assertEquals(mover_jogo_2(JOGO_4),
                          Jogo(mover_bola(JOGO_4.bola), JOGO_4.raquete, mover_raquete(JOGO_4.raquete2), JOGO_4.player1,
                               JOGO_4.player2, JOGO_4.game_over))

        self.assertEquals(mover_jogo_2(JOGO_3), JOGO_3)

    def test_trata_mouse_2(self):
        self.assertEquals(trata_mouse_2(JOGO_4, 200, JOGO_4.raquete.y, pg.MOUSEMOTION),
                          Jogo(JOGO_4.bola, Raquete(200, JOGO_4.raquete.y), JOGO_4.raquete2, JOGO_4.player1, JOGO_4.player2, JOGO_4.game_over))

        self.assertEquals(trata_mouse_2(JOGO_4, 500, JOGO_4.raquete.y, pg.MOUSEMOTION),
                          Jogo(JOGO_4.bola, Raquete(500, JOGO_4.raquete.y), JOGO_4.raquete2, JOGO_4.player1, JOGO_4.player2, JOGO_4.game_over))

        self.assertEquals(trata_mouse_2(JOGO_4, 200, JOGO_4.raquete.y, pg.MOUSEBUTTONDOWN),
                          JOGO_4)

    def test_trata_tecla(self):
        self.assertEquals(trata_tecla(JOGO_2, pg.K_RETURN), JOGO_4)

        self.assertEquals(trata_tecla(JOGO_4, pg.K_LEFT),
                          Jogo(JOGO_4.bola, JOGO_4.raquete, Raquete2(JOGO_4.raquete2.x, JOGO_4.raquete2.y, -DX_RAQUETE2), JOGO_4.player1, JOGO_4.player2, JOGO_4.game_over))

        self.assertEquals(trata_tecla(JOGO_4, pg.K_RIGHT),
                          Jogo(JOGO_4.bola, JOGO_4.raquete, Raquete2(JOGO_4.raquete2.x, JOGO_4.raquete2.y, DX_RAQUETE2), JOGO_4.player1, JOGO_4.player2, JOGO_4.game_over))

        self.assertEquals(trata_tecla(JOGO_2, pg.K_UP), JOGO_2)


    def test_trata_solta_tecla(self):
        self.assertEquals(trata_solta_tecla(JOGO_4, pg.K_LEFT),
                          Jogo(JOGO_4.bola, JOGO_4.raquete, Raquete2(JOGO_4.raquete2.x, JOGO_4.raquete2.y, 0), JOGO_4.player1, JOGO_4.player2, JOGO_4.game_over))

        self.assertEquals(trata_solta_tecla(JOGO_4, pg.K_RIGHT),
                          Jogo(JOGO_4.bola, JOGO_4.raquete, Raquete2(JOGO_4.raquete2.x, JOGO_4.raquete2.y, 0), JOGO_4.player1, JOGO_4.player2, JOGO_4.game_over))

        self.assertEquals(trata_solta_tecla(JOGO_2, pg.K_UP), JOGO_2)