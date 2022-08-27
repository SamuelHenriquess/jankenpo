# Nome dos 2 players
# Placar de vitórias e empates
# "imagem" em ascii art da pedra, papel e tesoura
# Obrigatoriamente estruturado em funções

import random
from time import sleep



def pedra():
    print("template desenho da pedra")

def papel():
    print("template desenho do papel")

def tesoura():
    print("template desenho da tesoura")

def vitoriaplayer():
     
    print(f"brabo {nome} voce ganhou dessa vez")
    pontoplayer = ptplayer 
    print(f"pontuação do jogo {pontoplayer} pro {nome} e {pontobot} pro bot")
    return pontoplayer

def vitoriabot():
     
    print("bot ganhou")
    pontobot = ptbot 
    print(f"pontuação do jogo {pontoplayer} pro {nome} e {pontobot} pro bot")
    return pontobot

def jogo():
    global ptplayer
    global ptbot
    global pontobot
    global pontoplayer
    # 0 pedra 1 papel 2 tesoura
    
    player = int(input(f"eae {nome}! vai jogar pedra(0) papel(1) ou tesoura (2): "))
    bot = random.randint(0,2) 

    if player == bot:
        print("empatou!")
        print(f"pontuação do jogo {pontoplayer} pro {nome} e {pontobot} pro bot")
        jogar = input("vai querer continuar jogando? digite 1 se sim: ")

# player joga pedra

    elif player == 0 and bot == 1:
        pedra()
        papel()
        ptbot += 1
        vitoriabot()
        jogar = input("vai querer continuar jogando? digite 1 se sim: ")

    elif player == 0 and bot == 2:
        pedra()
        tesoura()
        ptplayer += 1
        vitoriaplayer()
        jogar = input("vai querer continuar jogando? digite 1 se sim: ")

# player joga papel

    elif player == 1 and bot == 0:
        papel()
        pedra()
        ptplayer += 1
        vitoriaplayer()
        jogar = input("vai querer continuar jogando? digite 1 se sim: ")
    
    elif player == 1 and bot == 2:
        papel()
        tesoura()
        ptbot += 1
        vitoriabot()
        jogar = input("vai querer continuar jogando? digite 1 se sim: ")

# player joga tesoura

    elif player == 2 and bot == 0:
        ptbot += 1
        vitoriabot()
        jogar = input("vai querer continuar jogando? digite 1 se sim: ")

    elif player == 2 and bot == 1:
        ptbot +=1
        vitoriaplayer()
        jogar = input("vai querer continuar jogando? digite 1 se sim: ")
    return jogar

nome = input("digite seu nome: ")
jogar = int(input("Voce quer jogar? digite 1 se quiser: "))
pontobot = 0
pontoplayer = 0
ptbot = 0
ptplayer = 0

while jogar == 1:
    jogo()
if jogar < 1 or jogar >1:
    print("jogaremos outra vez")
