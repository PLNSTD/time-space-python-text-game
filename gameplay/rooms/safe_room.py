from utils import tools
from gameplay.stats_and_inventory import character_inventory, character_stats
import json

def options(character_name):
    while True:
        print(f'You are in the safe room, here you can:')
        print('\t1 - Move')
        print('\t2 - Check Inventory')
        print('\t3 - Talk To Merchant')
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
                user_inventory = character_inventory.get_inventory(character_name)
                print(json.dumps(user_inventory))
                # IF POTIONS >= 1 print('\n1 - HEAL')
                print('\t0 - Exit Inventory')
                choice = tools.get_player_input_choice()
                if choice == 0:
                    break
                tools.prompt_clear()
        elif choice == 3:
            talk_to_merchant()
        
        tools.prompt_clear()

def talk_to_merchant():
    pass