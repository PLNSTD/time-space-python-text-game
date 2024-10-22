''' 
IDEAs: 
    - Rooms are generated randomly
    - After generating a room it will be saved on the map for the character (getting back will return the same path as before)
    - Counter on directions depth (example limit of 3 rooms in each direction if connected)
    - Limited rooms (like endingRoom, safeRooms and genericRoom)
'''
import random
from gameplay.rooms import start_room

def start():
    map_dict = {}
    start_room.creation()
    print(start_room.get_room_coord())
    x = input('Did you understand?')

def map_new_room(name, coord):
    room_dict = {'name': name, 'coordinates': coord, 'adj_rooms': {'left': None, 'up': None, 'right': None, 'down': None}}
