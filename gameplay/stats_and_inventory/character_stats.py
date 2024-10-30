import os
import json

saves_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'characters', 'data.json')

def print_stats(user_stats):
    print('\nStats:')
    for stat in user_stats:
        print(f'\t{stat}: {user_stats[stat]}')

def get_stats(character_name):
    data = {}
    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)
    character_info = data['profiles'].get(character_name)
    return character_info['stats']

def set_health(character_name, modified_health):
    data = {}
    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)
        
    character_info = data['profiles'].get(character_name)
    character_info['stats']['health'] = character_info['stats']['health'] + modified_health

    with open(saves_file_path, 'w') as saves_file:
        json.dump(data, saves_file, indent=4)

def set_mana(character_name, modified_mana):
    data = {}
    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)
        
    character_info = data['profiles'].get(character_name)
    character_info['stats']['mana'] = character_info['stats']['mana'] + modified_mana

    with open(saves_file_path, 'w') as saves_file:
        json.dump(data, saves_file, indent=4)