import os
from random import randint

def run():
    print('\033[37m  Vamos jogar Jokenpo\n\n Para pedra digite: [0]\n Para papel digite: [1]\n Para tesoura digite: [2]')
    
    loop()

def loop():
	itens = ('Pedra', 'Papel', 'Tesoura')
	
	escolha = int(input('\n\033[33m Qual a sua escolha?\033[m '))
	pc = randint(0, 2)
	print(f'\033[37m Computador jogou {itens[pc]}')
	if escolha > -1 and escolha < 3:
		print(f' Jogador jogou {itens[escolha]}')
	if escolha == 0 and pc == 1 or escolha == 1 and pc == 2 or escolha == 2 and pc == 0:
		print('\n\033[31m  Voce perdeu!\033[m')
	elif escolha == 0 and pc == 2 or escolha == 1 and pc == 0 or escolha == 2 and pc == 1:
		print('\n\033[36m Voce ganhou!\033[m')
	else:
		print('\n\033[32m  Erro ou empate\033[m')
	exit = str(input('\n Deseja continuar? [S/N]: ')).upper()
	if exit.lower() in 's, sim':
	    os.system('clear')
	    run()

run()