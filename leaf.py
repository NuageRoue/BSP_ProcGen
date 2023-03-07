import random as rdm
from corridor_gen import corridor, Room, TILE_UNIT

MIN_LEAF_SIZE = 15

class Leaf():
    """
        a class that represents a subdivision of the space where the dungeon is, as the leaf of a binary tree, following the BSP concept
    """

    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = width + x
        self.y2 = height + y

        self.room = list() #a list that contains all the room that are in the zone of the leaf


        self.leftChild = None
        self.rightChild = None

        self.splitter() #division of the leaf
        self.createRoom() #creation of the room (which only happens if there is no subleaf)

        self.getRoom() #we add to the room list the room lists of the two subLeaves
        self.corridorGen()

    def splitter(self):
        if self.leftChild is not None and self.rightChild is not None:
            return False
        
        splitH = bool(rdm.randint(0,1)) #if True, then we split horizontally. else, we split vertically


        #the axis of splitting is a 50% chance if one of the ratio is not superior to 1.25
        if (self.width > self.height) and self.width / self.height >= 1.25:
            splitH = False
        elif self.height > self.width and self.height / self.width >= 1.25:
            splitH = True 


        max = self.height if splitH else self.width
        max -= MIN_LEAF_SIZE
        #max is the max size of the leaf

        if max <= MIN_LEAF_SIZE :
            return False
        
        split = rdm.randrange(MIN_LEAF_SIZE, max)

        if splitH:
            self.leftChild = Leaf(self.x, self.y, self.width, split)
            self.rightChild = Leaf(self.x, split + self.y, self.width, self.height - split)
        else:
            self.leftChild = Leaf(self.x, self.y, split, self.height)
            self.rightChild = Leaf(split + self.x , self.y, self.width - split, self.height)
        return True

    def createRoom(self):
        if self.leftChild is not None and self.rightChild is not None:
            return False
        roomWidth = rdm.randrange(int(0.5 * self.width), self.width - 4)
        roomHeight = rdm.randrange(int(0.5 * self.height), self.height - 4)

        roomX = rdm.randrange(1, self.width - roomWidth - 1) + self.x
        roomY = rdm.randrange(1, self.height - roomHeight - 1) + self.y
        roomX2 = roomX + roomWidth
        roomY2 = roomY + roomHeight

        self.room.append(Room(roomX, roomY, roomX2, roomY2, False))
        return True
    
    def getRoom(self):
        """if self.leftChild is not None and self.rightChild is not None:
            #self.room = self.room.union(self.leftChild.room.union(self.rightChild.room))
        elif self.leftChild is None and self.rightChild is not None:
            self.room = self.room.union(self.rightChild.room)
        elif self.leftChild is not None and self.rightChild is None:
            self.room = self.room.union(self.leftChild.room)"""
        if self.leftChild is not None:
            self.room.extend(room for room in self.leftChild.room if room not in self.room)
        if self.rightChild is not None:
            self.room.extend(room for room in self.rightChild.room if room not in self.room)

    def corridorGen(self):
        if self.leftChild:
            self.leftChild.corridorGen()
        if self.rightChild:
            self.rightChild.corridorGen()    
            self.room.append(corridor(self.leftChild, self.rightChild))