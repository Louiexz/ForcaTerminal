import os
from random import randint

class Adivinhar():
	def __init__(self): pass

	def continue_game(self):
		if input("\nDeseja sair? [S/N) ").lower() in "n, nao, não":
			try: os.system('cls')
			except Exception as e: os.system(e, 'clear')
			finally: self.run_game()

	def run_game(self):
		print('	~~Adivinhe o número!~~')
		numero = randint(1, 99)
		
		while True:
			try:
				tentativa = int(input('\n Digite um número inteiro: '))
				if tentativa == numero:
					print('\n Voce acertou!! ')
					self.continue_game()
				elif tentativa > numero: print('\n Muito alto!')
				else: print('\n Muito baixo!')
			except TypeError: print("\n Apenas números inteiros.")
