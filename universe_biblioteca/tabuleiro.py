#!/usr/bin/env python
# -*- coding: utf-8 -*-


from htdp_pt_br.universe import *


(LARGURA, ALTURA) = (600, 390)
tela = criar_tela_base(LARGURA, ALTURA)

quadrado_branco = retangulo(80,30,Cor("red"))
quadrado_preto = retangulo(80,30,Cor("white"))



duplo_quadrado = lado(quadrado_preto, quadrado_branco)
duplo_quadrado2 = encima(quadrado_branco, quadrado_preto)
minixadrez = duplo_quadrado2

xadrez1 = encima(lado(minixadrez, minixadrez), lado(minixadrez, minixadrez))
xadrez2 = encima((lado((encima(lado(xadrez1, xadrez1), lado(xadrez1, xadrez1))), (encima(lado(xadrez1, xadrez1), lado(xadrez1, xadrez1))))),(lado((encima(lado(xadrez1, xadrez1), lado(xadrez1, xadrez1))), (encima(lado(xadrez1, xadrez1), lado(xadrez1, xadrez1))))))
# colocar_imagem_sobre_tela_e_mostrar(minixadrez, minixadrez.get_width()//2 , minixadrez.get_height()//2)
colocar_imagem_sobre_tela_e_mostrar(xadrez2, xadrez2.get_width()//2 , xadrez2.get_height()//2)

# 
# def xadrez(tamanho, cor1, cor2):
#     dezesseis(padrao_xadrez(tamanho//4, cor1, cor2 ))

