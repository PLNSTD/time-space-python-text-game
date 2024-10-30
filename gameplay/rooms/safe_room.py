from utils import tools
from gameplay.stats_and_inventory import character_inventory, character_stats
import json
import time

user_inventory = {}
character_name = ''
snow_room_riddle = '\n\tSeek the chill where the frost does bite,\n\tA land of white under pale moonlight.\n\tWhere silence reigns and warmth is rare,\n\tThe key may lie in frozen air'
cave_room_riddle = '\n\tIf shadows call and echoes roam,\n\tGo where darkness makes its home.\n\tDeep within the earth’s embrace,\n\tThe key might hide in a stony place.'
sand_room_riddle = '\n\tWhere sun meets ground and grains do flow,\n\tIn endless dunes the warm winds blow.\n\tAmidst the heat and golden land,\n\tThe key may lie beneath the sand.'

def options(user_name):
    global character_inventory
    global character_name
    character_name = user_name
    user_inventory = character_inventory.get_inventory(character_name)

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
                user_stats = character_stats.get_stats(character_name)
                character_stats.print_stats(user_stats)
                user_inventory = character_inventory.get_inventory(character_name)
                character_inventory.print_inventory(user_inventory)
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
            talk_to_merchant()
        
        tools.prompt_clear()

def talk_to_merchant():
    global user_inventory
    global character_name
    ending_advice = False
    print('\n\t***Hello Adventurer! I am the Great Merchant***\n')
    while True:
        print('\t1 - Take a look to the Merch')
        if 'ending_note' in user_inventory:
            ending_advice = True
            print('\t2 - Ask for the Ending Key')
        print('\t0 - Move away')
        choice = tools.get_player_input_choice()
        if choice == 1:
            tools.prompt_clear()
            show_merch()
        elif choice == 2 and ending_advice:
            print("How do you know about the key?")
            print("Ah... very few know of such secrets. This key is indeed a powerful tool—a means to escape this twisted time-space dungeon.")
            print("But knowledge like that doesn’t come cheap, you see.")
            print("We merchants... we don’t simply *give away* wisdom. Pay my price, and perhaps I might recall rumors of three possible locations...")
            print("Yes, yes... Three mysterious areas. Who knows what might lurk within?")
            print("But only with payment can I guide you closer to the key. Without it, I fear my lips are sealed!")
            while True:
                if 'gold' in user_inventory:
                    if user_inventory.get('gold') >= 50: 
                        print('Would you like to pay 50 Gold to know more?')
                        print('\t1 - Pay the gold')
                        print('\t2 - Forget it')
                        choice = tools.get_player_input_choice()
                        if choice == 1:
                            character_inventory.add_item(character_name, 'gold', -50)
                            user_inventory = character_inventory.get_inventory(character_name)
                            # Advice based on room
                            room_seed = user_inventory['key_seed']
                            if room_seed == 'snow':
                                print(sand_room_riddle)
                            elif room_seed == 'cave':
                                print(cave_room_riddle)
                            elif room_seed == 'sand':
                                print(sand_room_riddle)
                        elif choice == 2:
                            break
                    else:
                        print("\n\tIt appears you lack the necessary 50 gold to persuade the Merchant")
                        print("\tPerhaps you should gather more gold and try again.")
                        time.sleep(2)
                        break
        elif choice == 0:
            return

def show_merch():
    merch = {'Potion': 10, 'Map': 30}
    user_inventory = character_inventory.get_inventory(character_name)
    while True:
        print('You will find some good stuff in here:')
        for item_id, item in enumerate(merch):
            print(f'\t{item_id + 1} - {item}\n\t\tPrice: {merch[item]} Gold')
        print(f'\t0 - Not now.')
        print('\nTell me if you find something interesting')
        choice = tools.get_player_input_choice()
        if choice == 1:
            if user_inventory.get('gold', 0) >= merch['Potion']:
                character_inventory.add_item(character_name, 'gold', -merch['Potion'])
                character_inventory.add_item(character_name, 'potion', 1)
                user_inventory = character_inventory.get_inventory(character_name)
            else:
                print('\tI am sorry fellow Adventurer but you do not have enough!')
                print("\tPerhaps you should gather more gold and try again.")
            time.sleep(3)
        elif choice == 2:
            if user_inventory.get('gold', 0) >= merch['Map']:
                character_inventory.add_item(character_name, 'gold', -merch['Map'])
                character_inventory.add_item(character_name, 'map', 1)
                user_inventory = character_inventory.get_inventory(character_name)
            else:
                print('\tI am sorry fellow Adventurer but you do not have enough!')
                print("\tPerhaps you should gather more gold and try again.")
            time.sleep(3)
        elif choice == 0:
            tools.prompt_clear()
            break
        tools.prompt_clear()