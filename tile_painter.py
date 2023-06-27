# import tiles
from tkinter import StringVar



# muse be reworked to get all data from the tiles, not just path and cost
class TilePainter(object):
    def __init__(self):
        self.paint = None
        self.cost = 0
# gotta find a better way than tile['mode]
    def update_painter(self, tile):
        print('tile is:', tile)
        self.paint = tile['path']
        self.cost = tile['cost']
        if tile['mode']:
            self.mode = tile['mode']
        else:
            self.mode = None
        print('painter: ', self.paint)
        print('cost: ', self.cost)

# initialize tile_painter
painter = TilePainter()