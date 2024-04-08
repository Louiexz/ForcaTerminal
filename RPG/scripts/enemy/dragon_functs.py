class DragonFuncts():
    def attack_dragon(player, dragon):
        player.life -= (dragon.attack - player.defense)
        return ' ~Dragão ataca'
    
    def show_life(dragon): return f'\n O dragão tem: {dragon.life} de vida'
