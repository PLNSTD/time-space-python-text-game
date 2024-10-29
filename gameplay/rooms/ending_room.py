from gameplay.stats_and_inventory import character_inventory

def options(character_name):
    print('You have found the ending room!')
    user_inventory = character_inventory.get_inventory()
    if 'key' in user_inventory:
        print('\n\tIt look like you have the key, now you can escape from the dungeon!')
        exit()
    print('You notice a strange notes on one of the walls of the room:')
    print('\n\tNote:')
    print('\n\tYou did not found the key yet!\n\tAsk to the Merchant in any room for guidance')
    character_inventory.add_item(character_name, 'ending_note')