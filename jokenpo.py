# Nome dos 2 players
# Placar de vitórias e empates
# "imagem" em ascii art da pedra, papel e tesoura
# Obrigatoriamente estruturado em funções
import random
from time import sleep
ptplayer = 0
ptbot = 0

def pedra():
    print("template desenho da pedra")

def papel():
    print("template desenho do papel")

def tesoura():
    print("template desenho da tesoura")

def vitoriaplayer():
    print(f"brabo {nome} voce ganhou dessa vez")
    ptplayer +=1
    print(f"pontuação do jogo {ptplayer} pro {nome} e {ptbot} pro bot")
    return ptplayer

def vitoriabot():
    print("bot ganhou")
    ptbot +=1
    print(f"pontuação do jogo {ptplayer} pro {nome} e {ptbot} pro bot")
    return ptbot

def jogo():
    # 0 pedra 1 papel 2 tesoura
    
    player = int(input(f"eae {nome}! vai jogar pedra(0) papel(1) ou tesoura (2): "))
    bot = random.randint(0,2) 

    if player == bot:
        print("empatou!")
        print(f"pontuação do jogo {ptplayer} pro {nome} e {ptbot} pro bot")

# player joga pedra

    elif player == 0 and bot == 1:
        pedra()
        papel()
        vitoriabot()

    elif player == 0 and bot == 2:
        pedra()
        tesoura()
        vitoriaplayer()

# player joga papel

    elif player == 1 and bot == 0:
        papel()
        pedra()
        vitoriaplayer()
    
    elif player == 1 and bot == 2:
        papel()
        tesoura()
        vitoriabot()

# player joga tesoura

    elif player == 2 and bot == 0:
        vitoriabot()

    elif player == 2 and bot == 1:
        vitoriaplayer()

nome = input("digite seu nome: ")
jogo()