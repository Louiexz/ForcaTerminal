import os
from scripts.main.preparation import initialize_game

try: os.system('cls')
except Exception as e: os.system('clear')

initialize_game()