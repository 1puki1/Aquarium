import Animal

MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7


class Crab(Animal.Animal):
    def __init__(self, name, age, x, y, directionH):
        self.name = name
        self.age = age
        self.x = x
        self.y = y
        self.directionH = directionH
        self.food = 5

    def __str__(self):
        st = "The crab " + str(self.name) + " is " + str(self.age) + " years old and has " + str(self.food) + " food"
        return st


    def starvation(self):
        if self.food == 0:
            return True
        else:
            return False

    def die(self):
        if self.age == 120:
            return True
        else:
            return False
