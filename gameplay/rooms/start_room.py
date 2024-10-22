import random

coordinates = None

def creation():
    global coordinates
    coordinates = random_coord()
    print('This is the Starting Room')

def random_coord():
    return (random.randint(-2,2), random.randint(-2,2))

def get_room_coord():
    return coordinates