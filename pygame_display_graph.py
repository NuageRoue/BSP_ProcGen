import pygame
from player import Player
import random as rdm
from graph import GrapheDico

def getStartRoom(graph):
    """
        function that gives us the starting room for the dungeon;
    """
    roomList = graph.getRoomList()
    for room in roomList:
        if room.id == "entrance":
            return room
    room = rdm.choice(roomList)
    while room.isCorridor:
        room = rdm.choice(roomList)
    return room

def screenGen(screen, player, graph, tile_unit):
    """
        everything that modifies the screen
    """
    screen.fill((0,0,0))
    for room in graph.getRoomList():
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((room.x * tile_unit, room.y * tile_unit),(room.width * tile_unit, room.height * tile_unit)))
    player.show(screen, tile_unit)


def screenUpdate(screen, player, graph, tile_unit):
    """
        everything that modifies the screen
    """
    #screen.fill((0,0,0))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(((player.current_room.x - 1) * tile_unit, (player.current_room.y - 1) * tile_unit),((player.current_room.width + 2) * tile_unit, (player.current_room.height + 2) * tile_unit)))
    for room in graph.getNeighborOf(player.current_room):
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((room.x * tile_unit, room.y * tile_unit),(room.width * tile_unit, room.height * tile_unit)))
    #pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(((player.current_room.x - 1) * tile_unit, (player.current_room.y - 1) * tile_unit),((player.current_room.width + 1) * tile_unit, (player.current_room.height + 1) * tile_unit)))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((player.current_room.x * tile_unit, player.current_room.y * tile_unit),(player.current_room.width * tile_unit, player.current_room.height * tile_unit)))
    player.show(screen, tile_unit)

def playerMovement(player):
    keys = pygame.key.get_pressed()

    # Respond to a specific key press
    if keys[pygame.K_UP]:
        player.move(player.x,player.y - 0.05)
    if keys[pygame.K_DOWN]:
        player.move(player.x,player.y + 0.05)
    if keys[pygame.K_LEFT]:
        player.move(player.x - 0.05,player.y)
    if keys[pygame.K_RIGHT]:
        player.move(player.x + 0.05,player.y)

"""def mainLoop(screen_width, screen_height, tile_unit, leaf):
    roomList = leaf.room
    entrance = getStartRoom(roomList)
    player = Player(entrance)
    print(player.current_room.id)
    
    pygame.init()
    screen = pygame.display.set_mode((screen_width * tile_unit,screen_height * tile_unit))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screenUpdate(screen, roomList, player, tile_unit)
        playerMovement(player)

        pygame.display.update()
    pygame.quit()"""



def mainLoop(screen_width, screen_height, tile_unit, graph):
    #roomList = graph.getRoomList()
    entrance = getStartRoom(graph)
    player = Player(entrance)
    print(player.current_room.id)
    

    pygame.init()
    screen = pygame.display.set_mode((screen_width * tile_unit,screen_height * tile_unit))

    screenGen(screen, player, graph, tile_unit)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #print(player.current_room.id)
        screenUpdate(screen, player, graph, tile_unit)
        playerMovement(player)

        pygame.display.update()
    pygame.quit()
