'''

Projete um programa mundo que consiste em uma bolinha (ou partícula) que se move em velocidade constante
pela tela. A bola deve poder se mover tanto no eixo x quanto no eixo y. Quando a bola atinge
os limites (beiradas) da tela, ela deve "quicar", isto é, não deve sair fora da tela e deve continuar
se movendo na direção correta (imagine o que acontece com uma bola que quica no chão diagonalmente).

DICA1: Inspire-se no exemplo da vaca. No entanto, lembre-se que aqui o eixo y (assim como o deslocamento
no eixo y) deve ser considerado.

DICA2: A direção (dx e dy) da bolinha deve ser definifa no estado inicial passado à função main.

DICA3: Veja como funciona o jogo Arkanoid para entender a dinâmica da bola na tela: https://www.youtube.com/watch?v=Th-Z6QQ5AOQ

DICA3: Trabalhem cuidadosamente na análise de domínio e nos exemplos. Este exercicio não é tão 
simples como pode parecer.
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Meu programa da bolinha quicante'''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (600, 400)
tela = criar_tela_base(LARGURA, ALTURA)

FREQUENCIA = 40
TAMANHO_BOLA = 30
COR_BOLA = "black"

IMG_BOLA = circulo(TAMANHO_BOLA, Cor(COR_BOLA))

LIMITE_CIMA = altura_imagem(IMG_BOLA) // 2
LIMITE_BAIXO = ALTURA - altura_imagem(IMG_BOLA) // 1.5
LIMITE_ESQUERDO = altura_imagem(IMG_BOLA) // 1.5
LIMITE_DIREITO = LARGURA - altura_imagem(IMG_BOLA) // 1.5


'''==================='''
'''# Definições de dados: '''

#Criando tipo composto.
Bola = definir_estrutura("Bola", "x, y, dx, dy")

''' Bola pode ser formado por: Bola(int, int, int, int)
interp. Bola ]e formada pelos seguintes campos (x[LIMITE_ESQUERDO, LIMITE_DIREITO], y[LIMITE_CIMA, LIMITE_BAIXO], dx, dy) 
'''
#EXEMPLOS
BOLA_1 = Bola(50,50,2,3)
BOLA_2 = Bola(300,200,2,3)
BOLA_3 = Bola(500,400,2,-3)
BOLA_4 = Bola(600,300,-2,-3)

#template
'''
def fn_para_bola(b):
    if b.y >= LIMITE_BAIXO and b.x >= LIMITE_DIREITO:
        ...b.x
        ...b.dx
        
    elif b.y <= LIMITE_CIMA and b.x <= LIMITE_ESQUERDO:
        ...b.x
        ...b.dx
        
    elif b.y <= LIMITE_CIMA or b.y >= LIMITE_BAIXO:
        ...b.y
        ...b.dy
        
    elif b.x <= LIMITE_ESQUERDO or b.x >= LIMITE_DIREITO:
        ...b.y
        ...b.dy
    #Else
    ...b.y
    ...b.dy
        
'''

'''===================='''
''' Funções: '''


'''
mover_bola: Bola -> Bola
Produz o próximo estado (Bola)'''

def mover_bola(b):

    if b.y >= LIMITE_BAIXO and b.x >= LIMITE_DIREITO:
        b = Bola(b.x, b.y, -b.dx, -b.dy)
        b = Bola(b.x + b.dx, b.y + b.dy, b.dx, b.dy)
        return b

    elif b.y <= LIMITE_CIMA and b.x <= LIMITE_ESQUERDO:
        b = Bola(b.x, b.y, -b.dx, -b.dy)
        b = Bola(b.x + b.dx, b.y + b.dy, b.dx, b.dy)
        return b

    elif b.y <= LIMITE_CIMA or b.y >= LIMITE_BAIXO:
        b = Bola(b.x, b.y, b.dx, -b.dy)
        b = Bola(b.x + b.dx, b.y + b.dy, b.dx, b.dy)
        return b

    elif b.x <= LIMITE_ESQUERDO or b.x >= LIMITE_DIREITO:
        b = Bola(b.x, b.y, -b.dx, b.dy)
        b = Bola(b.x + b.dx, b.y + b.dy, b.dx, b.dy)
        return b

    b = Bola(b.x + b.dx, b.y + b.dy, b.dx, b.dy)
    return b
'''
desenha: Bola -> Imagem
Desenha a imagem da bola na tela
'''

def desenha_b(b):
    colocar_imagem(IMG_BOLA,tela, b.x, b.y)

