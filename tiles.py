import file_path
from tkinter import Label, Canvas, NW
from PIL import Image, ImageTk
import tile_types
import tile_painter

# should make tile painter to get a path for painting on_click
# brick_path = file_path.get_path('img/tiles/brick_tile.png')

class Tile(object):
    def __init__(self, canvas, tile_type, player_state):
        self.canvas = canvas
        self.category = tile_type['category']
        self.type = tile_type['type']
        self.width = 25
        self.height = 25
        self.cost = 0
        self.passable = True
        self.clickable = True
        self.sellable = True
        self.img_path = tile_types.tile_types[self.category][self.type]['path']
        self.img = Image.open(self.img_path)
        self.pic = ImageTk.PhotoImage(self.img)
        self.tile = None
        self.position = []
        self.player_state = player_state

    def on_click(self, event):
        # print(f'Clicked tyle of type {self.type}')
        print(self)
        #  probably should move logic to tile_painter
        if tile_painter.painter.paint is not None:
            if tile_painter.painter.mode == 'sell':
                if self.sellable == True:
                    self.img = Image.open(tile_painter.painter.paint)
                    self.img = self.img.resize((self.width, self.height))
                    self.pic = ImageTk.PhotoImage(self.img)
                    self.canvas.itemconfig(self.tile, image=self.pic)
                    self.player_state.money += self.cost // 2
            if tile_painter.painter.cost <= self.player_state.money:
                if self.clickable == True:
                    self.img = Image.open(tile_painter.painter.paint)
                    self.img = self.img.resize((self.width, self.height))
                    self.pic = ImageTk.PhotoImage(self.img)
                    self.canvas.itemconfig(self.tile, image=self.pic)
                    self.player_state.money -= tile_painter.painter.cost
                    self.cost = tile_painter.painter.cost
                else:
                    print('tile is not clickable')
            else:
                print('player has no money')
        else:
            print('painter is None')

    def load(self, x, y):
        # probably should move logic to tile_painter, hopefully to be able to store all the needed data in the tiles,
        # like cost, clickable, sellable, passable etc.
        self.tile = self.canvas.create_image(
            x * self.width, y * self.width,
            image=self.pic, anchor=NW
        )
        self.position.append(x)
        self.position.append(y)
        # print(self.position)
        self.canvas.tag_bind(self.tile, '<Button-1>', self.on_click)
        # self.canvas.grid(row=x, column=y) why do I even use this?


# class GrassTile(Tile):
#     def __init__(self, canvas, tile_type):
#         super().__init__(canvas, tile_type)
#         self.img_path = grass_path
#         self.img = Image.open(self.img_path)
#         self.pic = ImageTk.PhotoImage(self.img)
#         self.passable = True


# class BrickTile(Tile):
#     def __init__(self, canvas, tile_type):
#         super().__init__(canvas, tile_type)
#         self.img_path = brick_path
#         self.img = Image.open(self.img_path)
#         self.pic = ImageTk.PhotoImage(self.img)
#         self.passable = False

