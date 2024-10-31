from gameplay.stats_and_inventory import character_stats, character_inventory
from characters import profiles
from utils import tools
import random
import time

move_set = ['physical', 'fire', 'ice', 'light']
user_name = ''

def fight(character_name, enemies):
    global user_name
    global move_set
    user_name = character_name
    user_stats = character_stats.get_stats(user_name)
    tot_enemies = enemies['quantity']
    while enemies['quantity'] > 0:
        user_stats = character_stats.get_stats(user_name)
        character_stats.print_stats(user_stats)
        print_enemies(enemies)
        print('\n\t0 - To escape')
        print('\nWhich enemy do you want to attack?')
        choice = tools.get_player_input_choice()
        if choice > enemies['quantity'] or choice < 1:
            continue
        elif choice == 0:
            escape_chances = random.randint(1,10)
            if escape_chances > 2:
                print(f'You managed to escape the {enemies['name']}{'s' if enemies['quantity'] > 1 else ''}!')
                return
            print('You could not escape!')
        enemy_target = choice
        while True:
            tools.prompt_clear()
            print_enemies(enemies)
            print(f'You chose {enemy_target + 1} - {enemies['name']} : {enemies['health'][enemy_target - 1]}')
            print(f'\nChoose your move:')
            for num, attack in enumerate(move_set):
                print(f'\t{num + 1} - {attack.capitalize()} Card')
            choice = tools.get_player_input_choice()
            if choice < 1 or choice > len(move_set):
                continue
            print(f'You drew the {move_set[choice - 1]} card!')
            multiplier = 1
            if move_set[choice - 1] in enemies['weaknesses']:
                print('The move is super effective!')
                multiplier = 4
            elif move_set[choice - 1] in enemies['resistances']:
                print('The enemy resisted your attack!')
                multiplier = 0.5
            damage_dealt = user_stats['attack'] * multiplier
            print(f'{damage_dealt} Damage dealt!')
            time.sleep(2)
            enemies['health'][enemy_target - 1] = enemies['health'][enemy_target - 1] - damage_dealt
            if enemies['health'][enemy_target - 1] <= 0:
                enemies['health'].pop(enemy_target - 1)
                enemies['quantity'] -= 1
                print(f'You have defeated 1 {enemies['name']}')
            break
        
        print('The enemies attack you: ')
        damage_received = 0
        for enemy in range(1, enemies['quantity'] + 1):
            if random.randint(1, tot_enemies * 5) > tot_enemies * 3:
                damage_received += enemies['attack']
            else:
                print('You avoided one attack')
        if damage_received > 0:
            character_stats.set_health(user_name, -damage_received)
        print(f'\nYou received {damage_received} total damage')
        if character_stats.get_stats(character_name)['health'] <= 0:
            print('Game Over... You died!')
            profiles.delete_character(user_name)
            time.sleep(3)
            exit()
    drops(tot_enemies, True if enemies['drops_key'] else False)
    tools.prompt_clear()

def print_enemies(enemies):
    for enemy_num in range(enemies['quantity']):
        enemy_name = enemies["name"]
        enemy_hp = enemies['health'][enemy_num]
        print(f'\n\t{enemy_num+1} - {enemy_name}:{enemy_hp}hp')

def drops(tot_enemies, key=False):
    global user_name
    user_inventory = character_inventory.get_inventory(user_name)
    possible_items = ['gold']
    drops = {}
    drops['gold'] = 2 * tot_enemies
    if key:
        if random.randint(1, tot_enemies * 5) <= tot_enemies:
            drops['ending_key'] = 1
    if random.randint(1, 10) <= 2:
        drops['potion'] = 1
    for item_drop in drops:
        character_inventory.add_item(user_name, item_drop, drops[item_drop])
        print(f'You got {drops[item_drop]}x {item_drop.capitalize()}!')
    time.sleep(4)