'''

PROBLEMA:

Projete (design) uma animação de um foguete descendo e pousando na terra.

Lembre-se de seguir a receita de Como Projetar Mundos e as demais!
Não esqueça também de fazer a análise de domínio antes de começar a 
trabalhar no código.

Dica1: a parte da definição de dados já foi feita nos exercícios anteriores! Apenas revise-a e utilize no projeto.

Utilize qualquer imagem de um foguete. Apenas lembre-se de colocar a imagem na mesma pasta que este código.


'''

from htdp_pt_br.universe import*
import unittest

#constantes

ALTURA = 360
LARGURA = 720
FREQUENCIA = 100
X = LARGURA // 2
IMG_FOGUETE = carregar_imagem("foguete.png")
IMG_FOGUETE = definir_dimensoes(IMG_FOGUETE, 100,200)
ALTURA_FOGUETE = altura_imagem(IMG_FOGUETE)

#criar tela
tela = criar_tela_base(LARGURA, ALTURA)

#definicao de dados
'''
Foguete e integer >= 0
interp. defini o ponto que o foguete esta no eixo y
'''
#exemplos

FOGUETE_INICAL = 0
FOGUETE_MEIO = ALTURA // 2
FOGUETE_FINAL = ALTURA

#templates
'''
def fn_para_foguete(f):
    ... f
'''

'''
mover: Foguete -> Foguete
recebe o Foguete(Y) atual e retorna o proximo Foguete(Y)
'''
def mover(f):
    if f < (ALTURA -(ALTURA_FOGUETE //4)):
        return f+1
    return (ALTURA -(ALTURA_FOGUETE // 4))

'''
desenha: Foguete -> imagem
desenha o foguete na tela
'''
def desenha(f):
    colocar_imagem(IMG_FOGUETE, tela, X, f)
    return tela
