import Crab


class Ocypode(Crab.Crab):
    def __init__(self, name, age, x, y, directionH):
        self.name = name
        self.age = age
        self.x = x
        self.y = y
        self.directionH = directionH
        self.food = 5

    def get_animal(self):
        anim = [[' ', '*', ' ', ' ', ' ', '*', ' ',], [' ', ' ', '*', '*', '*', ' ', ' '],
                ['*', '*', '*', '*', '*', '*', '*'], ['*', ' ', ' ', ' ', ' ', ' ', '*']]
        return anim
