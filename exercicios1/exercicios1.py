#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
'''Importe outras bibliotecas abaixo'''


''' EXERCÍCIOS
Obrigatorio UTILIZAR RECEITA DE PROJETO!!!
Todos os testes devem ser feitos dentro da classe Tests no final do arquivo.
Faca os testes antes do codigo, conforme a receita de projeto e a tecnica TDD.

(ATENÇÃO: Nao apague os comentarios entre aspas triplas, apenas os
comentarios na frente de #).
'''

'''
1. Defina uma funcao que encontre o maior valor entre 2 valores dados
'''
'''
maior: int int -> int
'''
'''retorna o maior numero'''
def maior_de_2(n1, n2):
    if (n1 > n2):
        return n1
    if (n2 > n1):
        return n2


'''
2. Defina uma funcao que receba 3 numeros como parametros
e retorne a soma dos quadrados dos dois maiores numeros.
'''

'''
maior: int int int -> int int
'''
'''retorna o quadrado dos dois maiores numeros dos tres numeros passados como parametro'''
def maior_de_3(n1, n2, n3): # como passar vetor como parametro
    if ((n1 > n2) and (n2 > n3)):
        return soma_quadrado(n1,n2)

    if ((n2 > n1) and (n3 > n2)):
        return soma_quadrado(n2,n3)

    if ((n1 > n2) and (n3 > n2)):
        return soma_quadrado(n1,n3)

'''
soma_quadrado: int int -> int
'''
''''faz o calculo do quadrado dos dois numeros'''
def soma_quadrado(b,b2):
    return ((b*b)+(b2*b2))

'''
3. Defina uma funcao que calcule a distancia de um ponto no plano cartesiano (representado por dois
numeros) a origem.
'''

'''
 distancia_origem: float float ->  float
'''

'''
formula = d²=(xa-ya)²+(xb-yb)²
'''
'''calcula a distancia de um um ponto ate sua origem (0,0)'''
import math

def distancia_origem (a,b):
    return math.sqrt(math.pow((a), 2) + math.pow((b),2))

'''
4. Defina uma funcao que receba como parametro 3 numeros que representam
os lados de um triangulo e classifique o triangulo como equilatero,
isosceles ou escaleno. Veja a pagina sobre triangulos na Wikipedia.
'''

'''
classifica_triangulo: float float float -> string
'''
'''
classifica os triangulos
'''

def classifica_triangulo(a, b, c):
    if (((a != b) and (b == c)) or ((b != c) and (c == a)) or ((c != b) and (b == a))):
        return "isoceles"
    if ((a == b ) and (b == c) and (c == a)):
        return "equilatero"
    if ((a != b ) and (b != c) and (c != a)):
        return "escaleno"

'''
5. Defina uma funcao que classifique o grau de obesidade de uma
pessoa usando o IMC.
'''

'''
formula = peso / altura * altura
'''

'''
calculo_imc: float float ->  string
'''
''' calcula o imc'''
def calculo_imc(peso, altura):
    imc = (peso /(altura * altura))
    return classifica_imc(imc)

'''
classifica_imc: float -> string
'''
'''classifica o imc'''
def classifica_imc(x):
    if (x < 18.5):
        return "Abaixo do peso"
    if ((x >= 18.6) and (x <= 24.9)):
        return "Peso normal"
    if ((x >= 25.0) and (x <= 29.9)):
        return "Sobrepeso"
    if ((x >= 30.0) and (x <= 34.9)):
        return "Obesidade"
    if ((x >= 35.0) and (x <= 39.9)):
        return "Obesidade Moderada"
    if ((x >= 40.0) and (x <= 49.9)):
        return "Obesidade Severa"
    if (x > 50):
        return "Obesidade Morbida"


'''
6. Desenvolva uma funcao 'juros_poupanca' que consome uma quantia depositada
de dinheiro, e produz a quantia de juros recebida em um ano. O banco
paga 4% para depositos de até R$1000, 4,5% para depositos de até
R$5000 e 5% para depositos acima de R$5000.
'''

'''
juros_poupanca: float -> float
'''
'''devolve o valor de entrada corrigido com o juros'''

def juros_poupanca(deposito):
    if (deposito > 5000):
        return (deposito + (deposito * 0.05))

    if (deposito > 1000):
        return (deposito + (deposito * 0.045))

    return (deposito + (deposito * 0.04))

'''
7. Defina uma funcao chamada fahrenheit_para_celsius que consome uma temperatura
medida em Fahrenheit e produz a equivalente em Celsius. Pesquise a formula
na internet ou em um livro.
'''
'''
fahrenheit_para_celsius: float -> float
'''
'''transforma a temperatura de fahrenheit para celsius'''

def fahrenheit_para_celsius(f):
    return ((f-32)/1.8)

'''
8. Os Estados Unidos e a Grã-Bretanha utilizam o sistema de medidas inglês. 
O resto do mundo usa o sistema metrico. Pessoas que viajam bastante,
principalmente a negócios, frequentemente precisam fazer a conversão
entre esses sistemas de medidas. A tabela abaixo mostra as seis principais
unidades de medida do sistema ingles:
             ingles            	metrico
           1 polegada      =       2.54 cm
           1 pé = 12 polegadas
           1 jarda = 3 pés
           1 vara = 5(1/2)	jardas
           1 furlong = 40 varas
           1 milha = 8 furlongs 
 Desenvolva as funcoes polegadas_para_cm, pes_para_polegadas, jardas_para_pes,
 varas_para_jardas, furlongs_para_varas e milhas_para_furlongs.
 Então, com base nas anteriores, desenvolva as funcoes pes_para_cm, jardas_para_cm, varas_para_polegadas,
 e milhas_para_pes
 DICA: Reuse as funcoes o maximo possivel. Use constantes.
'''

'''
polegadas_para_cm: float -> float
'''
'''converte a medida de polegadas para centimetros'''

def polegadas_para_cm(x):
    return (x * 2.54)

'''
pes_para_polegadas: float -> float
'''
'''converte a medida de pes para polegadas'''

def pes_para_polegadas(x):
    return (x *12)

'''
jardas_para_pes: float -> float
'''
''' converte a medida de jardas para float'''

def jardas_para_pes(x):
    return (x*3)

'''
varas_para_jardas: float -> float
'''
''' converte a medida de varas para jardas'''

def varas_para_jardas (x):
    return (x * 5.5)

'''
furlongs_para_varas: float -> float
'''
'''converte a medida de furlongs para varas'''

def furlongs_para_varas(x):
    return (x * 40)

'''
milhas_para_furlongs: float -> float
'''
'''converte a medida de milhas para furlongs'''

def milhas_para_furlongs(x):
    return(x*8)

'''
pes_para_cm: float -> float
'''
'''converte a medida de pes para centimetros'''

def pes_para_cm(x):
    return polegadas_para_cm(pes_para_polegadas(x))

'''
jardas_para_cm: float -> float
'''
'''converte a medida de jardas para centimetros'''

def jardas_para_cm(x):
    return polegadas_para_cm(pes_para_polegadas(jardas_para_pes(x)))
    ##PROFESSOR: Acho que é invertido: primeiro transforma jardas para pés, gerando o resultado em pés; depois os pés para polegadas, gerando o resultado em polegadas; e por fim polegadas para cm.
    ### Portanto, a fórmula correta ficaria: polegadas_para_cm(pes_para_polegadas(jardas_para_pes(x)))

    ##################
    ### CORRIGIDO.
    ##################
	
'''
varas_para_polegadas: float -> float
'''
'''converte a medida de varas para polegadas'''

def varas_para_polegadas(x):
    return varas_para_jardas (jardas_para_pes(pes_para_polegadas(x)))

'''
milhas_para_pes: float -> float
'''
'''converte a medida de milhas para pes'''

def milhas_para_pes(x):
    return milhas_para_furlongs(furlongs_para_varas(varas_para_jardas (jardas_para_pes(x))))


