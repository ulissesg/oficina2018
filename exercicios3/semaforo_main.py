from semaforo import *

def main(s):
    big_bang(s, frequencia=FREQUENCIA,
             quando_tick=troca_cor, #nao consegui usar a_cada_tick
             desenhar= desenha,
             )
main (2)