from gameplay.stats_and_inventory import character_inventory
from gameplay import combat
import random
from utils import tools
import time

def options(character_name):
    print("\tYou step into an endless sea of sand, heat waves rippling across the horizon.\n"
      "\tThe sun blazes overhead, casting harsh shadows that shift with the wind.\n"
      "\tEach step sinks into the golden dunes, and the air is thick with silence,\n"
      "\tbroken only by the occasional whisper of the desert breeze.")
    print("\n\tFrom the shadows, figures emerge with wicked grins and glinting blades.\n"
      "\tA leader steps forward, sneering:\n"
      "\t'Well, well, what do we have here?\n"
      "\tA wandering soul in our territory?'\n"
      "\t'Hand over your valuables, and you might leave with your skin intact!'")
    user_inventory = character_inventory.get_inventory(character_name)
    mob_spawned_quantity = random.randint(1,4)
    enemies = {'name': 'Bandit', 'quantity': mob_spawned_quantity,'attack': 3, 'weaknesses': ['fire'], 'resistances': ['light'], 'health': [30] * mob_spawned_quantity, 'drops_key': False}
    if user_inventory.get('key_seed') == 'sand':
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