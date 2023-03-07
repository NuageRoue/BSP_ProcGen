from room import Room, TILE_UNIT
import random as rdm

CORRIDOR_THICKNESS = 2

def corridor(node1, node2):
    side = ()
    secondAxis = ()
    link = None

    nodeA = node1
    nodeB = node2

    if node1.x2 == node2.x: #if node1 is at the left of node2
        side = ("x2", "x")
        secondAxis = ("y", "y2")
        link = corZoneX

    elif node1.x2 == node2.x:
        side = ("x2", "x")
        secondAxis = ("y", "y2")
        nodeA = node2
        nodeB = node1
        link = corZoneX

    elif node1.y2 == node2.y:
        side = ("y2","y")
        secondAxis = ("x","x2")
        link = corZoneY
    elif node1.y == node2.y2:
        side = ("y2","y")
        secondAxis = ("x","x2")
        nodeA = node2
        nodeB = node1
        link = corZoneY

    else:
        raise ValueError('nodes are not adjacent')


    couple = getNearestRooms(nodeA.room, nodeB.room, side, secondAxis)
    cor =  link(couple[0], couple[1])
    
    couple[0].addGraph(side[0], cor)
    couple[1].addGraph(side[1], cor)

    cor.addGraph(side[1], couple[0])
    cor.addGraph(side[0], couple[1])
    return cor

def enoughSpace(room1, room2, secondAxis):
    secondAxis0 = lambda room: getattr(room, secondAxis[0]) 
    secondAxis1 = lambda room: getattr(room, secondAxis[1]) 

    A = max(secondAxis0(room1),secondAxis0(room2))
    B = min(secondAxis1(room1),secondAxis1(room2))

    if B - A < CORRIDOR_THICKNESS + 2 :
        return False
    return True

def dist(room1, room2, side):
    side0 = lambda room: getattr(room, side[0]) 
    side1 = lambda room: getattr(room, side[1])
    return (side1(room2) - side0(room1))

def corZoneX(room1, room2):
    X = room1.x2
    Y = max(room1.y, room2.y)
    X2 = room2.x
    Y2 = min(room1.y2, room2.y2)

    return corrX(X, Y, X2, Y2)
def corrX(X, Y, X2, Y2):
    corrX = X
    corrX2 = X2

    if (Y2 - Y) == CORRIDOR_THICKNESS + 2:
        corrY = Y + 1
    else:
        corrY = rdm.randrange(Y + 1, Y2 - CORRIDOR_THICKNESS - 1)
    corrY2 = corrY + CORRIDOR_THICKNESS
    return Room(corrX, corrY, corrX2, corrY2, True)

def corZoneY(room1, room2):
    X = max(room1.x, room2.x)
    Y = room1.y2
    X2 = min(room1.x2, room2.x2)
    Y2 = room2.y

    return corrY(X, Y, X2, Y2)
def corrY(X,Y,X2,Y2):
    corrY = Y
    corrY2 = Y2

    if (X2 - X) == CORRIDOR_THICKNESS + 2:
        corrX = X + 1
    else:
        corrX = rdm.randrange(X + 1, X2 - CORRIDOR_THICKNESS - 1)
    corrX2 = corrX + CORRIDOR_THICKNESS
    return Room(corrX, corrY, corrX2, corrY2, True)


#generations of the couple
def getNearestRooms(room_list1, room_list2, side, secondAxis):
    couple = (None, None)
    shortest_dist = None

    side0 = lambda room: getattr(room, side[0]) 
    side1 = lambda room: getattr(room, side[1]) 

    secondAxis0 = lambda room: getattr(room, secondAxis[0]) 
    secondAxis1 = lambda room: getattr(room, secondAxis[1]) 

    for room1 in room_list1:
        for room2 in room_list2:
            if (secondAxis1(room1) > secondAxis0(room2)) and (secondAxis0(room1) < secondAxis1(room2)) and (enoughSpace(room1, room2, secondAxis)): #if rooms are facing
                if ((couple == (None, None)) or (dist(room1, room2, side) <= shortest_dist)):
                    shortest_dist = dist(room1, room2, side)
                    couple = (room1, room2)
    return couple




















## unused

def get_nearest_corridors(room_list1, room_list2, side, secondAxis):
    couple = (None, None)
    shortest_dist = None

    side0 = lambda room: getattr(room, side[0]) 
    side1 = lambda room: getattr(room, side[1]) 

    secondAxis0 = lambda room: getattr(room, secondAxis[0]) 
    secondAxis1 = lambda room: getattr(room, secondAxis[1]) 

    for room1 in room_list1:
        for room2 in room_list2:
            if ((room1.isCorridor) and (room2.isCorridor)):
                if (secondAxis1(room1) > secondAxis0(room2)) and (secondAxis0(room1) < secondAxis1(room2)) and (enoughSpace(room1, room2, secondAxis)): #if rooms are facing
                    if ((couple == (None, None)) or (dist(room1, room2, side) <= shortest_dist)):
                        shortest_dist = dist(room1, room2, side)
                        couple = (room1, room2)
    return couple if couple != (None, None) else False

def get_nearest_corridor_room(room_list1, room_list2, side, secondAxis):
    couple = (None, None)
    shortest_dist = None

    side0 = lambda room: getattr(room, side[0]) 
    side1 = lambda room: getattr(room, side[1]) 

    secondAxis0 = lambda room: getattr(room, secondAxis[0]) 
    secondAxis1 = lambda room: getattr(room, secondAxis[1]) 

    for room1 in room_list1:
        for room2 in room_list2:
            if ((room1.isCorridor)):
                if (secondAxis1(room1) > secondAxis0(room2)) and (secondAxis0(room1) < secondAxis1(room2)) and (enoughSpace(room1, room2, secondAxis)): #if rooms are facing
                    if ((couple == (None, None)) or (dist(room1, room2, side) <= shortest_dist)):
                        shortest_dist = dist(room1, room2, side)
                        couple = (room1, room2)
    return couple if couple != (None, None) else False

def get_nearest_room_corridor(room_list1, room_list2, side, secondAxis):
    couple = (None, None)
    shortest_dist = None

    side0 = lambda room: getattr(room, side[0]) 
    side1 = lambda room: getattr(room, side[1]) 

    secondAxis0 = lambda room: getattr(room, secondAxis[0]) 
    secondAxis1 = lambda room: getattr(room, secondAxis[1]) 

    for room1 in room_list1:
        for room2 in room_list2:
            if ((room2.isCorridor)):
                if (secondAxis1(room1) > secondAxis0(room2)) and (secondAxis0(room1) < secondAxis1(room2)) and (enoughSpace(room1, room2, secondAxis)): #if rooms are facing
                    if ((couple == (None, None)) or (dist(room1, room2, side) <= shortest_dist)):
                        shortest_dist = dist(room1, room2, side)
                        couple = (room1, room2)
    return couple if couple != (None, None) else False