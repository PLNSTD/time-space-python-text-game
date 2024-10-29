import os
import time
import json
from utils.custom_exceptions import ExitWithBlock

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
saves_file_path = os.path.join(current_directory, 'data.json')

# GET EVERY CHARACTER
def load_profiles():
    profiles_dict = {}
    # CHECK FILE EXISTANCE AND CREATES IT IF NOT FOUND
    try:
        with open(saves_file_path, 'r') as saves_file:
            data = json.load(saves_file)
            profiles_dict = data['profiles']
    except FileNotFoundError:
        with open(saves_file_path, 'w') as saves_file:
            # CREATING
            # CREATE DICTIONARY WITH PROFILEs DATA
            user_data = {'profiles': {}}
            json.dump(user_data, saves_file, indent=4)
        character_creation('Jason')

    return profiles_dict

# GET CHARACTER IF EXISTS (CAN BE USED TO AVOID DUPLICATES)
def get_character(name):
    result = False
    character_profile = {}
    try:
        with open(saves_file_path, 'r') as saves_file:
            data = json.load(saves_file)
            print(json.dumps(data))
            if len(data['profiles']) == 0:
                raise ExitWithBlock
            if name in data['profiles'].keys():
                character_profile = data['profiles'][name]
                result = True
    except ExitWithBlock: # No profiles in profile
        print('No profiles')

    return [result, character_profile]

# CREATES A CHARACTER BY NAME (NO CHECKING FOR DUPLICATES)
def character_creation(name):
    name = name.lower()
    character_profile = {'name': name, 'level': 1, 'skills': {'health': 1, 'agility': 1, 'magic': 1, 'speech': 1}, 'stats': {'health': 25, 'mana': 10, 'xp': 0, 'attack': 5}}
    data_profiles = {}
    with open(saves_file_path, 'r') as saves_file:
        data_profiles = json.load(saves_file)

    character_data = {character_profile['name']: character_profile}
    data_profiles['profiles'].update(character_data)
    with open(saves_file_path, 'w') as saves_file:
        json.dump(data_profiles, saves_file, indent=4)

    return character_profile

# DELETES A CHARACTER BY NAME
def delete_character(name):
    print(f'\nDeleting Character: {name}...')
    data = {}
    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)
        
    print(data)
    if name in data['profiles']:
        del data['profiles'][name]
    print(f'UPDATED characters list: {data}')
    with open(saves_file_path, 'w') as saves_file:
        json.dump(data, saves_file, indent=4)
    time.sleep(5)
    return data['profiles']