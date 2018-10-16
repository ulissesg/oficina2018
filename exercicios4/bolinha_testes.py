from bolinha import *
import unittest

class Test(unittest.TestCase):

    def test_mover_bola(self):
        self.assertEqual(mover_bola(BOLA_1), Bola(52,53,2,3))
        self.assertEqual(mover_bola(BOLA_2), Bola(302,203,2,3))

        self.assertEqual(mover_bola(Bola(500, LIMITE_BAIXO, 2, 3)), Bola(502,LIMITE_BAIXO -3 ,2,-3))
        self.assertEqual(mover_bola(Bola(LIMITE_DIREITO, 300, 2, 3)), Bola(LIMITE_DIREITO -2 ,303 , -2, 3))

        self.assertEqual(mover_bola(Bola(LIMITE_DIREITO, LIMITE_BAIXO, 2, 3)), Bola(LIMITE_DIREITO -2 ,LIMITE_BAIXO - 3,-2,-3))

        self.assertEqual(mover_bola(Bola(500, LIMITE_BAIXO + 1, 2, 3)), Bola(502,LIMITE_BAIXO -2, 2, -3))

        self.assertEqual(mover_bola(Bola(LIMITE_DIREITO + 1, LIMITE_BAIXO +1 , 2, 3)), Bola(LIMITE_DIREITO -1, LIMITE_BAIXO -2 , -2, -3))

