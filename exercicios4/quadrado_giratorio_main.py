from quadrado_giratorio import*

''' ================= '''
''' Main (Big Bang):'''


''' Quadrado -> Quadrado'''
def main(quad):
    big_bang(quad, tela=tela, frequencia= FREQUENCIA,
             quando_tick=fn_quadrado,
             desenhar=desenha,
             quando_tecla= trata_tecla,
             modo_debug=True
             )

main(QUADRADO_INICIAL)