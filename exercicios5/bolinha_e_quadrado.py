'''
Coloque o quadrado giratorio e a bolinha dos
exercícios anteriores no mesmo programa.
Isto é, o programa deve consistir em uma animação
com um quadrado giratório crescendo constantemente
e uma bolinha "rolando" pela tela e quicando nas
bordas também em velocidade constante.

'''

from bolinha import *
from quadrado_giratorio import *

Jogo = definir_estrutura("Jogo", "bola, quadrado")
''' Jogo pode ser formado assim: Jogo(Bola, Quadrado)
interp. representa o jogo com uma bolinha quicante e um quadrado giratorio.
'''
#EXEMPLOS:
JOGO_INICIAL = Jogo(BOLA_1, QUADRADO_INICIAL)
JOGO_MEIO = Jogo(BOLA_2, QUADRADO_2)
JOGO_FINAL = Jogo(BOLA_3, QUADRADO_FINAL)


#TEMPLATE
'''
def fn_para_jogo(jogo):
    ... jogo.bola
        jogo.quadrado
'''


'''
fn_jogo: Jogo -> Jogo
interp. cria o novo estado do jogo
'''
def fn_jogo(jogo):
    return Jogo(mover_bola(jogo.bola),fn_quadrado(jogo.quadrado))

'''
desenha: Jogo -> Imagem
interp. desenha na tela o estado atual do jogo
'''
def desenha(jogo):
    desenha_q(jogo.quadrado)
    desenha_b(jogo.bola)

'''
trata_tecla_jogo: 
'''
def trata_tecla_jogo(jogo, tecla):
    if tecla == pg.K_SPACE:
        return Jogo(jogo.bola, QUADRADO_INICIAL)
    return jogo

