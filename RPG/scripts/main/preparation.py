from ..game.game_control import GameControls
from ..enemy.dragon import Dragon
from ..character.player import Player
from .settings import Settings

def initialize_game():
    player = Player()
    dragon = Dragon()
    setts = Settings()

    GameControls().run_game(player, dragon, setts)
    