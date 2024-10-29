import os
import json
import time

saves_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'characters', 'data.json')

def print_inventory(character_name):
    user_inventory = get_inventory(character_name)
    print('\nInventory:')
    for item in user_inventory:
        if item == 'ending_note':
            continue
        print(f"\n\tItem: {item.capitalize()}")
        print(f"\n\tQt: {user_inventory[item]}")

def get_inventory(character_name):
    data = {}
    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)
    
    character_info = data['profiles'].get(character_name)
    user_inventory = character_info.get('inventory', {})

    return user_inventory

def add_item(character_name, item_name, quantity=1):
    item_name = item_name.lower()
    data = {}
    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)

    character_info = data['profiles'].get(character_name)

    if character_info.get('inventory', None) == None:
        character_info['inventory'] = {item_name: quantity}
    else:
        if item_name is not 'ending_note':
            character_info['inventory'][item_name] = character_info['inventory'].get(item_name, 0) + quantity
        else:
            character_info['inventory'][item_name] = quantity

    with open(saves_file_path, 'w') as saves_file:
        json.dump(data, saves_file, indent=4)
    
    print(f'\n\tItem: {item_name} {'+' if quantity > 0 else '-'} {quantity}')