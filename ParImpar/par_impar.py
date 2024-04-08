import os
from random import randint

class ParImpar():
	def __init__(self):
		self.QUANTIDADE = 0
	
	def loop(self, num, choice):
		pc = randint(0, 10)
		print(f'\n O computador jogou {pc}')
		s = num + pc
		print(f'\n {num} + {pc} = {s}\n')
		
		if choice in 'par':
			if s % 2 == 0:
				print(f'\033[32m {s} é par. Voce ganhou!\033[m\n')
				print('='*30); self.QUANTIDADE += 1
			else: print(f'\033[31m {s} é ímpar. Game Over!\033[m\n')
		elif choice in ['ímpar', 'impar']:
			if s % 2 != 0:
				print(f'\033[32m {s} é ímpar. Voce ganhou!\033[m\n')
				print('='*30); self.QUANTIDADE += 1
			else: print(f'\033[31m {s} é par. Game Over!\033[m\n')

		print(f'\033[33m Voce venceu {self.QUANTIDADE} vezes\033[m')
		self.continue_game()

	def continue_game(self):
		if input("\n Deseja continuar? [S/N] ").lower() in 's, sim':
			try: os.system('cls')
			except Exception as e: os.system(e, 'clear')
			finally: self.run_game()

	def run_game(self):
		print('\n\033[37m\tVai dar par ou ímpar?\n')

		num = int(input('\033[33m Digite um número: '))
		choice = input('\033[m Vai dar par ou ímpar? ').lower()

		self.loop(num, choice)
