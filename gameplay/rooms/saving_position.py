import os
import json

saves_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'characters', 'data.json')

def save_progress(character_name, room_info, rooms_map, visited_map):
    data = {}

    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)
    
    character_info = data['profiles'].get(character_name)
    character_info['rooms_map'] = rooms_map
    character_info['position'] = room_info
    character_info['visited_map'] = visited_map

    with open(saves_file_path, 'w') as saves_file:
        json.dump(data, saves_file)

def load_progress(character_name):
    data = {}

    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)

    character_info = data['profiles'].get(character_name)
    position = character_info['position']
    rooms_map = character_info['rooms_map']
    visited_map = character_info['visited_map']

    return [character_info, position, rooms_map, visited_map]