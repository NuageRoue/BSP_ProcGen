import random as rdm
from graph import GrapheDico
#l'objectif ici est l'attribution d'id aux differentes salles;

ROOMTYPE = ['treasure room','healing room','merchant room']

def idAttribution(graph):
    entrance(graph)
    sortie(graph)
    #specialRoom(roomList)

def specialRoom(roomList):
    roomNB = 0
    while rdm.random() > 0.8:
        roomNB += 1
        while (roomList[roomNB].isCorridor) and (roomList[roomNB].id is not None) :
            roomNB += 1
            roomNB %= len(roomList)
    roomList[roomNB].id = rdm.choice(ROOMTYPE)

    
def entrance(graph):
    room = rdm.choice(graph.getRoomList())
    while room.isCorridor or graph.nbNeighborOf(room) == 1:
        room = rdm.choice(graph.getRoomList())
    room.id = 'entrance'

def sortie(graph):
    room = rdm.choice(graph.getRoomList())
    while room.isCorridor or graph.nbNeighborOf(room) != 1 or room.id == 'entrance' :
        room = rdm.choice(graph.getRoomList())
    room.id = 'exit'