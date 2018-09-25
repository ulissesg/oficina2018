from semaforo import *

class Test(unittest.TestCase):

    def test_troca_cor(self):
        self.assertEqual(troca_cor(0), 1)
        self.assertEqual(troca_cor(1), 2)
        self.assertEqual(troca_cor(2), 0)
        self.assertEqual(troca_cor(4), 0)

unittest.main()