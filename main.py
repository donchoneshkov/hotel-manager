from tkinter import Tk, Frame, Canvas, messagebox
from tiles import *
from gui import *
import populate_background
from levels import level1
import tile_painter
import player
import tile_types
import guests
import random

root = Tk()
root.title('Hotel Manager')
# frames for the GUI to go into
# silly colours are for debugging purposes
level_frame = Frame(root, background='purple')
level_frame.grid(row=0, column=0, rowspan=10, padx=5, pady=5, sticky=NSEW)
messages_frame = Frame(root, background='red')
messages_frame.grid(row=11, column=0, padx=0, pady=0, sticky=NSEW)
tile_picker_frame = Frame(root, background='grey')
tile_picker_frame.grid(row=0, column=1, rowspan=5, padx=0, pady=0, sticky=NSEW)
tiles_catalog_frame = Frame(root, background='blue')
tiles_catalog_frame.grid(row=5, column=1, rowspan=5, padx=0, pady=0, sticky=NSEW)
info_pane_frame = Frame(root, background='yellow')
info_pane_frame.grid(row=11, column=1, padx=0, pady=0, sticky=NSEW)
# canvas for the tiles to go into
canvas = Canvas(level_frame, width=750, height=750)
canvas.grid(row=0,column=0)

# Player (money, stars)
player_state = player.Player(5000, 10)

# GUI
message_log = MessageLog(messages_frame)
tile_picker = TilePicker(tile_picker_frame, tile_painter.painter)
tiles_catalog = TilesCatalog(tiles_catalog_frame, tile_picker)
info_pane = InfoPane(info_pane_frame, player_state)
tile_info_pane = TileInfoPane(info_pane_frame, tile_painter.painter)
# populate map
level_map = populate_background.populate_level(level1.level)
# populate tiles from map
tiles = {}
entry_tile = None
for coords, value in level_map:

    tile = Tile(canvas, tile_types.tile_types[value['category']][value['type']], player_state)
    tile.load(coords[0], coords[1])

    tiles[coords[0], coords[1]] = tile
    if tile.type == 'entry':
        entry_tile = tile

# start calling guests
guests_list = []
def guest_caller():
    guests.generate_guest(root, canvas, guests_list, tiles, entry_tile, player_state)
    root.after(interval* 1000, guest_caller)

guests.generate_guest(root, canvas, guests_list, tiles, entry_tile, player_state)

interval = random.randint(10, 15)
root.after(interval* 1000, guest_caller)

# check win/loss conditions
def check_for_loss(*args):
    stars = player_state.stars_var.get()
    print('stars is:', stars)
    if stars <= 0:
        print('stars < 0')
        messagebox.showinfo('Game Over', 'You have dissappointed to many guests!')
        root.quit()
    elif stars >= level1.level_requrements['stars']:
        messagebox.showinfo('Win!', 'You have satisfied enough customers and have passed to the next level!')
        root.quit()

player_state.stars_var.trace('w', check_for_loss)


root.mainloop()