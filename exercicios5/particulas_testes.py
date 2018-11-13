from particulas import *
import unittest

class Test(unittest.TestCase):

    def test_colidem(self):
        self.assertEqual(colidem(Bola(300,200,1,1), Bola(305, 205,1,1)), True)
        self.assertEqual(colidem(Bola(400,300,1,1), Bola(405, 305,1,1)), True)
        self.assertEqual(colidem(Bola(300,200,1,1), Bola(100, 200,1,1)), False)
