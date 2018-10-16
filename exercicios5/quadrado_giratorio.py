'''

Projete um programa mundo como segue:

O mundo começa com um pequeno quadrado no centro da tela. Enquanto o tempo passa,
o quadrado deve ficar fixo no centro, mas aumentando de tamanho e girando
a uma velocidade constante. O angulo do giro deve ser representado em graus.
Ao pressionar a barra de espaço 'reseta-se' o mundo,
de modo que o quadrado volta a ser pequeno e sem ter girado.

.
OBSERVAÇÃO 1: Lembre-se de seguir a receita Como Projetar Mundos e as demais 
(Como Projetar Dados) e (Como Projetar Funções)! Assegure-se de fazer a análise
de domínio antes de começar a trabalhar no código (entregar em papel essa parte).

OBSERVAÇÃO 2: Use a função 'girar' do módulo image do htdp-pt-br (já incluido ao se importar universe)

DICA 1: Use a operação de resto da divisão (%) para fazer o angulo em graus voltar a 0 quando atingir o 360.

DICA 2: use dados compostos para fazer isso. Pense bem em quais são os dados que mudam
(variáveis) para projetar a definição de dados. Por isso é importante fazer a
análise de domínio.
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' quadrado giratorio '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (600, 400)
tela = criar_tela_base(LARGURA, ALTURA)

X = LARGURA // 2
Y = ALTURA // 2
FREQUENCIA = 30
VELOCIDADE_ANGULO = 5
VELOCIDADE_TAMANHO = 1
COR_QUADRADO = "red"
MSG_ERRO = "ERRO"

'''==================='''
'''# Definições de dados: '''

#Criando tipo composto.
Quadrado = definir_estrutura("Quadrado", "angulo, tamanho")

''' Quadrado eh composto assim: Quadrado(int, int)
    interp. representa um quadrado com os seguntes campos, angulo [0,360] e tamanho(>0).
'''
#exemplos

QUADRADO_INICIAL = Quadrado(1,10)
QUADRADO_2 = Quadrado(180,80)
QUADRADO_FINAL = Quadrado(360, 160)

#template
'''
def fn_para_quadrado(quad):
    if quad.tamanho >= 0 or quad.angulo >= 0:
        if quad.angulo < 360:
        ... quad.angulo
        ... quad.tamanho
        else :
        ... quad.angulo
        ... quad.tamanho
'''

'''===================='''
''' Funções: '''

'''quadrado: Quadrado -> Quadrado
Produz o próximo estado(quadrado)
'''

def fn_quadrado(quad):
    if quad.tamanho >= 0 and quad.angulo >= 0:
        if quad.angulo < 360:
            quad = Quadrado((quad.angulo) + VELOCIDADE_ANGULO, ((quad.tamanho) + VELOCIDADE_TAMANHO))
        else:
            quad = Quadrado((QUADRADO_INICIAL.angulo), ((quad.tamanho) + VELOCIDADE_TAMANHO))
        return quad
    else:
        return MSG_ERRO
'''
desenha: Quadrado -> Imagem
Desenha um quadrado com o tamanho e angulo definidos na tela
'''
def desenha_q(quad):
    quadra = quadrado(quad.tamanho, Cor(COR_QUADRADO))
    quadra = girar(quadra, quad.angulo)
    colocar_imagem(quadra,tela, X, Y)

'''
trata_tecla: Quadrado, Tecla -> Quadrado
Quando teclar space volta ao estado inicial
'''
def trata_tecla(quad, tecla):
    if tecla == pg.K_SPACE:
        return QUADRADO_INICIAL
    else:
        return quad
