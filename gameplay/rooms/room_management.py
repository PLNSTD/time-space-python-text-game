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
MAX_DEPTH = 5
character_name = ''
room_seeds_available = {'safe': 2, 'ending': 1, 'general': {'tot': 21, 'snow': 2, 'sand': 2, 'cave': 2, 'empty': 15}}
rooms_map = [[None for _ in range(MAX_DEPTH)] for _ in range(MAX_DEPTH)]
visited_rooms_map = [[None for _ in range(MAX_DEPTH)] for _ in range(MAX_DEPTH)] # USED TO BE SHOWN TO THE USER

def start(character_name_str):
    global character_name
    character_name = character_name_str
    map_dict = {}
    start_room.creation(MAX_DEPTH)
    print(start_room.get_room_coord())
    create_rooms_map(start_room.get_room_coord())
    x = input('Did you understand?')

def create_rooms_map(coord):
    global rooms_map
    data = None
    for row in range(MAX_DEPTH):
        for col in range(MAX_DEPTH):
            if row == coord[0] and col == coord[1]:
                print('I DIDNT COME')
                rooms_map[row][col] = 'start'
                continue
            rooms_map[row][col] = get_seed()
    
    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)
    
    character_data = data['profiles'][character_name]
    character_data['rooms_map'] = rooms_map

    with open(saves_file_path, 'w') as saves_file:
        json.dump(data, saves_file, indent=4)
            
def change_room(coord_tuple):
    row, col = coord_tuple

    ###### IMPORTANT: Change from -2 to 0 and from +2 to 4 because index changed in the map
    if row == -2 and col == -2: # Top-left
        pass
    elif row == -2 and col == 2: # Top-right
        pass
    elif row == 2 and col == -2: # Bot-left
        pass
    elif row == 2 and col == 2: # Bot-right
        pass

def get_seed():
    excluded_seeds = []
    while True:
        random_seed = random.randint(1, 3)
        if random_seed in excluded_seeds:
            continue
        if random_seed == 1:
            if room_seeds_available['safe'] > 0:
                room_seeds_available['safe'] -= 1
                return 'safe'
        elif random_seed == 2:
            if room_seeds_available['ending'] > 0:
                room_seeds_available['ending'] -= 1
                return 'ending'
        elif random_seed == 3:
            if room_seeds_available['general']['tot'] > 0:
                excluded_general_seeds = []
                while True:
                    random_general_seed = random.randint(1,21)
                    if random_general_seed in excluded_general_seeds:
                        continue
                    if random_general_seed == 1 and room_seeds_available['general']['snow'] > 0:
                        room_seeds_available['general']['snow'] -= 1
                        room_seeds_available['general']['tot'] -= 1
                        return 'snow'
                    elif random_general_seed == 2 and room_seeds_available['general']['sand'] > 0:
                        room_seeds_available['general']['sand'] -= 1
                        room_seeds_available['general']['tot'] -= 1
                        return 'sand'
                    elif random_general_seed == 3 and room_seeds_available['general']['cave'] > 0:
                        room_seeds_available['general']['cave'] -= 1
                        room_seeds_available['general']['tot'] -= 1
                        return 'cave'
                    elif room_seeds_available['general']['empty'] > 0:
                        room_seeds_available['general']['empty'] -= 1
                        room_seeds_available['general']['tot'] -= 1
                        return 'empty'
                    excluded_general_seeds.append(random_general_seed)
        excluded_seeds.append(random_seed)

def get_opposite_direction(direction):
    if direction == 'left':
        return 'right'
    elif direction == 'right':
        return 'left'
    elif direction == 'up':
        return 'down'
    elif direction == 'down':
        return 'up'
    else:
        return 'start'

# IDK IF THIS CAN BE USED AS FUNCTION.. DELETING LATER
def visit_room(room_name):
    room_info = {}

    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)
        room_info = data['profiles'][character_name]['rooms'][room_name]

    if not room_info['visited']:
        create_adj(room_info)

# def map_new_room(room_name, room_coord, left=None, up=None, right=None, down=None):
#     room_dict = {'name': room_name, 'coordinates': room_coord, 'adj_rooms': {'left': left, 'up': up, 'right': right, 'down': down}, 'visited': False}
#     character_data = {}

#     with open(saves_file_path,'r') as saves_file:
#         data = json.load(saves_file)
#         character_data = data['profiles'][character_name]
#         print(json.dumps(character_data))

#     try:
#         character_data['rooms'].update({room_name: room_dict})
#     except:
#         character_data['rooms'] = {room_name: room_dict}
    
#     with open(saves_file_path, 'w') as saves_file:
#         json.dump(data, saves_file, indent=4)