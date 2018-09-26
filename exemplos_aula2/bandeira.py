#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
PROBLEMA: Desenhar bandeira do EUA
'''

from universe import *

tela  = criar_tela_base(600,400)

colocar_imagem_sobre_tela_e_mostrar(tela,300,200)

quadrado_branco = retangulo(50,50,Cor("gray"))

tela = colocar_imagem_sobre_tela_e_mostrar(quadrado_branco, 300,200)