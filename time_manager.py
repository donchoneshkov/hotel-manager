from datetime import datetime, timedelta
import time

start_date = datetime(year=2000, month=1, day=1)
display_date = start_date.strftime('%d.%m.%Y')


class GameDate(object):
    def __init__(self, game_date = start_date, display_date = display_date):
        self.game_date = game_date
        self.display_date = display_date
        
    def add_day(self):
        self.game_date += timedelta(days=1)
        self.update_display_date() 

    def update_display_date(self):
        self.display_date = self.game_date.strftime('%d.%m.%Y')
        print(self.display_date)

    
class GameTime(object):
    def __init__(self, game_time):
        self.game_time = game_time

    
    def return_game_time(self):
        return self.game_time
    
    
game_time = GameTime(time.time())