import pygame

class Player():
    def __init__(self, room):
        self.x = ((room.x + room.x2) // 2)
        self.y = (room.y + room.y2) // 2
        self.current_room = room
    
    def move(self, x,y):
        """
            function that changes the player's coordinates if the new coordinates still let him in the dungeon
        """
        if self.current_room.collide((x,y)):
            self.x = x
            self.y = y
            return
        for room in self.current_room.adj:
            if self.current_room.adj[room].collide((x,y)):
                self.x = x
                self.y = y
                self.current_room = self.current_room.adj[room]
                return

    def show(self, screen, tile_unit):
        pygame.draw.circle(screen, (0, 255, 0), (int(self.x * tile_unit), int(self.y * tile_unit)), tile_unit//2)

def is_in(x,y, player):
    if player.current_room.collide((x,y)):
        return True
    for room_adj in player.current_room.adj:
        if player.current_room.adj[room_adj].collide((x,y)):
            player.current_room = player.current_room.adj[room_adj]
            return True
        return False