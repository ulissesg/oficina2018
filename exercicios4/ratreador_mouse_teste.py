from rastreador_mouse import *
import unittest

class Test(unittest.TestCase):

    def test_trata_mouse(self):
        self.assertEqual(trata_mouse(MOUSE_2, 50, 400, pg.MOUSEMOTION), Mouse(50,400))
        self.assertEqual(trata_mouse(MOUSE_2, 50, 400, pg.MOUSEBUTTONUP), MOUSE_2)
        self.assertEqual(trata_mouse(MOUSE_2, 50, 400, pg.MOUSEBUTTONDOWN), MOUSE_2)


