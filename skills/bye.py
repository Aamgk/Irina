import random

class GoodBye:
    def __init__(self):
        self.bye = ['Пока-пока', 'Досвидания', 'Выключаюсь']

    def byeBye(self):
        return random.choice(self.bye)