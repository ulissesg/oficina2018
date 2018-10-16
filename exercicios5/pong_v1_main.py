from pong_v1 import *

''' ================= '''
''' Main (Big Bang):'''


''' Jogo -> Jogo '''

def main(jogo):
    big_bang(jogo, tela=tela, frequencia=FREQUENCIA,
             quando_tick=mover_jogo,
             desenhar=desenha,
             quando_mouse=trata_mouse,
             modo_debug = True
             )


main(JOGO_1)