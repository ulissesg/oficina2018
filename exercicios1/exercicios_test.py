from exercicios1 import *

class Test(unittest.TestCase):

    def test_maior_de_2(self):

        self.assertEqual(maior_de_2(4,3), 4)
        self.assertEqual(maior_de_2(6,7), 7)

    def test_maior_de_3(self):

        self.assertEqual(maior_de_3(4,3,2), 25)
        self.assertEqual(maior_de_3(5,6,7), 85)
        self.assertEqual(maior_de_3(12,3,10), 244)
        self.assertEqual(maior_de_3(10,3,10), 200)


    def test_soma_quadrado(self):

        self.assertEqual(soma_quadrado(4,3), 25)
        self.assertEqual(soma_quadrado(6,7), 85)

    def test_distancia_origem(self):

        self.assertEqual(distancia_origem(4,3), 5)
        self.assertEqual(distancia_origem(6,0), 6)

    def test_classifica_triangulo(self):
        self.assertEqual(classifica_triangulo(6,6,6), "equilatero")
        self.assertEqual(classifica_triangulo(2,3,4), "escaleno")
        self.assertEqual(classifica_triangulo(2,3,3), "isoceles")
        self.assertEqual(classifica_triangulo(3,2,3), "isoceles")
        self.assertEqual(classifica_triangulo(3,3,2), "isoceles")


    def test_calculo_imc(self):
        self.assertEqual(calculo_imc(50, 1.78), "Abaixo do peso")
        self.assertEqual(calculo_imc(70, 1.78), "Peso normal")
        self.assertEqual(calculo_imc(80, 1.78), "Sobrepeso")
        self.assertEqual(calculo_imc(80, 1.60), "Obesidade")
        self.assertEqual(calculo_imc(90, 1.60), "Obesidade Moderada")
        self.assertEqual(calculo_imc(120, 1.60), "Obesidade Severa")
        self.assertEqual(calculo_imc(200, 1.98), "Obesidade Morbida")

    def test_fahrenheit_para_celsius(self):

        self.assertEqual(fahrenheit_para_celsius(86), 30)
        self.assertEqual(fahrenheit_para_celsius(59), 15)

    def test_juros_poupanca(self):

        self.assertEqual(juros_poupanca(800), 832)
        self.assertEqual(juros_poupanca(4800), 5016)
        self.assertEqual(juros_poupanca(5600), 5880)

    def test_polegadas_para_cm(self):

        self.assertEqual(polegadas_para_cm(5), 12.7)
        self.assertEqual(polegadas_para_cm(32), 81.28)

    def test_pes_para_polegadas(self):

        self.assertEqual(pes_para_polegadas(2), 24)
        self.assertEqual(pes_para_polegadas(6), 72)

    def test_jardas_para_pes(self):

        self.assertEqual(jardas_para_pes(2), 6)
        self.assertEqual(jardas_para_pes(9), 27)

    def test_varas_para_jardas(self):

        self.assertEqual(varas_para_jardas(4), 22)
        self.assertEqual(varas_para_jardas(3), 16.5)

    def test_furlongs_para_varas(self):

        self.assertEqual(furlongs_para_varas(4), 160)
        self.assertEqual(furlongs_para_varas(20), 800)

    def test_milhas_para_furlongs(self):

        self.assertEqual(milhas_para_furlongs(4), 32)
        self.assertEqual(milhas_para_furlongs(20), 160)

    def test_pes_para_cm(self):

        self.assertEqual(pes_para_cm(1), 30.48)
        self.assertEqual(pes_para_cm(20), 609.6)

    def test_jardas_para_cm(self):

        self.assertEqual(jardas_para_cm(1), 91.44)
        self.assertEqual(jardas_para_cm(6), 548.64)

    def test_varas_para_polegadas(self):

        self.assertEqual(varas_para_polegadas(3), 594)
        self.assertEqual(varas_para_polegadas(100), 19800)

    def test_varas_para_polegadas(self):

        self.assertEqual(varas_para_polegadas(3), 594)
        self.assertEqual(varas_para_polegadas(100), 19800)

    def test_milhas_para_pes(self):

        self.assertEqual(milhas_para_pes(5), 26400)
        self.assertEqual(milhas_para_pes(50), 264000)

unittest.main()  #não excluir (a menos que esteja rodando como unit test no PyCharm)
