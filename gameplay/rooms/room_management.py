''' 
IDEAs: 
    - Rooms are generated randomly
    - After generating a room it will be saved on the map for the character (getting back will return the same path as before)
    - Counter on directions depth (example limit of 3 rooms in each direction if connected)
    - Limited rooms (like endingRoom, safeRooms and genericRoom)
'''
import random
import os
import json
from gameplay.rooms import start_room

# Construct the relative path to data.json
saves_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'characters', 'data.json')

character_name = ''

def start(character_name_str):
    global character_name
    character_name = character_name_str
    map_dict = {}
    start_room.creation()
    print(start_room.get_room_coord())
    map_new_room('generic-room', start_room.get_room_coord())
    x = input('Did you understand?')

def map_new_room(room_name, room_coord):
    room_dict = {'name': room_name, 'coordinates': room_coord, 'adj_rooms': {'left': None, 'up': None, 'right': None, 'down': None}}
    character_data = {}

    with open(saves_file_path,'r') as saves_file:
        data = json.load(saves_file)
        character_data = data['profiles'][character_name]
        print(json.dumps(character_data))

    try:
        character_data['rooms'].update({room_name: room_dict})
    except:
        character_data['rooms'] = room_dict
    
    with open(saves_file_path, 'w') as saves_file:
        json.dump(data, saves_file, indent=4)
