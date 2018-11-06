

class Test(unittest.TestCase):

    def test_mover(self):
        self.assertEqual(mover(3), 4)
        self.assertEqual(mover(ALTURA), ALTURA -(ALTURA_FOGUETE // 4))
        self.assertEqual(mover(ALTURA + 5), ALTURA -(ALTURA_FOGUETE // 4))

unittest.main()