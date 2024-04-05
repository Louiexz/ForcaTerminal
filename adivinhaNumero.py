import os
from random import randint

def play():
	print('	~~Adivinhe o número!~~')
	numero = randint(1, 99)
	while True:
		try:
			tentativa = int(input('\n Digite um número inteiro: '))
			if tentativa == numero:
				print('\n Voce acertou!! ')
				resposta = input("\nDeseja sair? [S/N) ")
				if resposta.lower() in "sim, s": break
				else: print(); play(); os.system('cls')
			elif tentativa > numero: print('\n Muito alto!')
			else: print('\n Muito baixo!')
		except TypeError: print("\n Apenas números inteiros.")

play()