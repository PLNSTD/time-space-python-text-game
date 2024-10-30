from gameplay.stats_and_inventory import character_inventory
from utils import tools
import random
import time

def options(character_name):
    user_inventory = character_inventory.get_inventory(character_name)
    note_read = False
    while 'ending_key' in user_inventory:
        print('\n\tIt looks like you have the key, now you can escape from the dungeon!')
        print('\n\t1 - Get Out the Dungeon')
        print('\n\t0 - Keep Exploring')
        choice = tools.get_player_input_choice()
        if choice == 1:
            exit()
        elif choice == 0:
            return
    print('You notice a strange note on one of the walls of the room:')
    while True:
        print('\n\t1 - Read Note')
        print('\n\t0 - Keep Exploring')
        choice = tools.get_player_input_choice()
        if choice == 1:
            print('\n\tNote:')
            print('\n\tYou did not found the key yet!\n\tAsk to the Merchant in any safe room for guidance')
            note_read = True
            time.sleep(3)
        elif choice == 0:
            break
        tools.prompt_clear()
    if note_read and user_inventory.get('ending_note', None) == None:
        character_inventory.add_item(character_name, 'ending_note', True)