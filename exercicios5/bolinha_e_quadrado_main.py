from bolinha_e_quadrado import*


''' ================= '''
''' Main (Big Bang):'''


''' Jogo -> Jogo'''
def main(jogo):
    big_bang(jogo, tela=tela, frequencia=FREQUENCIA,
             quando_tick=fn_jogo,
             desenhar=desenha,
             quando_tecla= trata_tecla_jogo
             )

main(JOGO_INICIAL)