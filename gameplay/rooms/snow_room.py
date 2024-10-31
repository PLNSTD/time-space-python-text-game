from gameplay.stats_and_inventory import character_inventory
from gameplay import combat
import random
from utils import tools
import time

def options(character_name):
    print('''\n\tA biting chill wraps around you
          \tas snowflakes drift through the still air.
          \tEach step crunches softly,
          \tbreaking the eerie silence of this frozen realm.''')
    print('''\n\tThe ground trembles as figures of ice rise from the snow,
          \teyes glowing with an eerie blue light.
          \t'You do not belong here,' they rumble, advancing slowly.
          \t'Leave… or be frozen in time.''')
    user_inventory = character_inventory.get_inventory(character_name)
    mob_spawned_quantity = random.randint(1,4)
    enemies = {'name': 'Ice Golem', 'quantity': mob_spawned_quantity,'attack': 2, 'weaknesses': ['fire'], 'resistances': ['ice', 'physical'], 'health': [40] * mob_spawned_quantity, 'drops_key': False}
    if user_inventory.get('key_seed') == 'snow':
        enemies['drops_key'] = True
    print(f'\n\t{mob_spawned_quantity} {enemies['name']}{'s' if mob_spawned_quantity > 1 else ''} spawned!')
    time.sleep(2)

    while True:
        for enemy_num in range(1, mob_spawned_quantity+1):
            enemy_name = enemies["name"]
            enemy_hp = enemies['health'][enemy_num-1]
            print(f'\n{enemy_name}:{enemy_hp}hp')
        print(f'\nPress a key:')
        print(f'\n\t1 - Fight')
        print(f'\n\t0 - Escape')
        choice = tools.get_player_input_choice()
        if choice == 1:
            combat.fight(character_name, enemies)
            break
        elif choice == 0:
            escape_chances = random.randint(1,10)
            if escape_chances > 2:
                print(f'You managed to escape the {enemies['name']}{'s' if mob_spawned_quantity > 1 else ''}!')
                time.sleep(2)
                break
            print('\nYou could not escape the enemies\n')
            combat.fight(character_name, enemies)
            break
        tools.prompt_clear()