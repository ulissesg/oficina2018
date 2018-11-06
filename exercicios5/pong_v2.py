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

'''Definicao de dados'''

Jogo = definir_estrutura("Jogo", "bola, raquete, raquete2")
''' Jogo pode ser formado assim: Jogo(Bola, Raquete, Raquete)
interp. representa o jogo com uma bolinha quicante e dois raquete.
'''
#EXEMPLOS:
JOGO_4 = Jogo(BOLA_1, RAQUETE_1, Raquete(100,100))
JOGO_2 = Jogo(BOLA_2, RAQUETE_2, RAQUETE_1)
JOGO_3 = Jogo(BOLA_3, RAQUETE_3, RAQUETE_2)

#TEMPLATE
'''
def fn_para_jogo(jogo):
    ... jogo.bola
        jogo.raquete
        jogo.raquete2
'''

'''Funcoes'''

def mover_jogo_2(jogo):
    if (colidirem(jogo.bola, jogo.raquete)):
        return Jogo(mover_bola(Bola(jogo.bola.x, jogo.bola.y, jogo.bola.dx, -jogo.bola.dy)),jogo.raquete, jogo.raquete2)
    if (colidirem(jogo.bola, jogo.raquete2)):
        return Jogo(mover_bola(Bola(jogo.bola.x, jogo.bola.y, jogo.bola.dx, -jogo.bola.dy)),jogo.raquete, jogo.raquete2)
    return Jogo(mover_bola(jogo.bola), jogo.raquete, jogo.raquete2)

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
        return Jogo(jogo.bola, jogo.raquete, Raquete(jogo.raquete2.x - 10, jogo.raquete2.y))
    elif tecla == pg.K_RIGHT:
        return Jogo(jogo.bola, jogo.raquete, Raquete(jogo.raquete2.x + 10, jogo.raquete2.y))
    return jogo

def desenha_2(jogo):
    desenha_b(jogo.bola)
    desenha_raq(jogo.raquete)
    desenha_raq(jogo.raquete2)

# TODO testes trata mouse , trata tecla
