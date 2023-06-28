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
        self.tile_type = tile_type
        self.category = tile_type['tile_type']
        self.type = tile_type['tile']
        self.width = 25
        self.height = 25
        self.img_path = tile_type['path']
        self.cost = tile_type['cost']
        self.sellable = tile_type['sellable']
        self.passable = tile_type['passable']
        self.map_value = tile_type['map_value']
        self.tile_satisfaction = tile_type['tile_satisfaction']
        self.use_cost = tile_type['use_cost']
        self.clickable = True
        # self.img_path = tile_types.tile_types[self.category][self.type]['path']
        self.img = Image.open(self.img_path)
        self.img = self.img.resize((self.width, self.height))
        self.pic = ImageTk.PhotoImage(self.img)
        self.canvas_tile = None
        self.position = []
        self.player_state = player_state


    def on_click(self, event):

        if tile_painter.painter.paint is not None:
            if tile_painter.painter.paint['cost'] == 0:
                if self.sellable == True:
                    self.img = Image.open(tile_painter.painter.paint['path'])
                    self.img = self.img.resize((self.width, self.height))
                    self.pic = ImageTk.PhotoImage(self.img)
                    self.canvas.itemconfig(self.canvas_tile, image=self.pic)
                    self.player_state.money += self.cost // 2

                    self.category = tile_painter.painter.paint['tile_type']
                    self.type = tile_painter.painter.paint['tile']
                    # target_tile.width = 25
                    # target_tile.height = 25
                    self.img_path = tile_painter.painter.paint['path']
                    self.cost = tile_painter.painter.paint['cost']
                    self.sellable = tile_painter.painter.paint['sellable']
                    self.passable = tile_painter.painter.paint['passable']
                    self.tile_satisfaction = tile_painter.painter.paint['tile_satisfaction']
                    self.use_cost = tile_painter.painter.paint['use_cost']
                    self.map_value = tile_painter.painter.paint['map_value']
                    self.tile_type = tile_painter.painter.paint

            elif tile_painter.painter.paint['cost'] <= self.player_state.money:
                if self.clickable == True:
                    if self.sellable == True:

                        self.img = Image.open(tile_painter.painter.paint['path'])
                        self.img = self.img.resize((self.width, self.height))
                        self.pic = ImageTk.PhotoImage(self.img)
                        self.canvas.itemconfig(self.canvas_tile, image=self.pic)
                        self.player_state.money -= tile_painter.painter.paint['cost']

                        self.category = tile_painter.painter.paint['tile_type']
                        self.type = tile_painter.painter.paint['tile']
                        # target_tile.width = 25
                        # target_tile.height = 25
                        self.img_path = tile_painter.painter.paint['path']
                        self.cost = tile_painter.painter.paint['cost']
                        self.sellable = tile_painter.painter.paint['sellable']
                        self.passable = tile_painter.painter.paint['passable']
                        self.tile_satisfaction = tile_painter.painter.paint['tile_satisfaction']
                        self.use_cost = tile_painter.painter.paint['use_cost']
                        self.map_value = tile_painter.painter.paint['map_value']
                        self.tile_type = tile_painter.painter.paint
                    else:
                        print('tile is not sellable')
                else:
                    print('tile is not clickable')
            else:
                print('player has no money')
        else:
            print('painter is None')


    def load(self, x, y):

        self.canvas_tile = self.canvas.create_image(
            x * self.width, y * self.width,
            image=self.pic, anchor=NW
        )
        self.position.append(x)
        self.position.append(y)
        self.canvas.tag_bind(self.canvas_tile, '<Button-1>', self.on_click)
        # self.canvas.grid(row=x, column=y) why do I even use this ?????????
