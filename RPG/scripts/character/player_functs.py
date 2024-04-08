class PlayerFuncts():
    def attacks(player, escolha=0):
        attacks = {
            'leve' : [1, player.light_attack],
            'leve duplo' : [2, player.light_attack * 2],
            'pesado' : [3, player.heavy_attack],
            'pesado duplo' : [4, player.heavy_attack * 2],
            'especial' : [5, player.especial_attack],
        }

        for attack, info in attacks.items():
            if escolha == info[0]:
                player.attack = info[1]
                return f'\n ~{player.name} acertou um: golpe {attack} vezes~'
        else: return '\n Nenhuma opção escolhida'

    def show_life(player):
        return f' Você tem: {player.life} de vida'

    def drink_poisson(player, setts):
        print(f'\n\033[31m Você está à beira da morte\033[m')

        if input("\n Deseja tomar uma poção de cura? [S/N] ") in 's, sim':
            player.life += setts.poisson

    def show_able_attacks(player, setts, part):
        if part == 'start':
            setts.attacks = ', '.join([f'{x}: {y}' for x, y in setts.start_attacks.items()])
        else:
            setts.attacks = ', '.join([f'{x}: {y}' for x, y in setts.end_attacks.items()])
            
        return f'\n Ataques liberados- {setts.attacks}'