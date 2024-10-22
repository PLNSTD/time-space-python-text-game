import characters.profiles as mc
import os
import json
import time

profiles_dic = {}

def get_player_input():
    player_input = input('\nYour choice: ')

    try:
        player_input = int(player_input)
    except (ValueError, OverflowError):
        return -1
    
    return player_input

def Game():
    while True:
        print('Welcome to TimeSpace!\n\n')
        print('Press a key:\n\t1 - Start\n\t0 - Exit Game')
        user_choice = get_player_input()
        if user_choice == 1: # START
            prompt_clear()
            start()
        elif user_choice == 0: # EXIT
            prompt_clear()
            break
        prompt_clear()

def start():
    while True:
        print('Press a key:')
        print('\n\t1 - New Game')
        print('\n\t2 - Load Characters')
        print('\n\t0 - Exit')
        user_choice = get_player_input()
        if user_choice == 1: # CREATES A NEW CHARACTER
            pass
        elif user_choice == 2: # SHOW CHARACTERS
            prompt_clear()
            load_characters()
        elif user_choice == 0:
            prompt_clear()
            break
        prompt_clear()   

def load_characters():
    global profiles_dic
    profiles_dic = mc.load_profiles()
    if len(profiles_dic) == 0:
        print('No characters created... Start a New Game to create one')
        print('Returning to Main Menu')
        time.sleep(3.5)
        return
    while len(profiles_dic) > 0:
        print('Select a character\n')

        for profile in enumerate(profiles_dic):
            print(f'\n{profile[0] + 1} - Name: {profile[1]}\n\tLv: {profiles_dic[profile[1]].get('level')}')

        print('\n0 - Return to Main Menu')
        user_choice = get_player_input()
        if user_choice == 0:
            prompt_clear()
            break
        elif 0 < user_choice <= len(profiles_dic):
            profiles_list = list(profiles_dic.values())
            character_chosen = profiles_list[user_choice - 1]
            print(f'{character_chosen}')
            prompt_clear()
            character_option(character_chosen)
        prompt_clear()

def character_option(character_dic):
    global profiles_dic
    while True:
        print(f'You have chosen:\n{character_dic['name']}\nLv: {character_dic['level']}')
        print('\nPress a key:')
        print('\n\t1 - Start Game')
        print('\n\t2 - Delete Character')
        print('\n\t0 - Return to character selection')
        user_choice = get_player_input()
        if user_choice == 1: # START GAME
            prompt_clear()
            pass
        elif user_choice == 2: # DELETE THIS CHARACTER
            prompt_clear()
            profiles_dic = mc.delete_character(character_dic['name'])
            break
        elif user_choice == 0: # GO BACK
            prompt_clear()
            break
        prompt_clear()

def prompt_clear():
    os.system('cls' if os.name == 'nt' else 'clear')