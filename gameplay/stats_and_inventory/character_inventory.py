import os
import json

saves_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'characters', 'data.json')

def get_inventory(character_name):
    data = {}
    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)
    
    character_info = data['profiles'].get(character_name)
    character_inventory = character_info.get('inventory', {})

    return character_inventory

def add_item(character_name, item_name, quantity=1):
    data = {}
    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)

    character_info = data['profiles'].get(character_name)

    if character_info.get('inventory', None) == None:
        character_info['inventory'] = {item_name: quantity}
    else:
        character_info['inventory'][item_name] = character_info['inventory'].get(item_name, 0) + quantity
    
    with open(saves_file_path, 'w') as saves_file:
        json.dump(data, saves_file, indent=4)
