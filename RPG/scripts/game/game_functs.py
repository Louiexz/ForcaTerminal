from time import sleep
from ..enemy.dragon_functs import DragonFuncts
from ..character.player_functs import PlayerFuncts

class GameFuncts():
    def fight_result(self, player, dragon):
        # Mostra o resultado da luta
        if dragon.life <= 0: dragon.life = 1
        print(DragonFuncts.show_life(dragon))
        sleep(0.5)
        if player.life <= 0: player.life = 0
        print(PlayerFuncts.show_life(player))
    
    def fight(self, player, dragon, setts, part='start'):
        # Representa a luta
        print(PlayerFuncts.show_able_attacks(player, setts, part))
        try:
            escolha = int(input(' Escolha um ataque: '))
            numbers = [int(item.split(":")[-1]) for item in setts.attacks.split(", ")]
            if escolha in set(numbers):
                PlayerFuncts.attacks(player, escolha)
                print(player.attack)
                dragon.life -= (player.attack - dragon.defense)
        except Exception as e:
            print(e, " Digite um número válido")
            self.fight(player, dragon, setts)
        
        print(DragonFuncts.attack_dragon(player, dragon))

        if player.life <= 30:
            PlayerFuncts.drink_poisson(player, setts)
        self.fight_result(player, dragon)
