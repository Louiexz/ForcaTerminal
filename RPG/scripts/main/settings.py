from ..enemy.dragon import Dragon
from ..character.player import Player

class Settings():
    def __init__(self):
        # Ferramentas
        self.poisson = 20 # Poção de cura
        # Ataques do jogador
        self.attacks = None
        self.start_attacks = {
            'Leve' : '1',
            'Leve duplo' : '2',
            'Pesado' : '3',
        }
        self.end_attacks = {
            'Pesado duplo' : '4',
            'Especial: espada flamejante' : '5',
        }
    
    def restart(self):
        self.attacks = None