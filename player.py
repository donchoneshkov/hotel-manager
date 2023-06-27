from tkinter import IntVar


class Player(object):
    def __init__(self, money, stars):
        self.money_var = IntVar(value=money)
        self.stars_var = IntVar(value=stars)

    @property
    def money(self):
        return int(self.money_var.get())

    @money.setter
    def money(self, value):
        self.money_var.set(value)

    @property
    def stars(self):
        return float(self.stars_var.get())

    @stars.setter
    def stars(self, value):
        self.stars_var.set(float(value))
