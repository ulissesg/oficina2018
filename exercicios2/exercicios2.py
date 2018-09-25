#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from htdp_pt_br.universe import *

'''EXERCÍCIOS:
O uso das receitas de projeto é obrigatório!! Os testes devem estar na classe Test no final
do arquivo.
'''
### ERROS CONCERTADOS.
'''CONSTANTES'''

MSG_ERRO_INVALIDO = "Erro: dado invalido"

'''
-- Definição de dados:
Idade é um Natural
interp. a idade de uma pessoa em anos
Ex:
'''
I_FULANO = 18
I_BELTRANO = 25


'''
1.

PROBLEMA 1A: Considere a definição acima.

Projete uma função chamada 'eh_adolescente' que determina se uma pessoa
de uma idade específica é um adolescente (i.e., entre a idade 13 a 19)
(dica: se eh adolescente, retorne true, senão, retorne false
'''
'''
-- Definição de dados:
Idade é um Natural
interp. a idade de uma pessoa em anos
Ex:
'''
I_FULANO = 18
I_BELTRANO = 25

'''
#template 
def eh_adolescente(i):
    if i < 0:
        return MSG_ERRO_INVALIDO
    else 
        ...i
        
'''
''' INICIO FUNÇÂO'''

'''
Idade -> Boolean   ##PROF: Boolean
verifica se a pessoa e um adolescente
'''

def eh_adolescente(i):
    if i < 0:
        return MSG_ERRO_INVALIDO
    else:
        if ((i > 12) and (i < 20)):
            return True
        else:
            return False

# 10

'''
-------------//------------
2.

PROBLEMA 2A:

Você está projetando um programa para rastrear a viagem de um foguete
enquanto ele desce a 100 km de distância da Terra. Você está interessado
apenas na descida a partir de 100 km até o chão.

Projete uma definição de dados para representar a distância do foguete.
Chame de DistanciaDescidaFoguete.

'''
'''Definicao de dados'''

'''
DistanciaDescidaFoguete é um float [0, 100] ##PROF: NÃO É QUALQUER NUMERO. RELEIA O ENUNCIADO. TERÁ QUE USAR UM INTERVALO.
interp. descreve distancia do foguete ate o chao em km
Ex:
'''
DIST_MAX= 100
DIST_MED= DIST_MAX // 2
CHAO = 0

'''
#template
def distancia_do_chao(dist):
    if dist >= 0 and dist <= 100:
        ...dist
    else:
        ...
'''
## PROF: COMO O DADO É UM INTERVALO, PODERIA TER INCLUIDO LOGICA DE VALIDAÇÃO NO TEMPLATE
# 8

'''
PROBLEMA 2B:

Projete uma função que imprima a distância que falta para o foguete chegar
na terra por meio de uma curta string que possa ser publicada no Twitter.
Por exemplo: "Altitude atual: 80 km da superfície".
Quando a descida acabar, a mensagem deve aparecer "O foguete pousou!".
Dê o seguinte nome para a função: 'distancia-foguete-para-msg'.

'''
'''
distancia_foguete_para_msg: DistanciaDescidaFoguete -> string
retorna a mensagem de acordo com a distancia do foguete ate o chao
'''
def distancia_foguete_para_msg (dist):
    if (dist > 0) and (dist < 100):
        return "Altitude atual: "+str(dist)+" km da superfície"
    elif(dist > 100):
        return "Altitude atual: >= 100 km da superfície"
    elif(dist == 0):
        return "O foguete pousou!"
    return MSG_ERRO_INVALIDO

# 10

'''
------------//------------
3.

PROBLEMA 3A:

Você precisa desenvolver um sistema para classificar edifícios no centro
de Curitiba, com base no quão velhos são.
De acordo com as leis da cidade, há três diferentes níveis de classificação:
novo, velho e patrimônio.

Projete uma definição de dado para representar esses níveis de classificação.
Chame de CondicaoEdificio.

'''
'''
CondicaoEdificio e uma string podendo ser: "novo", "velho", "patrimonio".  ##PROF: MAS NÃO É QUALQUER STRING. POR ISSO TEM QUE SER DEFINIDO COMO UMA ENUMERAÇÃO. VEJA EXEMPLO DO SEMAFORO
interp. define a condição do edificio
Ex: 
'''
COND_EDIF1 = "novo"
COND_EDIF2 = "velho"
COND_EDIF3 = "patrimonio"

'''
#template 
def calssifica_edificio(s):
    if s == "novo":
        ... 
    if  s == "patrimonio":
        ...
    if s == "velho":
        ...
'''
##PROF: O TEMPLATE DEVERIA SER DE ACORDO COM UMA ENUMERAÇÃO. 

# 5

'''
PROBLEMA 3B:

A cidade precisa demolir todos os edifícios classificados como "velho".
Você foi contratado para projetar uma função chamada 'demolir', que
determina se o edifício deve ser demolido ou não. (dica: "demolir"=True,
"não demolir"=False)

'''
'''
demolir: CondicaoEdificio -> Boolean
'''
'''classifica se o predio sera demolido ou nao.'''
def demolir(s):
    if s == "novo" or s== "patrimonio":
        return False
    if s == "velho":
        return True

    return MSG_ERRO_INVALIDO

# 10

'''
-------------------//--------------
4.

PROBLEMA 4:

Considere um jogo onde você precisa representar a quantidade de vidas de
seu personagem.
A única coisa que importa sobre essas vidas é:

    - se o personagem está morto (sem vida, game over)
    - se o personagem está vivo então pode ter 0 ou mais vidas extras.

Projete uma definição de dados chamada Vidas para representar quantas
vidas tem seu personagem.

Projete uma função chamada 'ganhar-vida' que permite aumentar as vidas
de um personagem. A função deve apenas aumentar a vida de um
persongagem se ele não estiver morto, caso contrário o personagem
continua morto.

'''
'''
Vidas pode ser um dos tipos:##PROF: SE É APENAS UM BOOLEAN, NÃO TEM COMO REPRESENTAR A QUANTIDADE DE VIDAS. VEJA O EXEMPLO DO PASSARO NOS SLIDES, É PARECIDO.
   False
   int positivo (>=0)
interp. False significa que o personagem esta morto
se for >= 0 significa que o personagem esta vivo e tem uma quantidade x de vidas.
Ex.
'''
VIDAS_PERSONAGEM1 = False
VIDAS_PERSONAGEM2 = 4

'''
#template
def ganhar_vida(v):
    elif type(v) is int:
        ... v
    if not v:
        ...
    
'''

# 2

'''
ganhar_vida: Vidas -> False ou Int
'''
''' se o personagem estiver vivo(v>=0) aumenta 1 nas vidas, senao retorna a propria variavel(False).'''
def ganhar_vida(v):
    if type(v) is int: ##PROF: DÁ PARA FAZER SIMPLESMENTE: if v:
        return v+1
    if not v:
        return v
## PROF: O EXERCICIO TODO FICOU ERRADO EM DECORRÊNCIA DE NÃO TER PRESTADO ATENÇÃO NO ENUNCIADO. REFAÇA.

# 0


'''
---------------------//--------------
5.

PROBLEMA 5A:

Projete uma definição de dados para representar um filme, incluindo  
título, custo de produção, e ano que foi lançado.

Para ajudar a criar alguns exemplos, abaixo temos alguns fatos sobre alguns filmes: 
"Titanic" - custo: 200000000 lancamento: 1997
"Avatar" - custo: 237000000 lancamento: 2009
"The Avengers" - custo: 220000000 lancamento: 2012

No entanto, sinta-se livre para pesquisar.
DICA: terá que usar namedtuple ou class para criar um tipo composto (veja arquivo de exemplos)
'''

#Criando tipo composto.
Filme = definir_estrutura("Filme", "titulo, custo, lancamento")

'''Filme e formado assim: Filme(String, Int, Int)
interp. Filme representa um filme com os campos titulo, custo de producao e ano de lancamento.
'''
#exemplos

FILME1 = Filme("Titanic", 200000000, 1997)
FILME2 = Filme("Avatar", 237000000, 2009)
FILME3 = Filme("The Avengers", 220000000, 2012)

'''
#template
def fn_para_filme(f):
    ... f.titulo
        f.custo
        f.lancamento
'''

# 10

'''
PROBLEMA 5B:

Projete uma função que RECEBE DOIS filmes e retorne
o título do filme lançado mais recentemente.
'''

'''
mais_recente: Filme, Filme -> Filme.titulo   ##PROF: O ENUNCIADO DIZ QUE DEVERIA RETORNAR O TITULO (UMA String)
retorna o filme mais recente.
'''

def mais_recente(f1, f2):
    if (f1.lancamento > f2.lancamento):
        return f1.titulo
    return f2.titulo

# 9

