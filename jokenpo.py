# Nome dos 2 players
# Placar de vitórias e empates
# "imagem" em ascii art da pedra, papel e tesoura
# Obrigatoriamente estruturado em funções

import random
from time import sleep

def pedra():
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

def papel():
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

def tesoura():
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

def vitoriaplayer(): 
    global ptplayer
    global ptbot # faz com que as variaveis mudem de valor, existindo em escopo global
    print(f"brabo {nome} voce ganhou dessa vez")
    ptplayer += 1
    print(f"pontuação do jogo {ptplayer} pro {nome} e {ptbot} pro bot")
    

def vitoriabot():
    global ptplayer
    global ptbot # faz com que as variaveis mudem de valor, existindo em escopo global
    print("bot ganhou")
    ptbot += 1
    print(f"pontuação do jogo {ptplayer} pro {nome} e {ptbot} pro bot")
    

def jogo():
    global ptplayer
    global ptbot
    # 0 pedra 1 papel 2 tesoura
    
    player = int(input(f"eae {nome}! vai jogar pedra(0) papel(1) ou tesoura (2): "))
    bot = random.randint(0,2) 

    if player == bot:
        print("empatou!")
        print(f"pontuação do jogo {ptplayer} pro {nome} e {ptbot} pro bot")
        jogar = int(input("vai querer continuar jogando? digite 1 se sim: "))

# player joga pedra

    elif player == 0 and bot == 1:
        pedra()
        sleep(1)
        papel()
        sleep(0.5)
        vitoriabot()
        jogar = int(input("vai querer continuar jogando? digite 1 se sim: "))

    elif player == 0 and bot == 2:
        pedra()
        sleep(1)
        tesoura()
        sleep(0.5)
        vitoriaplayer()
        jogar = int(input("vai querer continuar jogando? digite 1 se sim: "))

# player joga papel

    elif player == 1 and bot == 0:
        papel()
        sleep(1)
        pedra()
        sleep(0.5)
        vitoriaplayer()
        jogar = int(input("vai querer continuar jogando? digite 1 se sim: "))
    
    elif player == 1 and bot == 2:
        papel()
        sleep(1)
        tesoura()
        sleep(0.5)
        vitoriabot()
        jogar = int(input("vai querer continuar jogando? digite 1 se sim: "))

# player joga tesoura

    elif player == 2 and bot == 0:        
        tesoura()
        sleep(1)
        pedra()
        sleep(0.5)
        vitoriabot()
        jogar = int(input("vai querer continuar jogando? digite 1 se sim: "))

    elif player == 2 and bot == 1:
        tesoura()
        sleep(1)
        papel()
        sleep(0.5)
        vitoriaplayer()
        jogar = int(input("vai querer continuar jogando? digite 1 se sim: "))



jogar = int(input("Voce quer jogar? digite 1 se quiser: "))

if jogar ==1:
    nome = input("digite seu nome: ")

ptbot = 0
ptplayer = 0

while jogar == 1:
    jogo()
if not jogar  == 1:
    print("jogaremos outra vez")
