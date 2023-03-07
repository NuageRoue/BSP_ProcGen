from leaf import Leaf, TILE_UNIT
from pygame_display_graph import mainLoop
import graph
from id_sys import idAttribution

SCREEN_WIDTH = int(1300/TILE_UNIT)
SCREEN_HEIGHT = int(700/TILE_UNIT)

class Game():
    def __init__(self):
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.tile_unit = TILE_UNIT
        leaf = Leaf(0,0, self.screen_width,self.screen_height)

        self.graph = graph.graphGen(leaf.room)
        idAttribution(self.graph)
        
    def pygame_show(self):
        mainLoop(self.screen_width, self.screen_height, self.tile_unit, self.graph)

main = Game()
main.pygame_show()