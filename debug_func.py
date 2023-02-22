from random import *
def display_info(leaf):

    print("lets show info about the dungeon:\n\n")
    print(f"in the dungeon there is {len(leaf.room)} rooms")
    nb_corr = 0
    nb_room = 0
    for room in leaf.room:
        if room.isCorridor:
            nb_corr += 1
        else:
            nb_room += 1
    print(f"there is {nb_corr} corridors and {nb_room} rooms")
    room_test = choice(list(leaf.room))
    print(room_test.adj)