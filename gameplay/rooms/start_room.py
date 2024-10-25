import random

coordinates = None

def creation(MAX_DEPTH):
    global coordinates
    coordinates = random_coord(MAX_DEPTH)
    print('This is the Starting Room')

def random_coord(MAX_DEPTH):
    return (random.randint(0, MAX_DEPTH - 1), random.randint(0, MAX_DEPTH - 1))

def get_room_coord():
    return coordinates