import random

coordinates = None

def creation():
    global coordinates
    coordinates = random_coord()
    print('This is the Starting Room')

def random_coord(MAX_DEPTH):
    return (random.randint(MAX_DEPTH), random.randint(MAX_DEPTH))

def get_room_coord():
    return coordinates