import os
from random import choice

class Forca:
	def __init__(self):
		paises = ['Alemanha', 'Austrália', 'Canadá', 'Estados Unidos', 'França', 'Itália', 'Reino Unido', 'África do Sul', 'Arábia Saudita', 'Argentina', 'Brasil', 'Coreia do Sul', 'Indonésia', 'México', 'Rússia', 'Turquia']
		comidas = ['Doce de batata', 'Churrasco', 'Tapioca', 'Feijão tropeiro', 'Arroz carreteiro', 'Paçoca', 'Pato no tucupi', 'Maniçoba', 'Baião-de-dois', 'Acarajé', 'Pamonha', 'Dobradinha', 'Rapadura', 'Farofa-de-içá', 'Barreado', 'Pastel', 'Palmito', 'Camarão na moranga', 'Doce de abóbora', 'Feijoada', 'feijão']
		objetos = ['Abajur', 'Cabide', 'Cadeira', 'Caneca', 'Cobertor', 'Colchao', 'Colher', 'Computador', 'Edredom', 'Escrivaninha', 'Esfregao', 'Espelho', 'Fronha', 'Prateleira', 'Quadro', 'Relógio', 'Sabonete', 'Toalha', 'Vassoura', 'Xícara']
		roupas = ['chinelo', 'sandalia', 'sapatilha', 'sapatenis', 'alpagarta', 'pantufa', 'chapeu', 'oculos', 'brinco', 'cachecol', 'pulseira', 'gravata', 'tornozeleira', 'alianca', 'camisa', 'camiseta', 'jaqueta', 'bermuda', 'camisola', 'calcinha', 'casaco', 'paleto', 'pijama', 'vestido', 'colete', 'biquini']

		self.my_titles = [paises, comidas, objetos, roupas]

	def choice_title(self, title):
		titles = [["paises", "pais"], ["comidas", "comida"], ["objetos", "objeto"], ["roupas", "roupa"]]

		for x in range(4):
			if title in titles[x]:
				the_word = choice(self.my_titles[x])
				self.my_titles[x].remove(the_word)
				break
		else:
			print(" Tema não encontrado.")
			the_word = "error"

		return the_word.upper()

	def continue_game(self):
		if input('\n\033[m Deseja continuar? [S/N] ').strip().lower() in 'n, nao': return False
		
		try: os.system('cls')
		except Exception as e: os.system(e, 'clear')
		finally: self.play_game()
	
	def settings_game(self, title):
		letter_sorted = []
		word = self.choice_title(title)
		chance = 5

		if word == 'ERROR' and Forca.continue_game() == True: self.play_game()

		print('\n\n A palavra é:', end= ' ')
		certas = ['_' for c in word]

		for pos, valor in enumerate(certas): print(valor, end= ' ')

		# tentativas
		if len(word) <= 7 >= 7: chance = len(word) - 2

		for x in range(chance):
			caractere = input('\n\033[37m Digite uma letra: ').upper().strip()

			if caractere in letter_sorted: print('\n\033[31m Essa letra já foi sorteada\033[m')
			elif caractere in 'BCDFGHJKLMNPQRSTVWXYZAEIOU':
				letter_sorted.append(caractere)
				if caractere in word:
					for pos, value in enumerate(word):
						if value == caractere: certas[pos] = caractere

			for pos, value in enumerate(certas): print(' ',value, end= '')

			print('\n\033[37m Letras que já foram sorteadas: \n\033[31m', letter_sorted)
			print('  Vezes restantes', chance)

			chance -= 1
			if chance == 0:
				end_try = input("\n Qual é a palavra? ").upper().strip()
				if end_try == word: print("\n Você acertou!!")
				else: print("\n Errado! Quem sabe da próxima vez")
		
		self.continue_game()

	def play_game(self):
		print('\033[37m\t\nJogo da Forca\n Temas: Países, Comidas, Objetos, Roupas\n')
		title = input(' Qual tema voce deseja? ').strip().lower()

		self.settings_game(title)
