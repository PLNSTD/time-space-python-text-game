import characters.profiles as mc
import os
import json

def Game():
    prompt_clear()
    while True:
        print('Welcome to TimeSpace!\n\n')
        print('Press a key:\n\t1 - Start\n\t0 - Exit Game')
        user_choice = int(input('Key: '))
        if user_choice == 1: # START
            start()
        elif user_choice == 0: # EXIT
            prompt_clear()
            break
        else:
            prompt_clear()

def start():
    while True:
        prompt_clear()
        print('Press a key:')
        print('\n\t1 - New Game')
        print('\n\t2 - Load Characters')
        print('\n\t0 - Exit')
        user_choice = int(input('Your choice: '))
        if user_choice == 2: # SHOW CHARACTERS
            prompt_clear()
            load_characters()
        elif user_choice == 0:
            prompt_clear()
            break   

def load_characters():
    profiles_dic = mc.load_profiles()
    while True:
        for profile in enumerate(profiles_dic):
            print(f'\n{profile[0] + 1} - Name: {profile[1]}\n\tLv: {profiles_dic[profile[1]].get('level')}')
        print('\n0 - Return to Main Menu')
        user_choice = int(input('\nYour choice: '))
        if user_choice == 0:
            prompt_clear()
            break
        elif 0 < user_choice - 1 < len(profiles_dic):
            profiles_list = list(profiles_dic.values())
            character_chosen = profiles_list[user_choice - 1]
            print(f'{character_chosen}')
            character_option(character_chosen)
        else:
            prompt_clear()

def character_option(character_dic):
    pass

def prompt_clear():
    os.system('cls' if os.name == 'nt' else 'clear')