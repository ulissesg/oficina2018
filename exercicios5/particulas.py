'''
Reaproveitando a definição já existente da bolinha,
crie uma animação com várias bolinhas com direções e velocidades
aleatórias que colidem entre si
'''
from bolinha import *
import random
import math

BOLA_1 = Bola(random.randrange(LIMITE_ESQUERDO,LIMITE_DIREITO),random.randrange(LIMITE_CIMA,LIMITE_BAIXO),random.randrange(2,5),random.randrange(2,5))
BOLA_2 = Bola(random.randrange(LIMITE_ESQUERDO,LIMITE_DIREITO),random.randrange(LIMITE_CIMA,LIMITE_BAIXO),random.randrange(2,5),random.randrange(2,5))
BOLA_3 = Bola(random.randrange(LIMITE_ESQUERDO,LIMITE_DIREITO),random.randrange(LIMITE_CIMA,LIMITE_BAIXO),random.randrange(2,5),random.randrange(2,5))
BOLA_4 = Bola(random.randrange(LIMITE_ESQUERDO,LIMITE_DIREITO),random.randrange(LIMITE_CIMA,LIMITE_BAIXO),random.randrange(2,5),random.randrange(2,5))
BOLA_5 = Bola(random.randrange(LIMITE_ESQUERDO,LIMITE_DIREITO),random.randrange(LIMITE_CIMA,LIMITE_BAIXO),random.randrange(2,5),random.randrange(2,5))

Jogo = definir_estrutura("Jogo", "bola1, bola2, bola3, bola4, bola5")
''' Jogo pode ser formado assim: Jogo(Bola, Bola, Bola, Bola, Bola)
interp. representa o jogo com varias bolinha quicantes.
'''
#EXEMPLOS:
JOGO_1 = Jogo(BOLA_1, BOLA_2, BOLA_3, BOLA_4, BOLA_5)
JOGO_2 = Jogo(BOLA_3, BOLA_5, BOLA_1, BOLA_2, BOLA_4)

#TEMPLATE
'''
def fn_para_jogo(jogo):
    ... jogo.bola1
        jogo.bola2
        ...
'''

'''
colidem : Bola, Bola -> boolean
interp calcula a distancia das bolas.
'''
def colidem(b1, b2):
    if (math.sqrt(pow((b2.x - b1.x), 2) + pow((b2.y - b1.y),2)) < TAMANHO_BOLA * 2):
        return True
    return False

def fn_jogo(jogo):
    # TODO
    #  Compracoes com a bola 1
    if (colidem(jogo.bola1, jogo.bola2)):
        return Jogo(mover_bola(Bola(jogo.bola1.x,jogo.bola1.y,-jogo.bola1.dx, -jogo.bola1.dy)),
                    mover_bola(Bola(jogo.bola2.x,jogo.bola2.y,-jogo.bola2.dx, -jogo.bola2.dy)),
                    mover_bola(jogo.bola3),
                    mover_bola(jogo.bola4),
                    mover_bola(jogo.bola5))

    elif (colidem(jogo.bola1, jogo.bola3)):
        return Jogo(mover_bola(Bola(jogo.bola1.x,jogo.bola1.y,-jogo.bola1.dx, -jogo.bola1.dy)),
                    mover_bola(jogo.bola2),
                    mover_bola(Bola(jogo.bola3.x,jogo.bola3.y,-jogo.bola3.dx, -jogo.bola3.dy)),
                    mover_bola(jogo.bola4),
                    mover_bola(jogo.bola5))

    elif (colidem(jogo.bola1, jogo.bola4)):
        return Jogo(mover_bola(Bola(jogo.bola1.x,jogo.bola1.y,-jogo.bola1.dx, -jogo.bola1.dy)),
                    mover_bola(jogo.bola2),
                    mover_bola(jogo.bola3),
                    mover_bola(Bola(jogo.bola4.x,jogo.bola4.y,-jogo.bola4.dx, -jogo.bola4.dy)),
                    mover_bola(jogo.bola5))

    elif (colidem(jogo.bola1, jogo.bola5)):
        return Jogo(mover_bola(Bola(jogo.bola1.x,jogo.bola1.y,-jogo.bola1.dx, -jogo.bola1.dy)),
                    mover_bola(jogo.bola2),
                    mover_bola(jogo.bola3),
                    mover_bola(jogo.bola4),
                    mover_bola(Bola(jogo.bola5.x,jogo.bola5.y,-jogo.bola5.dx, -jogo.bola5.dy)))

    # comparacoes com a bola 2

    elif (colidem(jogo.bola1, jogo.bola2)):
        return Jogo(mover_bola(Bola(jogo.bola1.x,jogo.bola1.y,-jogo.bola1.dx, -jogo.bola1.dy)),
                    mover_bola(Bola(jogo.bola2.x,jogo.bola2.y,-jogo.bola2.dx, -jogo.bola2.dy)),
                    mover_bola(jogo.bola3),
                    mover_bola(jogo.bola4),
                    mover_bola(jogo.bola5))

    elif (colidem(jogo.bola2, jogo.bola3)):
        return Jogo(mover_bola(jogo.bola1),
                    mover_bola(Bola(jogo.bola2.x,jogo.bola2.y,-jogo.bola2.dx, -jogo.bola2.dy)),
                    mover_bola(Bola(jogo.bola3.x,jogo.bola3.y,-jogo.bola3.dx, -jogo.bola3.dy)),
                    mover_bola(jogo.bola4),
                    mover_bola(jogo.bola5))

    elif (colidem(jogo.bola2, jogo.bola4)):
        return Jogo(mover_bola(jogo.bola1),
                    mover_bola(Bola(jogo.bola2.x,jogo.bola2.y,-jogo.bola2.dx, -jogo.bola2.dy)),
                    mover_bola(jogo.bola3),
                    mover_bola(Bola(jogo.bola4.x,jogo.bola4.y,-jogo.bola4.dx, -jogo.bola4.dy)),
                    mover_bola(jogo.bola5))

    elif (colidem(jogo.bola2, jogo.bola5)):
        return Jogo(mover_bola(jogo.bola1),
                    mover_bola(Bola(jogo.bola2.x,jogo.bola2.y,-jogo.bola2.dx, -jogo.bola2.dy)),
                    mover_bola(jogo.bola3),
                    mover_bola(jogo.bola4),
                    mover_bola(Bola(jogo.bola5.x,jogo.bola5.y,-jogo.bola5.dx, -jogo.bola5.dy)))

    # comparacoes com a bola 3

    elif (colidem(jogo.bola1, jogo.bola3)):
        return Jogo(mover_bola(Bola(jogo.bola1.x,jogo.bola1.y,-jogo.bola1.dx, -jogo.bola1.dy)),
                    mover_bola(jogo.bola2),
                    mover_bola(Bola(jogo.bola3.x,jogo.bola3.y,-jogo.bola3.dx, -jogo.bola3.dy)),
                    mover_bola(jogo.bola4),
                    mover_bola(jogo.bola5))

    elif (colidem(jogo.bola3, jogo.bola2)):
        return Jogo(mover_bola(jogo.bola1),
                    mover_bola(Bola(jogo.bola2.x,jogo.bola2.y,-jogo.bola2.dx, -jogo.bola2.dy)),
                    mover_bola(Bola(jogo.bola3.x,jogo.bola3.y,-jogo.bola3.dx, -jogo.bola3.dy)),
                    mover_bola(jogo.bola4),
                    mover_bola(jogo.bola5))

    elif (colidem(jogo.bola3, jogo.bola4)):
        return Jogo(mover_bola(jogo.bola1),
                    mover_bola(jogo.bola2),
                    mover_bola(Bola(jogo.bola3.x,jogo.bola3.y,-jogo.bola3.dx, -jogo.bola3.dy)),
                    mover_bola(Bola(jogo.bola4.x,jogo.bola4.y,-jogo.bola4.dx, -jogo.bola4.dy)),
                    mover_bola(jogo.bola5))

    elif (colidem(jogo.bola3, jogo.bola5)):
        return Jogo(mover_bola(jogo.bola1),
                    mover_bola(jogo.bola2),
                    mover_bola(Bola(jogo.bola3.x,jogo.bola3.y,-jogo.bola3.dx, -jogo.bola3.dy)),
                    mover_bola(jogo.bola4),
                    mover_bola(Bola(jogo.bola5.x,jogo.bola5.y,-jogo.bola5.dx, -jogo.bola5.dy)))

    # comparacoes com a bola 4

    elif (colidem(jogo.bola1, jogo.bola4)):
        return Jogo(mover_bola(Bola(jogo.bola1.x,jogo.bola1.y,-jogo.bola1.dx, -jogo.bola1.dy)),
                    mover_bola(jogo.bola2),
                    mover_bola(jogo.bola3),
                    mover_bola(Bola(jogo.bola4.x,jogo.bola4.y,-jogo.bola4.dx, -jogo.bola4.dy)),
                    mover_bola(jogo.bola5))

    elif (colidem(jogo.bola4, jogo.bola2)):
        return Jogo(mover_bola(jogo.bola1),
                    mover_bola(Bola(jogo.bola2.x,jogo.bola2.y,-jogo.bola2.dx, -jogo.bola2.dy)),
                    mover_bola(jogo.bola3),
                    mover_bola(Bola(jogo.bola4.x,jogo.bola4.y,-jogo.bola4.dx, -jogo.bola4.dy)),
                    mover_bola(jogo.bola5))

    elif (colidem(jogo.bola3, jogo.bola4)):
        return Jogo(mover_bola(jogo.bola1),
                    mover_bola(jogo.bola2),
                    mover_bola(Bola(jogo.bola3.x,jogo.bola3.y,-jogo.bola3.dx, -jogo.bola3.dy)),
                    mover_bola(Bola(jogo.bola4.x,jogo.bola4.y,-jogo.bola4.dx, -jogo.bola4.dy)),
                    mover_bola(jogo.bola5))

    elif (colidem(jogo.bola4, jogo.bola5)):
        return Jogo(mover_bola(jogo.bola1),
                    mover_bola(jogo.bola2),
                    mover_bola(jogo.bola3),
                    mover_bola(Bola(jogo.bola4.x,jogo.bola4.y,-jogo.bola4.dx, -jogo.bola4.dy)),
                    mover_bola(Bola(jogo.bola5.x,jogo.bola5.y,-jogo.bola5.dx, -jogo.bola5.dy)))

    # comparacoes com a bola 5

    elif (colidem(jogo.bola1, jogo.bola5)):
        return Jogo(mover_bola(Bola(jogo.bola1.x,jogo.bola1.y,-jogo.bola1.dx, -jogo.bola1.dy)),
                    mover_bola(jogo.bola2),
                    mover_bola(jogo.bola3),
                    mover_bola(jogo.bola4),
                    mover_bola(Bola(jogo.bola5.x,jogo.bola5.y,-jogo.bola5.dx, -jogo.bola5.dy)))

    elif (colidem(jogo.bola5, jogo.bola2)):
        return Jogo(mover_bola(jogo.bola1),
                    mover_bola(Bola(jogo.bola2.x,jogo.bola2.y,-jogo.bola2.dx, -jogo.bola2.dy)),
                    mover_bola(jogo.bola3),
                    mover_bola(jogo.bola4),
                    mover_bola(Bola(jogo.bola5.x,jogo.bola5.y,-jogo.bola5.dx, -jogo.bola5.dy)))

    elif (colidem(jogo.bola3, jogo.bola5)):
        return Jogo(mover_bola(jogo.bola1),
                    mover_bola(jogo.bola2),
                    mover_bola(Bola(jogo.bola3.x,jogo.bola3.y,-jogo.bola3.dx, -jogo.bola3.dy)),
                    mover_bola(jogo.bola4),
                    mover_bola(Bola(jogo.bola5.x,jogo.bola5.y,-jogo.bola5.dx, -jogo.bola5.dy)))

    elif (colidem(jogo.bola4, jogo.bola5)):
        return Jogo(mover_bola(jogo.bola1),
                    mover_bola(jogo.bola2),
                    mover_bola(jogo.bola3),
                    mover_bola(Bola(jogo.bola4.x,jogo.bola4.y,-jogo.bola4.dx, -jogo.bola4.dy)),
                    mover_bola(Bola(jogo.bola5.x,jogo.bola5.y,-jogo.bola5.dx, -jogo.bola5.dy)))


    return Jogo(mover_bola(jogo.bola1),mover_bola(jogo.bola2),mover_bola(jogo.bola3),mover_bola(jogo.bola4),mover_bola(jogo.bola5))

def desenha(jogo):
    desenha_b(jogo.bola1)
    desenha_b(jogo.bola2)
    desenha_b(jogo.bola3)
    desenha_b(jogo.bola4)
    desenha_b(jogo.bola5)