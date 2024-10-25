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
from utils import tools as user

# Construct the relative path to data.json
saves_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'characters', 'data.json')
MAX_DEPTH = 5
get_seed_cnt = 25
character_name = ''
room_seeds_available = {'safe': 2, 'ending': 1, 'general': {'tot': 21, 'snow': 2, 'sand': 2, 'cave': 2, 'empty': 15}}
rooms_map = [[None for _ in range(MAX_DEPTH)] for _ in range(MAX_DEPTH)]
visited_rooms_map = [[None for _ in range(MAX_DEPTH)] for _ in range(MAX_DEPTH)] # USED TO BE SHOWN TO THE USER

def start(character_name_str):
    global character_name
    character_name = character_name_str
    # IF SAVING_FILE_EXISTS: LOAD MAP AND POSITION
    map_dict = {}
    start_room.creation(MAX_DEPTH)
    print(start_room.get_room_coord())
    create_rooms_map(start_room.get_room_coord())
    change_room(start_room.get_room_coord())

def create_rooms_map(coord):
    global rooms_map
    data = None
    for row in range(MAX_DEPTH):
        for col in range(MAX_DEPTH):
            if row == coord[0] and col == coord[1]:
                rooms_map[row][col] = 'start'
                continue
            rooms_map[row][col] = get_seed()
    user.prompt_clear()

    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)
    
    character_data = data['profiles'][character_name]
    character_data['rooms_map'] = rooms_map

    with open(saves_file_path, 'w') as saves_file:
        json.dump(data, saves_file, indent=4)
            
def change_room(coord_tuple):
    row, col = coord_tuple
    room_choices = []
    direction = -1

    if row == 0 and col == 0: # Top-left
        room_choices.extend(['Down', 'Right'])
    elif row == 0 and col == 4: # Top-right
        room_choices.extend(['Down', 'Left'])
    elif row == 4 and col == 0: # Bot-left
        room_choices.extend(['Up', 'Right'])
    elif row == 4 and col == 4: # Bot-right
        room_choices.extend(['Up', 'Left'])
    elif row == 0:
        room_choices.extend(['Down', 'Left', 'Right'])
    elif row == MAX_DEPTH - 1:
        room_choices.extend(['Up', 'Left', 'Right'])
    elif col == 0:
        room_choices.extend(['Up', 'Down', 'Right'])
    elif col == MAX_DEPTH - 1:
        room_choices.extend(['Up', 'Down', 'Left'])
    else:
        room_choices.extend(['Up', 'Down', 'Left', 'Right'])

    direction = show_room_choices(coord_tuple, room_choices)
    if room_choices[direction] == 'Up':
        change_room((coord_tuple[0] - 1, coord_tuple[1]))
    elif room_choices[direction] == 'Down':
        change_room((coord_tuple[0] + 1, coord_tuple[1]))
    elif room_choices[direction] == 'Left':
        change_room((coord_tuple[0], coord_tuple[1] - 1))
    elif room_choices[direction] == 'Right':
        change_room((coord_tuple[0], coord_tuple[1] + 1))

def show_room_choices(this_room, choices):
    visited_rooms_map[this_room[0]][this_room[1]] = 'User'
    while True:
        print(f'MAP: {show_map()}')
        print(f'You are in this coordinates ({this_room[0]} - {this_room[1]})')
        print('\nYou can go:')
        for index, direction in enumerate(choices):
            print(f"\t{index} - {direction}")
        choice = user.get_player_input_choice()
        if 0 <= choice < len(choices):
            visited_rooms_map[this_room[0]][this_room[1]] = rooms_map[this_room[0]][this_room[1]]
            user.prompt_clear()
            return choice
        user.prompt_clear()

def get_seed():
    excluded_seeds = []
    global get_seed_cnt
    while True:
        print(f'Getting seeds... remaining {room_seeds_available}')
        print(rooms_map)
        random_seed = random.randint(1, 3)
        if random_seed in excluded_seeds:
            continue
        else:
            get_seed_cnt -= 1
        if random_seed == 1:
            if room_seeds_available['safe'] > 0:
                room_seeds_available['safe'] -= 1
                return 'safe'
            else:
                excluded_seeds.append(random_seed)
        elif random_seed == 2:
            if room_seeds_available['ending'] > 0:
                room_seeds_available['ending'] -= 1
                return 'ending'
            else:
                excluded_seeds.append(random_seed)
        elif random_seed == 3:
            if room_seeds_available['general']['tot'] > 0:
                excluded_general_seeds = []
                while True:
                    random_general_seed = random.randint(1,21)
                    if random_general_seed in excluded_general_seeds:
                        continue
                    if random_general_seed == 1:
                        if room_seeds_available['general']['snow'] > 0:
                            room_seeds_available['general']['snow'] -= 1
                            room_seeds_available['general']['tot'] -= 1
                            return 'snow'
                        else:
                            excluded_general_seeds.append(random_general_seed)
                    elif random_general_seed == 2:
                        if room_seeds_available['general']['sand'] > 0:
                            room_seeds_available['general']['sand'] -= 1
                            room_seeds_available['general']['tot'] -= 1
                            return 'sand'
                        else:
                            excluded_general_seeds.append(random_general_seed)
                    elif random_general_seed == 3:
                        if room_seeds_available['general']['cave'] > 0:
                            room_seeds_available['general']['cave'] -= 1
                            room_seeds_available['general']['tot'] -= 1
                            return 'cave'
                        else:
                            excluded_general_seeds.append(random_general_seed)
                    elif room_seeds_available['general']['empty'] > 0:
                        room_seeds_available['general']['empty'] -= 1
                        room_seeds_available['general']['tot'] -= 1
                        return 'empty'
                    
def show_map():
    for room in visited_rooms_map:
        print(room)

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