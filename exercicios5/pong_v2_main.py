from pong_v2 import *
''' ================= '''
''' Main (Big Bang):'''


''' Jogo -> Jogo '''

def main(jogo):
    big_bang(jogo, tela=tela, frequencia=FREQUENCIA,
             quando_tick=mover_jogo_2,
             desenhar=desenha_2,
             quando_mouse=trata_mouse_2,
             quando_tecla= trata_tecla,
             quando_solta_tecla=trata_solta_tecla,
             modo_debug= True
             )


main(JOGO_4)