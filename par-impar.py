from random import randint

qt = 0

print('\033[37m   Jogo: Par ou Ímpar?\n')

while True:
	num = int(input('\033[33m  Digite um número: '))
	choice = input('  Vai dar par ou ímpar? ').lower().strip()
	pc = randint(0, 10)
	print(f'\n O computador jogou {pc}')
	s = num + pc
	print(f'\n  {num} + {pc} = {s}\n')
	if choice == 'par':
	 	if s % 2 == 0:
	 	 	print(f'\033[32m {s} é par. Voce ganhou!\n')
	 	 	print('='*30); qt += 1
	 	else:
	 		print(f'\033[31m {s} é ímpar. Game Over!\033[m\n')
	 		break
	elif choice == 'ímpar':
	 	if s % 2 != 0:
	 		print(f'\033[32m {s} é ímpar. Voce ganhou!\n')
	 		print('='*30); qt += 1
	 	else:
	 		print(f'\033[31m {s} é par. Game Over!\033[m\n')
	 		break
print(f'\033[33m  Voce venceu {qt} vezes\033[m')	 	