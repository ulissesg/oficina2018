'''

Incremente o exercicio pong_v1 acrescentando
mais uma raquete, que seria o Player 2. No caso,
a segunda raquete deve ser controlada pelo teclado.
Implemente também a parte do jogo em que um jogador
ganha ou perde, isto é, se encostar na parede do fundo,
dá ponto para o adversário, e faz a bola retornar
para o centro do "campo".

EXTRA: faça a contagem de pontos de cada
adversário

EXTRA: faça com que somente conte pontos para o adversá-
rio quando encosta em uma área limitada do fundo (tipo
um golzinho).

'''

'''Ping Pong multiplayer'''

from pong_v1 import *

DX_RAQUETE2 = 10

'''Definicao de dados'''
Raquete2 = definir_estrutura("Raquete2", "x, y, dx")
'''
Raquete pode ser formado por: Raquete2(Int[LARGURA, ALTURA], Int[LARGURA, ALTURA], Int)
interp. representa uma raquete no jogo
'''
# Exemplos:
RAQ_1=Raquete2(LARGURA//2,50,0)
RAQ_2=Raquete2(300,200,0)
RAQ_3=Raquete2(500,300,0)


Jogo = definir_estrutura("Jogo", "bola, raquete, raquete2")
''' Jogo pode ser formado assim: Jogo(Bola, Raquete, Raquete2)
interp. representa o jogo com uma bolinha quicante e dois raquete.
'''
#EXEMPLOS:
JOGO_4 = Jogo(BOLA_1, RAQUETE_1, RAQ_1)
JOGO_2 = Jogo(BOLA_2, RAQUETE_2, RAQ_2)
JOGO_3 = Jogo(BOLA_3, RAQUETE_3, RAQ_3)

#TEMPLATE
'''
def fn_para_jogo(jogo):
    ... jogo.bola
        jogo.raquete
        jogo.raquete2
'''

'''Funcoes'''

'''
mover_raquete: Raquete2 -> Raquete2
interp. retorna o novo estado da raquete
'''
def mover_raquete(raq):
    return Raquete2(raq.x + raq.dx, raq.y, raq.dx)

'''
mover_jogo_2: Jogo -> Jogo
interp. retorna o novo estado do jogo
'''
def mover_jogo_2(jogo):
    if (colidirem(jogo.bola, jogo.raquete)):
        return Jogo(mover_bola(Bola(jogo.bola.x, jogo.bola.y, jogo.bola.dx, -jogo.bola.dy)),jogo.raquete, mover_raquete(jogo.raquete2))

    if (colidirem(jogo.bola, jogo.raquete2)):
        return Jogo(mover_bola(Bola(jogo.bola.x, jogo.bola.y, jogo.bola.dx, -jogo.bola.dy)),jogo.raquete, mover_raquete(jogo.raquete2))

    return Jogo(mover_bola(jogo.bola), jogo.raquete, mover_raquete(jogo.raquete2))

'''
trata_mouse_2: Jogo, Int, Int, EventoMouse -> Jogo:
Quando o mouse se movimentar para os lados na posiçao x no mouse produz a nova posicao da raquete
'''
def trata_mouse_2(jogo, x, y, ev):
    if ev == pg.MOUSEMOTION:
        return Jogo(jogo.bola, Raquete(x, jogo.raquete.y), jogo.raquete2)
    return jogo

def trata_tecla(jogo, tecla):
    if tecla == pg.K_LEFT:
        return Jogo(jogo.bola, jogo.raquete, Raquete2(jogo.raquete2.x, jogo.raquete2.y, -DX_RAQUETE2))
    elif tecla == pg.K_RIGHT:
        return Jogo(jogo.bola, jogo.raquete, Raquete2(jogo.raquete2.x, jogo.raquete2.y, DX_RAQUETE2))
    return jogo

'''
trata_solta_tecla : Jogo Tecla -> Jogo
'''
def trata_solta_tecla(jogo, tecla):
    if tecla == pg.K_LEFT or tecla == pg.K_RIGHT:
        return Jogo(jogo.bola, jogo.raquete, Raquete2(jogo.raquete2.x, jogo.raquete2.y, 0))
    return jogo


def desenha_2(jogo):
    desenha_b(jogo.bola)
    desenha_raq(jogo.raquete)
    desenha_raq(jogo.raquete2)








# TODO testes trata mouse , trata tecla
