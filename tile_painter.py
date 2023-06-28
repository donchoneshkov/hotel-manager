# import tiles
from tkinter import StringVar
from PIL import Image, ImageTk


# hold the 'paint' to let tiles know how they should be painted
class TilePainter(object):
    def __init__(self):
        self.paint = None

    def update_painter(self, tile):
        self.paint = tile
        















# initialize tile_painter
painter = TilePainter()