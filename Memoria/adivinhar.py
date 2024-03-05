import random

class adivinharJogo():
    def __init__(self):
        self.choicePos = [['-'] * 6 for _ in range(3)]
    
    def shuffleNumbers(self):
        #numbers = [chr(0x1F600 + (x + 5)) for x in range(1, 10)]
        numbers = [x for x in range(1, 10)]
        listMemory = [[], [], []]

        for _ in range(9):
            number = random.choice(numbers)
            numbers.remove(number)
            posOne = random.randint(0, 1)
            
            listMemory[posOne].append(number)
            listMemory[posOne + 1].append(number)
            
        return listMemory
    
    def ajustLen(self):
        listMemory = self.shuffleNumbers()
        listLen = [len(x) for x in listMemory]
        
        while min(listLen) != max(listLen):
            posMin = listLen.index(min(listLen))
            posMax = listLen.index(max(listLen))
            
            num = listMemory[posMax].pop()
            listMemory[posMin].append(num)
            
            listLen[posMin] += 1; listLen[posMax] -= 1
            
        return listMemory
    
    def choiceCards(self):
        choices = []
        
        for x in range(2):    
            row, col  = -1, -1
            
            while not (0 <= col <= 5) or not (0 <= row <= 2):
                try:
                    col = int(input(f"\n Digite {x + 1}° coluna: (1 até 6) ")) - 1
                    row = int(input(f" Digite {x + 1}° linha: (1 até 3) ")) - 1
                    if not (0 <= col <= 5) or not (0 <= row <= 2): print(" Número inválido.")
                    
                except ValueError: print(" Digite apenas números válidos.")
            choices.extend([row, col])
            
        return choices
    
    def userChoice(self, cards):
        for row in self.choicePos: print(row)
        myChoices = self.choiceCards()
    
        numOne = cards[myChoices[0]][myChoices[1]]
        numTwo = cards[myChoices[2]][myChoices[3]]
        
        print("Números escolhidos: ", numOne, numTwo)

        if numOne == numTwo and myChoices[3] != myChoices[1]:
            self.choicePos[myChoices[0]][myChoices[1]] = numOne
            self.choicePos[myChoices[2]][myChoices[3]] = numTwo

            return True
        else: return False
