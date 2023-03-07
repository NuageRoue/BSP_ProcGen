TILE_UNIT = 10

class Room():
    """
        class of objects that represents a squared room with coordinates as his attributes and methods that can be used to show the room on screen, tell if the room is colliding... 

        /!\ coordinates are given in TILE_UNIT, not in pixel :  if TILE_UNIT = 2 and self.x = 10 TU, then self.x = 20px
    """
    def __init__(self, x, y, x2, y2, isCorridor):

        #coordinates
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2

        #width and length
        self.width = x2 - x
        self.height = y2 - y

        self.isCorridor = isCorridor

        self.id = None
        self.adj = {}

    def collide(self, coord):
        if (coord[0] > self.x and coord[0] < self.x2) and (coord[1] > self.y and coord[1] < self.y2):
            return True
        return False
    
    def addGraph(self,side,room):
        if side not in self.adj :
            self.adj[side] = room