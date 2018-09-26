from exercicios2 import *

class Test(unittest.TestCase):

    def test_eh_adolescente(self):
        self.assertEqual(eh_adolescente(15), True)
        self.assertEqual(eh_adolescente(20), False)
        self.assertEqual(eh_adolescente(35), False)
        self.assertEqual(eh_adolescente(5), False)
        self.assertEqual(eh_adolescente(0), False)
        self.assertEqual(eh_adolescente(-5), MSG_ERRO_INVALIDO)

    def test_distancia_foguete_para_msg(self):
        self.assertEqual(distancia_foguete_para_msg(50), "Altitude atual: 50 km da superfície")
        self.assertEqual(distancia_foguete_para_msg(110), "Altitude atual: >= 100 km da superfície")
        self.assertEqual(distancia_foguete_para_msg(0), "O foguete pousou!")
        self.assertEqual(distancia_foguete_para_msg(-5), MSG_ERRO_INVALIDO)

    def test_demolir(self):
        self.assertEqual(demolir("novo"), False)
        self.assertEqual(demolir("velho"), True)
        self.assertEqual(demolir("patrimonio"), False)
        self.assertEqual(demolir("caindo aos pedaços"), MSG_ERRO_INVALIDO)

    def test_ganhar_vida(self):
        self.assertEqual(ganhar_vida(False), False)
        self.assertEqual(ganhar_vida(0), 1)
        self.assertEqual(ganhar_vida(1), 2)
        self.assertEqual(ganhar_vida(2), 3)

    def test_mais_recente(self):
        self.assertEqual(mais_recente(FILME1, FILME2), FILME2.titulo)
        self.assertEqual(mais_recente(FILME2, FILME1), FILME2.titulo)
        self.assertEqual(mais_recente(FILME3, FILME2), FILME3.titulo)

unittest.main()  #excluir no pycharm



