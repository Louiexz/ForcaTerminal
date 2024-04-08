import random

class Memoria():
    def __init__(self):
        self.choice_pos = [['-'] * 6 for _ in range(3)]
    
    def shuffle_numbers(self):
        #numbers = [chr(0x1F600 + (x + 5)) for x in range(1, 10)]
        numbers = [x for x in range(1, 10)]
        list_memory = [[], [], []]

        for _ in range(9):
            number = random.choice(numbers)
            numbers.remove(number)
            pos_one = random.randint(0, 1)
            
            list_memory[pos_one].append(number)
            list_memory[pos_one + 1].append(number)
            
        return list_memory
    
    def ajust_len(self):
        list_memory = self.shuffle_numbers()
        list_len = [len(x) for x in list_memory]
        
        while min(list_len) != max(list_len):
            pos_min = list_len.index(min(list_len))
            pos_max = list_len.index(max(list_len))
            
            num = list_memory[pos_max].pop()
            list_memory[pos_min].append(num)
            
            list_len[pos_min] += 1; list_len[pos_max] -= 1
            
        return list_memory
    
    def choice_cards(self):
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
    
    def user_choice(self, cards):
        for row in self.choice_pos: print(row)
        my_choices = self.choice_cards()
    
        num_one = cards[my_choices[0]][my_choices[1]]
        num_two = cards[my_choices[2]][my_choices[3]]
        
        print("\n Números escolhidos: ", num_one, num_two)

        if num_one == num_two and my_choices[3] != my_choices[1]:
            self.choice_pos[my_choices[0]][my_choices[1]] = num_one
            self.choice_pos[my_choices[2]][my_choices[3]] = num_two

            return True
        else: return False
