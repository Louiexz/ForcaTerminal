import os
from random import choice

class forca:
    def __init__(self):
        paises = ['Alemanha', 'Austrália', 'Canadá', 'Estados Unidos', 'França', 'Itália', 'Reino Unido', 'África do Sul', 'Arábia Saudita', 'Argentina', 'Brasil', 'Coreia do Sul', 'Indonésia', 'México', 'Rússia', 'Turquia']
        comidas = ['Doce de batata', 'Churrasco', 'Tapioca', 'Feijão tropeiro', 'Arroz carreteiro', 'Paçoca', 'Pato no tucupi', 'Maniçoba', 'Baião-de-dois', 'Acarajé', 'Pamonha', 'Dobradinha', 'Rapadura', 'Farofa-de-içá', 'Barreado', 'Pastel', 'Palmito', 'Camarão na moranga', 'Doce de abóbora', 'Feijoada', 'feijão']
        objetos = ['Abajur', 'Cabide', 'Cadeira', 'Caneca', 'Cobertor', 'Colchao', 'Colher', 'Computador', 'Edredom', 'Escrivaninha', 'Esfregao', 'Espelho', 'Fronha', 'Prateleira', 'Quadro', 'Relógio', 'Sabonete', 'Toalha', 'Vassoura', 'Xícara']
        roupas = ['chinelo', 'sandalia', 'sapatilha', 'sapatenis', 'alpagarta', 'pantufa', 'chapeu', 'oculos', 'brinco', 'cachecol', 'pulseira', 'gravata', 'tornozeleira', 'alianca', 'camisa', 'camiseta', 'jaqueta', 'bermuda', 'camisola', 'calcinha', 'casaco', 'paleto', 'pijama', 'vestido', 'colete', 'biquini']
        
        self.myTitles = [paises, comidas, objetos, roupas]
    
    def choiceTitle(self, title):
    	titles = [["paises", "pais"], ["comidas", "comida"], ["objetos", "objeto"], ["roupas", "roupa"]]
    	
    	for x in range(3):
    	   if title in titles[x]:
    	   	 theWord = choice(self.myTitles[x])
    	   	 self.myTitles[x].remove(theWord)
    	   	 break
    	   else:
    	           print(" Tema não encontrado.")
    	           theWord = "error"

    	return theWord.upper()


    def setGame(self, title):
    	while True:
    		letterCorrect, letterSorted = [], []
    		word = self.choiceTitle(title)
    		chance = 5
    		
    		if word == 'ERROR': break
    
    		print('\n\n A palavra é:', end= ' ')
    		certas = ['_' for c in word]

    		for pos, valor in enumerate(certas):
    			print(valor, end= ' ')
		
    		# tentativas
    		if len(word) <= 7: chance = len(word) - 2
			
    		while chance != 0:
    			caractere = input('\n\033[37m Digite uma letra: ').upper().strip()
    			
    			if caractere in letterSorted: print('\n\033[31m Essa letra já foi sorteada\033[m')
    			elif caractere in 'BCDFGHJKLMNPQRSTVWXYZAEIOU':
    				if caractere in word:
    					for pos, value in enumerate(word):
    						if value == caractere:
    							certas[pos] = caractere
				
    				chance -= 1
    				letterSorted.append(caractere)
				
    				for pos, value in enumerate(certas):
    					print(' ',value, end= '')
				
    				print('\n\033[37m Letras que já foram sorteadas: \n\033[31m', letterSorted)
    				print('  Vezes restantes', chance)
		
    		endTry = input('\n\033[33m Qual a palavra? ').strip().upper()
		
    		if endTry == word: print('\n\033[32m Voce acertou a palavra!!')
    		else: print(f'\n A palavra era: {word.title()}')
		
    		endChoice = input('\n\033[m Deseja continuar? [S/N] ').strip().lower()
		
    		if endChoice == 'n': break
   		 os.system('cls')
	
    def playGame(self):
    	print('\033[37m\tJogo da Forca\n Temas: Países, Comidas, Objetos, Roupas\n')
    	title = input(' Qual tema voce deseja? ').strip().lower()
    	
    	self.setGame(title)
