class Player():
    def __init__(self):
        # Player
        self.name = None
        # Vida do Player
        self.life = 100
        # Ataques do Player
        self.light_attack = 300
        self.heavy_attack = 500
        self.especial_attack = 850 
        self.attack = None
        # Defesa do Player
        self.defense = 70
    
    def restart(self):
        self.life = 100
        self.attack = None
