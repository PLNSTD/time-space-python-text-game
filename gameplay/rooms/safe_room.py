from utils import tools
from gameplay.stats_and_inventory import character_inventory, character_stats
import json
import time

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
                character_stats.print_stats(character_name)
                user_inventory = character_inventory.get_inventory(character_name)
                character_inventory.print_inventory()
                heal_enabled = False
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
        elif choice == 3:
            character_inventory.add_item(character_name, 'potion')
            talk_to_merchant()
        
        tools.prompt_clear()

def talk_to_merchant():
    print('***Hello Adventurer! I am the Great Merchant***')
    # options to buy