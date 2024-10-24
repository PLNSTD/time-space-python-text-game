import os

def get_player_input_choice():
    player_input = input('\nYour choice: ')

    try:
        player_input = int(player_input)
    except (ValueError, OverflowError):
        return -1
    
    return player_input

def prompt_clear():
    os.system('cls' if os.name == 'nt' else 'clear')