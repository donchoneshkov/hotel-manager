# here should go:
# message log
# types of placeables picking menu
# placeables picker menu
# info about day, money and etc.
from tkinter import Label, Text, END, NSEW, NE, NW, E, Listbox, Button
import tile_types
from PIL import Image, ImageTk
# import file_path
import time_manager


class MessageLog(object):
    def __init__(self, root):
        self.root = root
        self.messages_box = Text(root, height=10, width=94)
        self.messages_box.grid(row=0, column=0, sticky=NSEW, padx=0, pady=0)
        self.messages_box.insert(END, 'placeholder message_box')

    def update_self(self, message):
        self.message = message
        print(message)

class TilePicker(object):
    def __init__(self, root, painter):
        self.root = root
        self.tiles_list = []
        self.painter = painter

    def display_tiles_selection(self, tile_category):
        for tile in self.tiles_list:
            tile.grid_forget()
        self.tiles_list = []
# =================== Set painter to none tile
        img = Image.open('img/other/none.png')
        img = img.resize((25,25))
        photo_img = ImageTk.PhotoImage(img)
        label = Label(self.root, image=photo_img)
        label.image = photo_img
        label.bind('<Button-1>', lambda event, tile= None: self.pick_tile(event, tile))
        self.tiles_list.append(label)
# =================== Set painter to sell tile
        img = Image.open('img/other/sell.png')
        img = img.resize((25,25))
        photo_img = ImageTk.PhotoImage(img)
        label = Label(self.root, image=photo_img)
        label.image = photo_img

        label.bind('<Button-1>', lambda event, tile={
                                                    'tile_type' : 'ground_tiles', 
                                                    'tile' : 'grass',
                                                    'path' : 'img/tiles/grass_tile.png', 
                                                    'cost' : 0,  
                                                    'sellable' : True,
                                                    'passable' : False,
                                                    'tile_satisfaction' : 0,
                                                    'use_cost' : 0,
                                                    'map_value': 0,} : self.pick_tile(event, tile))

        self.tiles_list.append(label)
# ===================
        for key in tile_category.keys():
            img = Image.open(tile_category[key]['path'])
            img = img.resize((25,25))
            photo_img = ImageTk.PhotoImage(img)
            label = Label(self.root, image=photo_img)
            label.image = photo_img
            label.bind('<Button-1>', lambda event, tile=tile_category[key]: self.pick_tile(event, tile))
            self.tiles_list.append(label)
        for i, lbl in enumerate(self.tiles_list):
            lbl.grid(row= i // 5 + 1, column= i % 5)

    def pick_tile(self, event, tile):
        self.painter.update_painter(tile)


class TilesCatalog(object):
    def __init__(self, root, tile_picker):
        self.root = root
        self.tile_picker = tile_picker

        self.catalog = Listbox(root, height=24, width=50)
        self.catalog.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)
        self.catalog.bind('<<ListboxSelect>>', self.update_tile_picker)

        for tile_categoery in tile_types.tile_types.keys():
            self.catalog.insert(END, tile_categoery)


    def update_tile_picker(self, event):
        selected_item =  self.catalog.curselection()
        if selected_item:
            selected_tile_category = self.catalog.get(selected_item)
            self.tile_picker.display_tiles_selection(tile_types.tile_types[selected_tile_category])


class InfoPane(object):
    def __init__(self, root, player_state):
        self.root = root
        self.player_state = player_state
        # get time from time_manager.py
        self.game_date = time_manager.GameDate()

        self.money_label = Label(root, text='Money : $')
        self.money_label.grid(row=0, column=0, padx=0, pady=0, sticky=NSEW)
        self.money_value = Label(root, text=player_state.money_var)
        self.money_value.grid(row=0, column=1, padx=0, pady=0, sticky=NSEW)

        self.stars_label = Label(root, text='Stars : ')
        self.stars_label.grid(row=1, column=0, padx=0, pady=0, sticky=NSEW)
        self.stars_value = Label(root, text=player_state.stars_var)
        self.stars_value.grid(row=1, column=1, padx=0, pady=0, sticky=NSEW)

        self.date_label = Label(root, text='Date : ')
        self.date_label.grid(row=2, column=0, padx=0, pady=0, sticky=NSEW)
        self.date_value = Label(root, text=self.game_date.display_date)
        self.date_value.grid(row=2, column=1, padx=0, pady=0, sticky=NSEW)
        
        self.add_day_button = Button(root, text='Add day', command=self.update_time)
        self.add_day_button.grid(row=3, column=0)

        # track user money and stars
        self.player_state.money_var.trace('w', self.update_labels)
        self.player_state.stars_var.trace('w', self.update_labels)
        # initialize values
        self.money_value.config(text=self.player_state.money_var.get())
        self.stars_value.config(text=self.player_state.stars_var.get())

    def update_labels(self, *args):
        self.money_value.config(text=self.player_state.money_var.get())
        self.stars_value.config(text=self.player_state.stars_var.get())

    def update_time(self):
        self.game_date.add_day()
        self.date_value.config(text=self.game_date.display_date)

    
class TileInfoPane(object):
    def __init__(self, root, painter):
        self.root = root
        self.tile_picker = painter
        tile_category_label = Label(self.root, text='Tile category: ')
        tile_category_label.grid(row=0, column=3, sticky=NE)
        tile_category_value = Label(self.root, text='ground tiles')
        tile_category_value.grid(row=0, column=4, sticky=NW)

        tile_type_label = Label(self.root, text='Tile type: ')
        tile_type_label.grid(row=1, column=3, sticky=NE)
        tile_type_value = Label(self.root, text='grass')
        tile_type_value.grid(row=1, column=4, sticky=NW)

        tile_cost_label = Label(self.root, text='Tile cost: ')
        tile_cost_label.grid(row=2, column=3, sticky=NE)
        tile_cost_value = Label(self.root, text='10')
        tile_cost_value.grid(row=2, column=4, sticky=NW)

        img = Image.open('img/other/none.png')
        img = img.resize((25,25))
        photo_img = ImageTk.PhotoImage(img)
        tile_img_label = Label(self.root, image=photo_img)
        tile_img_label.image = photo_img
        tile_img_label.grid(row=3, column=3, sticky=E)