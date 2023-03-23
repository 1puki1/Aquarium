import Fish


class Moly(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        self.name = name
        self.age = age
        self.x = x
        self.y = y
        self.directionH = directionH
        self.directionV = directionV
        self.food = 5

    def get_animal(self):
        anim = [[' ', '*', '*', '*', ' ', ' ', ' ', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'],
                [' ', '*', '*', '*', ' ', ' ', ' ', '*']]
        if self.directionH == 0:
            return anim
        else:
            anim = [['*', ' ', ' ', ' ', '*', '*', '*', ' '], ['*', '*', '*', '*', '*', '*', '*', '*'],
                    ['*', ' ', ' ', ' ', '*', '*', '*', ' ']]
            return anim
