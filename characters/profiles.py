import os
import json

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
saves_file_path = os.path.join(current_directory, 'data.json')

def get_characters(name = 'guest_player'):
    try:
        with open(saves_file_path, 'r') as saves_file:
            print('Loading saving file...')
            print(saves_file.read())
            print('Loading Completed!')
            character_creation('Pippo')
    except FileNotFoundError:
        with open(saves_file_path, 'w') as saves_file:
            # CREATING
            print('Creating saving file...')
            # CREATE DICTIONARY WITH PROFILEs DATA
            user_data = {'profiles': {}}
            print(json.dumps(user_data))
            json.dump(user_data, saves_file, indent=4)
            print('Creation Completed!')
        character_creation(name)

def character_creation(name):
    character_profile = {'name': name, 'level': 1, 'skills': {'health': 1, 'agility': 1, 'magic': 1, 'speech': 1}}
    data_profiles = {}
    with open(saves_file_path, 'r') as saves_file:
        data_profiles = json.load(saves_file)
        print(data_profiles)
    
    character_data = {character_profile['name']: character_profile}
    data_profiles['profiles'].update(character_data)
    with open(saves_file_path, 'w') as saves_file:
        json.dump(data_profiles, saves_file, indent=4)

    