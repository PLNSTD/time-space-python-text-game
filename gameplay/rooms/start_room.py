import random
from utils import tools 
from gameplay.stats_and_inventory import character_stats as main_character

coordinates = None

def creation(MAX_DEPTH):
    global coordinates
    coordinates = random_coord(MAX_DEPTH)
    print('This is the Starting Room')

def random_coord(MAX_DEPTH):
    return (random.randint(0, MAX_DEPTH - 1), random.randint(0, MAX_DEPTH - 1))

def get_room_coord():
    return coordinates

def options():
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
                # IF POTIONS >= 1 print('\n1 - HEAL')
                print('\t0 - Exit Inventory')
                choice = tools.get_player_input_choice()
                if choice == 0:
                    break
                tools.prompt_clear()
        tools.prompt_clear()