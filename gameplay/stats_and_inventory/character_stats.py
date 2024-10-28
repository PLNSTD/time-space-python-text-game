import os
import json

saves_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'characters', 'data.json')


def get_health(character_name):
    data = {}
    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)
    character_info = data['profiles'].get(character_name)
    health = character_info['stats'].get('health')
    return health

def set_health(character_info):
    data = {}
    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)
        
    data.update(character_info)

    with open(saves_file_path, 'w') as saves_file:
        json.dump(data, saves_file, indent=4)