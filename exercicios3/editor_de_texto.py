'''
PROBLEMA:

Projete um programa de editor de texto simples (de uma linha).
O programa deve permitir que o usuário digite com o teclado, dando feedback imediato na tela.
Deve permitir, também, que o usuário conserte seu texto por meio da tecla 'backspace' (tecla de apagar texto).

DICA1: Muita atenção na análise de domínio. Uma análise bem feita facilitará o desenvolvimento.
DICA2: o valor referente à tecla 'backspace' é pg.K_BACKSPACE, e para as letras do alfabeto é, pg.K_a, pg.K_b, pg.K_c,
        e assim por diante.
DICA3: veja como desenhar texto na tela no exemplo contagem_regressiva.py.
       Use sabiamente as constantes (se fez analise de dominio bem feita, isso torna-se natural).
DICA4: use 'nome_variavel[:-1]' para pegar o texto sem a última letra
DICA5: verifique o que acontece quando tenta dar 'backspace' em um texto vazio (pode ser necessário usar (if ...) )
DICA6: use concatenação de strings
        para inserir uma nova letra no final do texto (ex: nome_variavel+"a"). Para transformar o 
        valor da tecla em string (ex: pg.K_a -> "a"), use: chr(pg.K_a)
DICA7: este programa não precisa de 'quando_tick=...'. Por quê?

NÃO ESQUEÇAM QUE TODAS AS RECEITAS DEVEM SER UTILIZADAS, ASSIM COMO OS TEMPLATES APROPRIADOS!!

'''

from htdp_pt_br.universe import *

#declaracao de variaveis

ALTURA = 70
LARGURA = 800
TIPO_FONTE = "serif"
TAMANHO_FONTE = 20
COR_FONTE = "black"

tela = criar_tela_base(LARGURA, ALTURA)

#definicao de dados
'''
Texto e uma string
interp. composta apenas por simbolos ASC validos.
'''
'''exemplos'''

texto1 = "a"
texto2 = "ab"
texto3 = "abc*"

#template
'''
def fn_para_texto (t):
    ... t 
'''

#definicao de funcoes

'''
desenha_texto: Texto -> Texto
concatena o novo dado inserido com a string ja existente.
'''
def desenha_texto (t):
    img_texto = texto(str(t), Fonte(TIPO_FONTE, TAMANHO_FONTE), Cor(COR_FONTE))
    colocar_imagem(img_texto, tela, LARGURA //2, ALTURA//2)

'''
trata_tecla: Texto, tecla -> Texto
recebe um Texto e uma tecla do teclado(numero) e devolve um Texto
'''
def trata_tecla(t, tecla):
    if (tecla == pg.K_BACKSPACE):
        if (t == ''):
            return t
        return t[:-1]

    elif (tecla >= 32) and (tecla <= 126):
        return t+chr(tecla)

    else:
        return t

def main(t):
    big_bang(t,tela=tela,
             desenhar= desenha_texto,
             frequencia=30,
             quando_tecla=trata_tecla)

main("hv")