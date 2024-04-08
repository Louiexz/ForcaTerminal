import os
from random import randint

class Jokenpo:
	def __init__(self):
		self.itens = ('Pedra', 'Papel', 'Tesoura')

	def loop_game(self):
		escolha = int(input('\n\033[33m Qual a sua escolha?\033[m '))
		pc = randint(0, 2)
		print(f'\n\033[37m Computador jogou {self.itens[pc]}')
		
		if escolha > -1 and escolha < 3: print(f' Jogador jogou {self.itens[escolha]}')
		
		if escolha == 0 and pc == 1 or escolha == 1 and pc == 2 or escolha == 2 and pc == 0:
			print('\n\033[31m Voce perdeu!\033[m')
		elif escolha == 0 and pc == 2 or escolha == 1 and pc == 0 or escolha == 2 and pc == 1:
			print('\n\033[36m Voce ganhou!\033[m')
		else: print('\n\033[32m  Erro ou empate\033[m')

		self.continue_game()
		
	def continue_game(self):
		if str(input('\n Deseja continuar? [S/N]: ')).lower() in 's, sim':
			try: os.system('cls')
			except Exception as e: os.system(e, 'clear')
			finally: self.run_game()

	def run_game(self):
		print('\n\033[37m  Vamos jogar Jokenpo\n')
		print(' Para pedra digite: 0\n Para papel digite: 1\n Para tesoura digite: 2')
		
		self.loop_game()
