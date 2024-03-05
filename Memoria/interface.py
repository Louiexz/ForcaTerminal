from adivinhar import adivinharJogo as jogo

def playGame():
    cards = jogo().ajustLen()
    while True:
        try:
            print("Escolha até no máximo 10 bilhetes")
            x = int(input(" Quantas bilhetes deseja? "))
            if x < 10:
                for _ in range(x):
                    acerto = jogo().userChoice(cards)
                    if acerto: print("Você acertou!")
                    else: print("Você errou")

                resposta = input("Deseja sair? [S/N] ")
                
                if reposta.lower() in 'sim, s': break
        except ValueError: print(" Apenas números.")