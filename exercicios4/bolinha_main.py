from bolinha import*

''' ================= '''
''' Main (Big Bang):'''


''' Bola -> Bola '''
''' inicie o mundo com BOLA_1'''
def main(b):
    big_bang(b, tela=tela, frequencia=FREQUENCIA,
             quando_tick=mover_bola,
             desenhar=desenha_b,
             modo_debug = True
             )


main(BOLA_1)