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
import time
from gameplay.rooms import start_room, safe_room, saving_position, ending_room, snow_room, sand_room, cave_room
from utils import tools
from gameplay.stats_and_inventory import character_inventory

# Construct the relative path to data.json
saves_file_path = os.path.join(os.path.dirname(__file__), '..', '..', 'characters', 'data.json')
MAX_DEPTH = 5
get_seed_cnt = 25
character_name = ''
room_seeds_available = {'safe': 2, 'ending': 1, 'general': {'tot': 21, 'snow': 2, 'sand': 2, 'cave': 2, 'empty': 15}}
rooms_map = [[None for _ in range(MAX_DEPTH)] for _ in range(MAX_DEPTH)]
visited_rooms_map = [[None for _ in range(MAX_DEPTH)] for _ in range(MAX_DEPTH)] # USED TO BE SHOWN TO THE USER
has_map = False

def start(character_name_str):
    global character_name
    global starting_position
    global visited_rooms_map
    global rooms_map

    character_name = character_name_str
    character_info = {}
    # IF SAVING_FILE_EXISTS: LOAD MAP AND POSITION
    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)
        character_info = data['profiles'].get(character_name)

    if character_info.get('rooms_map', None) == None:
        start_room.creation(MAX_DEPTH)
        print(start_room.get_room_coord())
        create_rooms_map(start_room.get_room_coord())
        visit_room(start_room.get_room_coord())
    else:
        rooms_map = character_info['rooms_map']
        starting_position = character_info['position']
        visited_rooms_map = character_info['visited_map']
        visit_room(starting_position)
    
def create_rooms_map(coord):
    global rooms_map
    data = None
    for row in range(MAX_DEPTH):
        for col in range(MAX_DEPTH):
            if row == coord[0] and col == coord[1]:
                rooms_map[row][col] = 'start'
                continue
            rooms_map[row][col] = get_seed()
    tools.prompt_clear()

    with open(saves_file_path, 'r') as saves_file:
        data = json.load(saves_file)
    
    character_data = data['profiles'][character_name]
    character_data['rooms_map'] = rooms_map

    with open(saves_file_path, 'w') as saves_file:
        json.dump(data, saves_file, indent=4)
            
def visit_room(coord_tuple):
    global visited_rooms_map
    visited_rooms_map[coord_tuple[0]][coord_tuple[1]] = 'User'
    while True:
        show_visited_map()
        row, col = coord_tuple
        saving_position.save_progress(character_name, [row, col], rooms_map, visited_rooms_map)
        show_room_options(coord_tuple)
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

        direction = show_directions_choices(coord_tuple, room_choices)
        if direction == -1:
            pass
        elif room_choices[direction] == 'Up':
            visit_room((coord_tuple[0] - 1, coord_tuple[1]))
        elif room_choices[direction] == 'Down':
            visit_room((coord_tuple[0] + 1, coord_tuple[1]))
        elif room_choices[direction] == 'Left':
            visit_room((coord_tuple[0], coord_tuple[1] - 1))
        elif room_choices[direction] == 'Right':
            visit_room((coord_tuple[0], coord_tuple[1] + 1))

def show_directions_choices(this_room, choices):
    global visited_rooms_map
    visited_rooms_map[this_room[0]][this_room[1]] = 'User'
    time.sleep(0.5)
    tools.prompt_clear()
    while True:
        show_visited_map()
        print(f'You are in this coordinates ({this_room[0]} - {this_room[1]})')
        print('\nYou can go:')
        for index, direction in enumerate(choices):
            print(f"\t{index} - {direction}")
        print(f"\t{len(choices)} - Room Options")
        choice = tools.get_player_input_choice()
        if 0 <= choice < len(choices):
            visited_rooms_map[this_room[0]][this_room[1]] = rooms_map[this_room[0]][this_room[1]]
            tools.prompt_clear()
            return choice
        if choice == len(choices):
            return -1
        tools.prompt_clear()

def show_room_options(this_room):
    row, col = this_room[0], this_room[1]
    if rooms_map[row][col] == 'start':
        start_room.options(character_name)
        return
    elif rooms_map[row][col] == 'safe':
        safe_room.options(character_name)
        return
    elif rooms_map[row][col] == 'ending':
        print('You have found the ending room!')
        ending_room.options(character_name)
        pass
    elif rooms_map[row][col] == 'snow':
        snow_room.options(character_name)
        return
    elif rooms_map[row][col] == 'sand':
        sand_room.options(character_name)
        return
    elif rooms_map[row][col] == 'cave':
        cave_room.options(character_name)
        return
    elif rooms_map[row][col] == 'empty':
        print('This is an empty room! There is not much to do here...')
        time.sleep(2)

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
                    
def show_visited_map():
    global has_map
    global visited_rooms_map
    global rooms_map
    if not has_map:
        user_inventory = character_inventory.get_inventory(character_name)
        if 'map' in user_inventory:
            has_map = True
            visited_rooms_map = rooms_map
    print('\n\t----------Map----------')
    for room in visited_rooms_map:
        print(f'\t{room}')
    print('\n')
    