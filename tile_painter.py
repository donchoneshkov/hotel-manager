# import tiles
from tkinter import StringVar
from PIL import Image, ImageTk


# muse be reworked to get all data from the tiles, not just path and cost
class TilePainter(object):
    def __init__(self):
        self.paint = None
        # self.cost = 0
# gotta find a better way than tile['mode]
    def update_painter(self, tile):
        print('painter tile: ', tile)
        self.paint = tile
        















# initialize tile_painter
painter = TilePainter()