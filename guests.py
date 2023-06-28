# logic for the customer class should be here
from PIL import Image, ImageTk
from tkinter import NW
import random
import time
import time_manager

class Guest(object):
    def __init__(self, canvas, tiles, player_state, guests_list):
        self.canvas = canvas 
        guest_stats = generate_guest_stats()
        self.player_state = player_state
        self.guests_list = guests_list
        self.enter_time = 0
        self.money = guest_stats['money']
        self.satisfaction = guest_stats['satisfaction']
        self.interests = guest_stats['interests']
        self.opinion = guest_stats['opinion']
        self.stay_duration = 0   
        self.img_path = guest_stats['path']
        self.width = 25
        self.height = 25
        self.img = Image.open(self.img_path)
        self.img = self.img.resize((self.width, self.height))
        self.pic = ImageTk.PhotoImage(self.img)
        self.canvas_tile = None
        self.tiles = tiles
        self.position = []
        self.is_leaving = False
        self.path = []
        self.has_left = False

    def enter_shop(self, x, y):
        self.enter_time = time.time()
        self.canvas_tile = self.canvas.create_image(
            x * self.width, y * self.width,
            image=self.pic, anchor=NW
        )
        self.path.append((x, y))
        self.position.append(x)
        self.position.append(y)
        self.move_guest()



    def leave_shop(self):
        self.canvas.delete(self.canvas_tile)
        self.has_left = True
        self.guests_list.pop()
        self.player_state.stars += self.opinion


    def check_current_tile(self):
        print('checking tile:', self.position)
        checking_tile = self.tiles[self.position[0], self.position[1]]
        print('checking_tile.tile_satisfaction is:', checking_tile.tile_satisfaction)
        if checking_tile:
            if checking_tile.tile_satisfaction > 0:
                if self.money >= checking_tile.use_cost:
                    self.satisfaction += checking_tile.tile_satisfaction
                    self.money -= checking_tile.use_cost
                    self.player_state.money += checking_tile.use_cost
                    print(self.money)
                    print(self.player_state.money)
                else:
                    print('customer leaving because he has no money')
                    # increase stars
                    self.opinion = +0.1
                    self.is_leaving = True
            else:
                if self.satisfaction > 0:
                    self.satisfaction += checking_tile.tile_satisfaction
                else:
                    print('customer leaving because he has no satisfaction')
                    # lower stars by a lot
                    self.opinion = -0.4
                    self.is_leaving = True

    def move_guest(self):
        self.check_current_tile()
        if self.has_left:
            return
        new_position = self.get_new_path()

        # print('new position is:', new_position)
        new_x = new_position[0]
        new_y = new_position[1]
    
        if (new_x, new_y) not in self.tiles:
            print("Cannot move guest. Position not in canvas.")
            return

        canvas_x = new_x * self.width
        canvas_y = new_y * self.height

        self.canvas.coords(self.canvas_tile, canvas_x, canvas_y)

        self.position = new_position

        self.canvas.after(1000, self.move_guest)



    def get_new_path(self):
        
        tileN = None
        tileS = None
        tileW = None
        tileE = None
        if self.is_leaving == True:
            if len(self.path) > 0:
                new_position = self.path.pop()
                return new_position
            else:
                self.leave_shop()
        else:
            tileN = self.tiles.get((self.position[0], self.position[1] - 1))
            tileS = self.tiles.get((self.position[0], self.position[1] + 1))
            tileW = self.tiles.get((self.position[0] + 1, self.position[1]))
            tileE = self.tiles.get((self.position[0] - 1, self.position[1]))

            passable_tiles = []

            if tileN and tileN.passable:
                passable_tiles.append((self.position[0], self.position[1] - 1))
            if tileS and tileS.passable:
                passable_tiles.append((self.position[0], self.position[1] + 1))
            if tileW and tileW.passable:
                passable_tiles.append((self.position[0] + 1, self.position[1]))
            if tileE and tileE.passable:
                passable_tiles.append((self.position[0] - 1, self.position[1]))

            if passable_tiles:
                new_position = random.choice(passable_tiles)
                tries = 0
                while new_position in self.path:
                    tries += 1
                    if tries < 10:
                        new_position = random.choice(passable_tiles)
                    else:
                        print('customer is leaving now, because he was lost')
                        # lower stars a little
                        self.opinion = -0.1

                        self.is_leaving = True
                        return self.get_new_path()
                # print(new_position)
                # print(self.path)
                self.path.append(new_position)
                # print(self.path)
                return new_position

        return (self.position[0], self.position[1])







def generate_guest_stats():
    money = random.randint(35, 80)
    interests = 'placeholder'
    opinion = 5
    path = 'img/other/customer.png'
    satisfaction = random.randint(0, 5)
    stats = {
        'money' : money,
        'interests' : interests,
        'opinion' : opinion,
        'path' : path,
        'satisfaction' : satisfaction
    }

    return stats


def generate_guest(root, canvas, guests_list, tiles, entry_tile, player_state):
    if len(guests_list) < 5:
        guest = Guest(canvas, tiles, player_state, guests_list)
        guest.enter_shop(entry_tile.position[0], entry_tile.position[1])
        guests_list.append(guest)

   

