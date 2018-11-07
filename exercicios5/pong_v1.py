'''

Reaproveitando mais uma vez o exemplo da bolinha:
crie um programa com a bolinha que desliza pela tela
e que contenha também uma plataforma, como se fosse
a raquete do jogo Pong. Essa plataforma nada mais é
do que um retângulo (pode ser na horizontal ou na
vertical). Quando a bola encostar na raquete, ela
deve quicar, assim como faz quando encosta na parede.
A raquete deve ser movimentada simplesmente
ao mover o ponteiro do mouse pela tela
'''

from bolinha import *

''' ping pong  single player'''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

COR_RAQUETE = 'blue'
TAMANHO_RAQUETE_L= 200
TAMANHO_RAQUETE_A= 10

DESENHO_RAQUETE= retangulo(TAMANHO_RAQUETE_L, TAMANHO_RAQUETE_A, Cor(COR_RAQUETE))

METADE_H_RAQUETE = altura_imagem(DESENHO_RAQUETE) // 2
METADE_L_RAQUETE = largura_imagem(DESENHO_RAQUETE) // 2

Raquete = definir_estrutura("Raquete", "x, y")
''' Raquete pode ser formado assim: Raquete(int[0; LARGURA],y[0; ALTURA)
interp. representa uma raquete no jogo.
'''
#EXEMPLOS:
RAQUETE_1 = Raquete(LARGURA//2, ALTURA - 50)
RAQUETE_2 = Raquete(100, ALTURA -20)
RAQUETE_3 = Raquete(300, ALTURA - 20)

#TEMPLATE
'''
def fn_para_raquete(r):
    ... r.x
        r.y
'''

Jogo = definir_estrutura("Jogo", "bola, raquete")
''' Jogo pode ser formado assim: Jogo(Bola, Raquete)
interp. representa o jogo com uma bolinha quicante e uma raquete.
'''
#EXEMPLOS:
JOGO_1 = Jogo(BOLA_1, RAQUETE_1)
JOGO_2 = Jogo(BOLA_2, RAQUETE_2)
JOGO_3 = Jogo(BOLA_3, RAQUETE_3)

#TEMPLATE
'''
def fn_para_jogo(jogo):
    ... jogo.bola
        jogo.raquete
'''
'''
mover_jogo: Jogo -> Jogo
interp. gera o novo estado do jogo
'''

'''===================='''
''' Funções: '''
def colidirem(b, r):
    L_CIMA_RAQUETE = r.y - METADE_H_RAQUETE
    L_BAIXO_RAQUETE = r.y + METADE_H_RAQUETE
    L_DIREITO_RAQUETE = r.x + METADE_L_RAQUETE
    L_ESQUERDO_RAQUETE = r.x - METADE_L_RAQUETE

    LIMITE_BOLA_CIMA = b.y - TAMANHO_BOLA
    LIMITE_BOLA_BAIXO = b.y + TAMANHO_BOLA
    LIMITE_ESQUERDO_BOLA = b.x - TAMANHO_BOLA
    LIMITE_DIREITO_BOLA = b.x + TAMANHO_BOLA

    if (b.x >= L_ESQUERDO_RAQUETE and b.x <= L_DIREITO_RAQUETE) and \
            LIMITE_DIREITO_BOLA >= L_ESQUERDO_RAQUETE and \
            LIMITE_ESQUERDO_BOLA <= L_DIREITO_RAQUETE and \
            LIMITE_BOLA_BAIXO >= L_CIMA_RAQUETE and \
            LIMITE_BOLA_CIMA <= L_BAIXO_RAQUETE:
        return True
    return False

def mover_jogo(jogo):
    if (colidirem(jogo.bola, jogo.raquete)):
        return Jogo(mover_bola(Bola(jogo.bola.x, jogo.bola.y, jogo.bola.dx, -jogo.bola.dy)),jogo.raquete)
    return Jogo(mover_bola(jogo.bola),jogo.raquete)
'''
desenha_raq: Raquete -> Raquete
interp. gera o novo estado na raquete
'''
def desenha_raq(r):
    colocar_imagem(DESENHO_RAQUETE, tela, r.x, r.y)
'''
desenha: Jogo -> Imagem
interp. desenha a bola e a raquete na tela
'''
def desenha(jogo):
    desenha_b(jogo.bola)
    desenha_raq(jogo.raquete)
'''
trata_mouse: Jogo, Int, Int, EventoMouse -> Jogo:
Quando o mouse se movimentar para os lados na posiçao x no mouse produz a nova posicao da raquete
'''
def trata_mouse(jogo, x, y, ev):

    if ev == pg.MOUSEMOTION:
        return Jogo(jogo.bola, Raquete(x, jogo.raquete.y))
    return jogo









# TODO testes colidem trata mouse