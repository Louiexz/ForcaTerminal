import os
from functs import Memoria as jogo

def continue_game():
    if input("\n Deseja sair? [S/N] ").lower() in 'nao, n, não':
        try: os.system('cls')
        except Exception as e: os.system(e, 'clear')
        finally: play_game()

def play_game():
    cards = jogo().ajust_len()
    print("\n Bem-vindo(a) ao jogo da Mémoria com números!")
    while True:
        try:
            print("\n Escolha até no máximo 10 bilhetes")
            x = int(input(" Quantas bilhetes deseja? "))
            if x < 10:
                for _ in range(x):
                    acerto = jogo().user_choice(cards)
                    if acerto: print(" Você acertou!")
                    else: print(" Você errou")
                
                continue_game()
        except ValueError: print(" Apenas números.")