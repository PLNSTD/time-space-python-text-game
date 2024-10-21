import os
import json

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
saves_file_path = os.path.join(current_directory, 'data.json')

# GET EVERY CHARACTER
def load_profiles():
    profiles_dict = {}

    # CHECK FILE EXISTANCE AND CREATES IT IF NOT FOUND
    try:
        with open(saves_file_path, 'r') as saves_file:
            profiles_dict = json.load(saves_file)
            profiles_dict = profiles_dict['profiles']
    except FileNotFoundError:
        with open(saves_file_path, 'w') as saves_file:
            # CREATING
            # CREATE DICTIONARY WITH PROFILEs DATA
            user_data = {'profiles': {}}
            json.dump(user_data, saves_file, indent=4)

    return profiles_dict

# GET CHARACTER IF EXISTS (CAN BE USED TO AVOID DUPLICATES)
def get_character(name):
    result = False
    character_profile = {}
    with open(saves_file_path, 'r') as saves_file:
        profiles_dict = json.load(saves_file)
        if name in profiles_dict['profiles'].keys():
            character_profile = profiles_dict['profiles'][name]
            result = True

    return [result, character_profile]

# CREATES A CHARACTER BY NAME (NO CHECKING FOR DUPLICATES)
def character_creation(name):
    character_profile = {'name': name, 'level': 1, 'skills': {'health': 1, 'agility': 1, 'magic': 1, 'speech': 1}}
    data_profiles = {}
    with open(saves_file_path, 'r') as saves_file:
        data_profiles = json.load(saves_file)

    character_data = {character_profile['name']: character_profile}
    data_profiles['profiles'].update(character_data)
    with open(saves_file_path, 'w') as saves_file:
        json.dump(data_profiles, saves_file, indent=4)

    return character_profile
    