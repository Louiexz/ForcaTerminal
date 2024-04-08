from time import sleep
from .game_functs import GameFuncts

class GameControls:
	"""Classe representando funções de um jogo de RPG"""
	def introduce(self, player):
		# Introdução a história
		print('\033[37m Vamos cavaleiro, venha lutar ao meu lado contra o dragão que está atacando nosso reino!\n')
		player.name = input(' Diga-me seu nome primeiro: ').strip().capitalize()
		print(f'\n Certo {player.name}, vamos à luta.')
		sleep(0.5)

	def success_game(self, player, dragon):
		# Sucesso no jogo
		print(f'\n ~{player.name} corta a cabeça do dragão com um golpe final~')
		sleep(1.5)
		print(f'\n\033[32m Você venceu, {player.name}!\033[m Agora o reino está a salvo, graças a você!')

	def game_over(self, player, dragon):
		# Final falho
		print('\n Sua vida é', player.life)
		player.life -= dragon.swallow
		sleep(1.0)

		if player.life <= 0:
			print(' \n ~O dragão te engole~')
			sleep(1.5)
			return '\n\033[31m Você perdeu!\033[m Boa sorte na próxima.'

	def restart(self, player, dragon, setts):
		if input('\n Deseja recomeçar? [S/N] ').lower() in 's, sim':
			setts.restart()
			dragon.restart()
			player.restart()
			self.run_game(player, dragon, setts)
	
	def run_game(self, player, dragon, setts):
		self.introduce(player)
		
		for x in range(3):
			if x == 2: GameFuncts().fight(player, dragon, setts, 'end')
			else: GameFuncts().fight(player, dragon, setts)
		
		if dragon.life <= 1: self.success_game(player, dragon)
		else:
			print(self.game_over(player, dragon))
			self.restart(player, dragon, setts)
			
