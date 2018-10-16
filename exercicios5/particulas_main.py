from particulas import *

''' ================= '''
''' Main (Big Bang):'''


''' Jogo -> Jogo'''
def main(jogo):
    big_bang(jogo, tela=tela, frequencia=30,
             quando_tick=fn_jogo,
             desenhar=desenha
             )

main(JOGO_1)