from time import sleep

# Introdução a história
print('\033[37m Vamos cavaleiro, venha lutar ao meu lado contra o dragão que está atacando nosso reino!\n')
nome = input(' Diga-me seu nome primeiro: ').strip().capitalize()
print(f' Certo {nome}, vamos a luta.\n')
sleep(0.5)

# Vida do Dragão
vd = 1800

# Ataques do Dragão
bc =  200; atkd = 100

# Defesa do Dragão
dfd = 60

# Vida do Player
vp = 100

# Ataques do Player
atkl = 250; atkp = 400; atkf = 850

# Defesa do Player
dfp = 70

# Poção de cura
pc = 20

# Introdução a luta
print(' A vida do dragão é:', vd)
print(' A sua vida é:', vp); sleep(1.0)

# Escolha 1
print(f'\n Seus ataques são: leve duplo [1] e pesado [2]')
escolha = input(' Escolha um ataque:' )
if escolha == '1' :
	dd = atkl * 2 - dfd; vd -= dd
	print(f'\n ~{nome} ataca ~')
elif escolha == '2' :
	dd = atkp - dfd; vd -= dd
	print(f'\n ~{nome} ataca ~')
else:
	print('\n Nenhuma opção escolhida')
sleep(1.1)
print(f' A vida do dragão é {vd}'); sleep(0.5)
pd = atkd - dfp; vp -= pd
print('\n ~ Dragão ataca ~'); sleep(0.5)
print(f' Sua vida cai para: {vp}'); sleep(1.0)

# Escolha 2
print('\n [1] ataque leve e [2] ataque pesado duplo')
escolha2 = input(' Escolha um ataque: ')
if escolha2 == '1' :
	dd = atkl - dfd; vd -= dd
	print(f'\n ~{nome} acerta um ataque leve!~')
	print(f' ~A vida do dragão desceu para: {vd}~')
elif escolha2 == '2' :
	dd = (atkp * 2) - dfd; vd -= dd
	print(f'\n ~{nome} conseguiu acertas o golpe duplo! Agora a vida dele é: {vd}!')
else:
	print('\n Nenhuma opção escolhida')
sleep(1.1); vp = vp - pd * 2
print('\n ~O Dragão da um ataque duplo~')
sleep(1.1)
print(f' ~Sua vida cai para: {vp}')
sleep(1.1) 
if vp <= 30:
	print(f'\n\033[31m Você está à beira da morte\033[m, tome uma \033[32mpoção de cura\033[m\033[37m e continue!')
	vp = vp + pc
	print(f'\n Você tem: {vp} de vida, você terá que dar o golpe final agora!'); sleep(1.3) 

# Escolha final
print('\n Ataques possíveis: [1] Ataque pesado, [2] Ataque flamejante')
escolha3 = input(' Escolha um ataque: ')
if escolha3 == '1' :
	dd = atkp - dfd; vd -= dd
	print('\n Escolheu ataque pesado!')
elif escolha3 == '2' :
	dd = atkf - dfd; vd -= dd
	print('\n Wow! Você usou um ataque especial')
else:
	print('\n Nenhuma opção escolhida')

# Final
print(' A vida do dragão é:',vd)
if vd <= 0:
	print(f'\n ~{nome} corta a cabeça do dragão com um golpe final~')
	sleep(1.5)
	print(f'\n \033[32mVocê venceu {nome}!\033[m Agora o reino está a salvo, graças a você!')
elif vd > 0:
	print('\n Sua vida é', vp)
	dfp2 = vd + dfp; vd = dfp2 - bc
	sleep(1.0); print(' ~O dragão te engole~')
	sleep(1.5)
	print('\n\033[31m Você perdeu!\033[m Boa sorte na próxima.')