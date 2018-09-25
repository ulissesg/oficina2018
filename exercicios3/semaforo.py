'''
PROBLEMA:
Projete (design) uma animação de um semáforo.
Seu programa deve mostrar um semáforo que é vermelho, depois verde,
depois amarelo, depois vermelho, etc. Para este programa, a definição
de dados do estado mutável do mundo deve ser uma enumeração.
Para fazer as luzes mudarem a uma velocidade razoável, você pode usar
a opção 'frequencia' do big_bang. Por exemplo, 'big_bang(inic, frequencia=1, ...)' fará o
big-bang esperar 1 segundo antes de chamar a função no 'quando_tick'.
Lembre-se de seguir a receita de Como Projetar Mundos e as demais!
Não esqueça também de fazer a análise de domínio antes de começar a
trabalhar no código.
Dica1: a parte da definição de dados já foi feita em aula! Apenas revise-a e utilize no projeto.
Dica2: o ideal é não utilizar a imagem como o valor do tipo de dado semáforo, mas apenas como a
representação gráfica (como no caso do gato, que é apenas um número).
Imagens de exemplo na pasta (vc pode colocar outras imagens se preferir)
'''
from htdp_pt_br.universe import*
import unittest

#constantes
LAGURA = 250
ALTURA = 600
FREQUENCIA = 1
X = LAGURA // 2
Y = ALTURA // 2

#importanto as imagens

IMG_SEMAFORO_0 = carregar_imagem("semaforo1.png")
IMG_SEMAFORO_0= definir_dimensoes(IMG_SEMAFORO_0, X * 2 , Y * 2)

IMG_SEMAFORO_1 = carregar_imagem("semaforo2.png")
IMG_SEMAFORO_1= definir_dimensoes(IMG_SEMAFORO_1, X * 2 , Y * 2)

IMG_SEMAFORO_2 = carregar_imagem("semaforo3.png")
IMG_SEMAFORO_2= definir_dimensoes(IMG_SEMAFORO_2, X * 2 , Y * 2)

#definicao de dados
'''
Semaforo e um integer
interp. podendo ter os valores 0,1,2
'''

SEMAFORO1 = 0   #representado visualmente pela luz vermelha do sinal
SEMAFORO2 = 1   #representado visualmente pela luz amarela do sinal
SEMAFORO3 = 2   #representado visualmente pela luz verde do sinal

#template
'''
def fn_para_semaforo(s):
    ...s
'''
#definicao das funcoes
'''
troca_cor: Semaforo -> Semaforo
muda para o proximo semaforo, os tres possiveis sao : 0,1,2
'''
def troca_cor(s):
    if (s >= 0) and (s < 2):
        return s+1
    return 0

'''
desenha: Semaforo -> Imagem
desenha a imagem corresponde ao Semaforo na tela 
'''
def desenha(s):
    if s == 0:
        colocar_imagem(IMG_SEMAFORO_0, tela, X, Y)
        return tela
    if s == 1:
        colocar_imagem(IMG_SEMAFORO_1, tela, X, Y)
        return tela
    if s == 2:
        colocar_imagem(IMG_SEMAFORO_2, tela, X, Y)
        return tela

#criando a tela
tela = criar_tela_base(LAGURA, ALTURA)


