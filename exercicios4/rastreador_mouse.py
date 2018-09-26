'''

Projete um programa mundo que mostre a posição (x, y) atual
do mouse. Assim, enquanto o mouse se move, os números (x, y) na tela 
mudam (não basta/vale usar o modo_debug).

Para desenhar texto na tela, veja como foi feito no exemplo da contagem regressiva.

Use a receita de como projetar mundos e o template mundo.

'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from htdp_pt_br.universe import *

''' Meu rastreador de mouse '''

'''==================='''
'''# Preparacao da Tela e Constantes: '''

(LARGURA, ALTURA) = (600, 400)
tela = criar_tela_base(LARGURA, ALTURA)

FREQUENCIA = 30
X_TEXTO = 130
Y_TEXTO = 30
FONTE_TEXTO = "monospace"
TAMANHO_TEXTO = 20
COR_TEXTO = "red"
MSG_ERRO = "ERRO"

'''==================='''

'''# Definições de dados: '''

#Criando tipo composto.
Mouse = definir_estrutura("Mouse", "x,y")

''' Mouse eh composto por: Mouse(int, int)
    interp. representa a posicao do mouse na tela com os seguintes campos(x[0,LARGURA],y[0, ALTURA])    
'''

# exemplos
MOUSE_1 = Mouse(0,0)
MOUSE_2 = Mouse(300,200)
MOUSE_3 = Mouse(0,400)
MOUSE_4 = Mouse(600,0)

#template

'''
def fn_para_mouse(m):
    ...m.x
    ...m.y
'''

'''===================='''
''' Funções: '''
'''
desenha: EstadoMundo -> Imagem
Desenha na tela a posicao X, Y do mouse.
'''
def desenha(m):
    img_texto = texto(str(m), Fonte(FONTE_TEXTO, TAMANHO_TEXTO), Cor(COR_TEXTO))
    colocar_imagem(img_texto, tela, X_TEXTO, Y_TEXTO)

'''
trata_mouse: Mouse, Int, Int, EventoMouse -> Mouse:
Quando mover o mouse mostra a posicao atual(x,y) do mouse na tela.
'''

def trata_mouse(m, x, y, ev):

    if ev == pg.MOUSEMOTION:
        m = Mouse(x, y)
        return m
    return m


