import random
from utils import tools 
import json
import time
from gameplay.stats_and_inventory import character_stats, character_inventory

coordinates = None

def creation(MAX_DEPTH):
    global coordinates
    coordinates = random_coord(MAX_DEPTH)
    print('This is the Starting Room')

def random_coord(MAX_DEPTH):
    return (random.randint(0, MAX_DEPTH - 1), random.randint(0, MAX_DEPTH - 1))

def get_room_coord():
    return coordinates

def options(character_name):
    while True:
        print(f'You are in the starting room, here you can:')
        print('\t1 - Move')
        print('\t2 - Check Inventory')
        print('\t0 - Exit Game')
        choice = tools.get_player_input_choice()
        tools.prompt_clear()
        if choice == 0:
            exit()
        elif choice == 1: # Move
            return 1
        elif choice == 2: # Inventory and stats
            while True:
                print(f"This is your inventory and stats")
                # Show Inventory and Stats
                user_stats = character_stats.get_stats(character_name)
                character_stats.print_stats(user_stats)
                user_inventory = character_inventory.get_inventory(character_name)
                character_inventory.print_inventory(user_inventory)
                heal_enabled = False
                if user_inventory.get('key', 0) > 0:
                    print('You have the key, look for the ending room!')
                if user_inventory.get('potion', 0) > 0:
                    heal_enabled = True
                    print('\t1 - HEAL')
                print('\t0 - Exit Inventory')
                choice = tools.get_player_input_choice()
                if choice == 0:
                    break
                elif choice == 1 and heal_enabled:
                    character_inventory.add_item(character_name, 'potion', -1)
                    character_stats.set_health(character_name, +5)
                    print('You used a potion! +5 hp')
                    time.sleep(2)
                tools.prompt_clear()
        tools.prompt_clear()