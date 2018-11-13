'''

Incremente o exercicio pong_v1 acrescentando
mais uma raquete, que seria o Player 2. No caso,
a segunda raquete deve ser controlada pelo teclado.
Implemente também a parte do jogo em que um jogador
ganha ou perde, isto é, se encostar na parede do fundo,
dá ponto para o adversário, e faz a bola retornar
para o centro do "campo".

EXTRA: faça a contagem de pontos de cada
adversário

EXTRA: faça com que somente conte pontos para o adversá-
rio quando encosta em uma área limitada do fundo (tipo
um golzinho).

'''

'''Ping Pong multiplayer'''

from pong_v1 import *

DX_RAQUETE2 = 10
PLAYER_1_PLACAR= 0
PLAYER_2_PLACAR= 0
AUMENTO_PLACAR = 10
PLACAR_MAX = 50

'''Definicao de dados'''
Raquete2 = definir_estrutura("Raquete2", "x, y, dx")
'''
Raquete pode ser formado por: Raquete2(Int[LARGURA, ALTURA], Int[LARGURA, ALTURA], Int)
interp. representa uma raquete no jogo
'''
# Exemplos:
RAQ_1=Raquete2(LARGURA//2,50,0)
RAQ_2=Raquete2(300,200,0)
RAQ_3=Raquete2(500,300,0)


Jogo = definir_estrutura("Jogo", "bola, raquete, raquete2, player1, player2, game_over")
''' Jogo pode ser formado assim: Jogo(Bola, Raquete, Raquete2, Int, Int, Boolean)
interp. representa o jogo com uma bolinha quicante e dois raquete.
'''
#EXEMPLOS:
JOGO_4 = Jogo(BOLA_1, RAQUETE_1, RAQ_1, 0, 0, False)
JOGO_2 = Jogo(BOLA_2, RAQUETE_2, RAQ_1, 20, 30, False)
JOGO_3 = Jogo(BOLA_3, RAQUETE_3, RAQ_3, 10, 40, True)

#TEMPLATE
'''
def fn_para_jogo(jogo):
    if jogo.game_over:
        ... jogo.bola
            jogo.raquete
            jogo.raquete2
            jogo.player1
            jogo.player2
'''

'''Funcoes'''

'''
mover_raquete: Raquete2 -> Raquete2
interp. retorna o novo estado da raquete
'''
def mover_raquete(raq):
    return Raquete2(raq.x + raq.dx, raq.y, raq.dx)

'''
contador_pontos: Jogo -> jogo
interp. incrementa ou nao o valor do score, se incrementar volta a bola no centro da tela
'''

def contador_pontos(jogo):
    if (jogo.bola.y <= LIMITE_CIMA):
        return Jogo(Bola(LARGURA//2, ALTURA//2, jogo.bola.dx, jogo.bola.dy),
                    jogo.raquete, jogo.raquete2, jogo.player1 + AUMENTO_PLACAR, jogo.player2, jogo.game_over)

    if (jogo.bola.y >= LIMITE_BAIXO ):
        return Jogo(Bola(LARGURA//2, ALTURA//2, jogo.bola.dx, jogo.bola.dy),
                    jogo.raquete, jogo.raquete2, jogo.player1, jogo.player2 + AUMENTO_PLACAR, jogo.game_over)
    return jogo


'''
verfica_placar: Jogo -> Jogo
interp. verifica se nenhum dos dois jogadores ja atingiram o maximo de pontos
'''

def verifica_placar(j):
    if(j.player1 >= PLACAR_MAX):
        return Jogo(j.bola, j.raquete, j.raquete2, j.player1, j.player2, True)

    if(j.player2 >= PLACAR_MAX):
        return Jogo(j.bola, j.raquete, j.raquete2, j.player1, j.player2, True)

    return j

'''
mover_jogo_2: Jogo -> Jogo
interp. retorna o novo estado do jogo
'''
def mover_jogo_2(jogo):
    if not jogo.game_over:

        jogo = contador_pontos(jogo)

        jogo = verifica_placar(jogo)

        if (colidirem(jogo.bola, jogo.raquete)):
            return Jogo(mover_bola(Bola(jogo.bola.x, jogo.bola.y, jogo.bola.dx, -jogo.bola.dy)),jogo.raquete, mover_raquete(jogo.raquete2),
                        jogo.player1, jogo.player2, jogo.game_over)

        if (colidirem(jogo.bola, jogo.raquete2)):
            return Jogo(mover_bola(Bola(jogo.bola.x, jogo.bola.y, jogo.bola.dx, -jogo.bola.dy)),jogo.raquete, mover_raquete(jogo.raquete2),
                        jogo.player1, jogo.player2, jogo.game_over)

        return Jogo(mover_bola(jogo.bola), jogo.raquete, mover_raquete(jogo.raquete2), jogo.player1, jogo.player2, jogo.game_over)
    return jogo

'''
trata_mouse_2: Jogo, Int, Int, EventoMouse -> Jogo:
Quando o mouse se movimentar para os lados na posiçao x no mouse produz a nova posicao da raquete
'''
def trata_mouse_2(jogo, x, y, ev):
    if ev == pg.MOUSEMOTION:
        return Jogo(jogo.bola, Raquete(x, jogo.raquete.y), jogo.raquete2, jogo.player1, jogo.player2, jogo.game_over)
    return jogo

'''
trata_tecla: Jogo, Tecla -> Jogo
interp. muda o estado do jogo de acordo com a tecla pressionada
'''

def trata_tecla(jogo, tecla):
    if tecla == pg.K_LEFT:
        return Jogo(jogo.bola, jogo.raquete, Raquete2(jogo.raquete2.x, jogo.raquete2.y, -DX_RAQUETE2), jogo.player1, jogo.player2, jogo.game_over)

    elif tecla == pg.K_RIGHT:
        return Jogo(jogo.bola, jogo.raquete, Raquete2(jogo.raquete2.x, jogo.raquete2.y, DX_RAQUETE2), jogo.player1, jogo.player2, jogo.game_over)

    elif tecla == pg.K_RETURN:
        return JOGO_4

    return jogo

'''
trata_solta_tecla : Jogo Tecla -> Jogo
interp. muda o estado do dx da raquete 2 quando a tecla eh solta.
'''
def trata_solta_tecla(jogo, tecla):
    if tecla == pg.K_LEFT or tecla == pg.K_RIGHT:
        return Jogo(jogo.bola, jogo.raquete, Raquete2(jogo.raquete2.x, jogo.raquete2.y, 0), jogo.player1, jogo.player2, jogo.game_over)
    return jogo

'''
desenha_2: Jogo -> Imagem
interp. retorna a imagem de representacao do jogo.
'''
def desenha_2(jogo):
    if not jogo.game_over:

        desenha_b(jogo.bola)
        desenha_raq(jogo.raquete)
        desenha_raq(jogo.raquete2)
        desenha_player(jogo.player1, jogo.player2)

    desenha_player(jogo.player1, jogo.player2)
    desenha_game_over(jogo)

'''
desenha_game_over: Jogo -> Imagem
Desenha a tela do game over
'''
def desenha_game_over(jogo):
    if jogo.game_over:
        if jogo.player1 < 100:
            texto_game_over = texto("GAME OVER", Fonte("comicsans", 50), Cor("red"))
            colocar_imagem(texto_game_over, tela, LARGURA//2, ALTURA//2)
            texto_game_over = texto("GANHADOR PLAYER 2", Fonte("comicsans", 35), Cor("red"))
            colocar_imagem(texto_game_over, tela, LARGURA//2, ALTURA//1.5)
        else:
            texto_game_over = texto("GAME OVER", Fonte("comicsans", 50), Cor("red"))
            colocar_imagem(texto_game_over, tela, LARGURA//2, ALTURA//2)
            texto_game_over = texto("GANHADOR PLAYER 1", Fonte("comicsans", 35), Cor("red"))
            colocar_imagem(texto_game_over, tela, LARGURA//2, ALTURA//1.5)

'''
desenha_game_over: Boolean -> Imagem
Desenha o score
'''

def desenha_player(player1, player2):
    texto_player_1 = texto("Player 1: "+ str(player1), Fonte("comicsans", 30), Cor("red"))
    colocar_imagem(texto_player_1, tela, LARGURA//4, ALTURA//14)
    texto_player_2 = texto("Player 2: "+ str(player2), Fonte("comicsans", 30), Cor("red"))
    colocar_imagem(texto_player_2, tela, LARGURA//1.5, ALTURA//14)
