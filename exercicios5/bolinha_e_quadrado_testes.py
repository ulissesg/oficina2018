from bolinha_e_quadrado import *
import unittest

class Test(unittest.TestCase):

    def test_trata_tecla(self):
        self.assertEqual(trata_tecla(QUADRADO_2, pg.K_SPACE), QUADRADO_INICIAL)
        self.assertEqual(trata_tecla(QUADRADO_2, pg.K_l), QUADRADO_2)

