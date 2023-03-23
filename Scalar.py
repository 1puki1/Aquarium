import Fish


class Scalar(Fish.Fish):
    def __init__(self, name, age, x, y, directionH, directionV):
        super().__init__(name, age, x, y, directionH, directionV)
        self.width = 8
        self.height = 5
        self.food = 5

    def get_animal(self):
        anim = [['*', '*', '*', '*', '*', '*', ' ', ' '], [' ', ' ', ' ', ' ', '*', '*', '*', ' '],
                [' ', ' ', '*', '*', '*', '*', '*', '*'], [' ', ' ', ' ', ' ', '*', '*', '*', ' '],
                ['*', '*', '*', '*', '*', '*', ' ', ' ']]
        if self.directionH == 1:
            return anim
        else:
            anim = [[' ', ' ', '*', '*', '*', '*', '*', '*'], [' ', '*', '*', '*', ' ', ' ', ' ', ' '],
                    ['*', '*', '*', '*', '*', '*', ' ', ' '], [' ', '*', '*', '*', ' ', ' ', ' ', ' '],
                    [' ', ' ', '*', '*', '*', '*', '*', '*']]
            return anim
