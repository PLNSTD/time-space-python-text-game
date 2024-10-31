from gameplay.stats_and_inventory import character_inventory
from gameplay import combat
import random
from utils import tools
import time

def options(character_name):
    print("\tYou step into the cave, and a damp chill settles over you.\n\t"
      "Shadows twist and crawl along the rough stone walls,\n\t"
      "while distant echoes hint at unseen depths.\n\t"
      "The air is thick and still, broken only by the faint drip of water somewhere in the darkness.")
    print("\n\tBones clatter in the darkness, assembling into twisted forms.\n"
      "\tA hollow voice echoes through the shadows:\n"
      "\t'The dead do not rest... and neither shall you.'\n"
      "\tSkeletons rise, their empty eyes fixed upon you, ready to attack.")
    user_inventory = character_inventory.get_inventory(character_name)
    mob_spawned_quantity = random.randint(1,4)
    enemies = {'name': 'Skeleton', 'quantity': mob_spawned_quantity,'attack': 1, 'weaknesses': ['light'], 'resistances': ['physical'], 'health': [30] * mob_spawned_quantity, 'drops_key': False}
    if user_inventory.get('key_seed') == 'cave':
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