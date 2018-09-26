from rastreador_mouse import *

''' ================= '''
''' Main (Big Bang):'''


''' Mouse -> Mouse '''

def main(m):
    big_bang(m, tela=tela, frequencia=FREQUENCIA,
             desenhar=desenha,
             quando_mouse=trata_mouse
             )

main(Mouse(0,0))