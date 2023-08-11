from datetime import datetime
class Greet:
    def __init__(self):
        self.dt = datetime.now()
        self.hour = self.dt.hour

    def greeting(self):
        if self.hour <= 0 <= 12:
            return("Доброе утро") 
        elif self.hour >= 12 <= 17:
            return("Добрый день") 
        elif self.hour >= 17 <= 24:
            return("Добрый вечер") 
        else:
            return("Доброй ночи")