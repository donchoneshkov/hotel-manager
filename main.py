from tkinter import *
from tiles import *
from gui import *
import populate_background
from levels import level1
import tile_painter
import player
root = Tk()
root.title('Hotel Manager')

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

canvas = Canvas(level_frame, width=750, height=750)
canvas.grid(row=0,column=0)

# Player
player_state = player.Player(5000, 5.0)


message_log = MessageLog(messages_frame)
tile_picker = TilePicker(tile_picker_frame, tile_painter.painter)
tiles_catalog = TilesCatalog(tiles_catalog_frame, tile_picker)
info_pane = InfoPane(info_pane_frame, player_state)
tile_info_pane = TileInfoPane(info_pane_frame, tile_painter.painter)

level_map = populate_background.populate_level(level1.level)




tiles = {}
for coords, value in level_map:
    # print(coords, value)
    tile = Tile(canvas, value, player_state)
    tile.load(coords[0], coords[1])
    # tiles.append(tile)

    tiles[coords[0], coords[1]] = tile
    # print(tiles[coords[0], coords[1]])

# print(tiles[4 , 15].position)
# tiles[4, 15].on_click('e')



root.mainloop()