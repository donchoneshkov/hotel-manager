from tkinter import IntVar

# holds player stats
class Player(object):
    def __init__(self, money, stars):
        self.money_var = IntVar(value=money)
        self.stars_var = IntVar(value=stars)
    # getter
    @property
    def money(self):
        return int(self.money_var.get())
    # setter
    @money.setter
    def money(self, value):
        self.money_var.set(value)

    # getter
    @property
    def stars(self):
        return int(self.stars_var.get())
    # setter
    @stars.setter
    def stars(self, value):
        self.stars_var.set(int(value))
