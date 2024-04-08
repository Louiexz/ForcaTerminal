class OlderGame():
	def __init__(self):
		self.matriz = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

	def matriz_pos(self, vez=None, escolha=0):
		if escolha in self.matriz[0]:
			for pos, valor in enumerate(self.matriz[0]):
				if valor == escolha:
					if vez == 'par': self.matriz[0][pos] = 'X'
					else: self.matriz[0][pos] = 'O'
		
		elif escolha in self.matriz[1]:
			for pos, valor in enumerate(self.matriz[1]):
				if valor == escolha:
					if vez == 'par': self.matriz[1][pos] = 'X'
					else: self.matriz[1][pos] = 'O'
		
		elif escolha in self.matriz[2]:
			for pos, valor in enumerate(self.matriz[2]):
				if valor == escolha:
					if vez == 'par': self.matriz[2][pos] = 'X'
					else: self.matriz[2][pos] = 'O'
			
		else: print('\n Escolha inválida.')
		
		return f'\n	{self.matriz[0]}\n	{self.matriz[1]}\n	{self.matriz[2]}\n'

	def jogador_choice(self):
		local = 0
		print(f'\n	{self.matriz[0]}\n	{self.matriz[1]}\n	{self.matriz[2]}\n')

		for c in range(0, 9):
			if c % 2 == 0:
				jogador_one = input('Jogador um: Onde você quer colocar o "X"? ')
				local = jogador_one; jogo = 'par'
			else:
				jogador_two = input('Jogador dois: Onde você quer colocar o "0"? ')
				local = jogador_two; jogo = 'impar'

			print(self.matriz_pos(jogo, local))
	
	def run(self):
		print("\nn ~Iniciando jogo da velha~")
		self.jogador_choice()