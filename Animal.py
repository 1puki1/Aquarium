MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
STARTING_FOOD = 5
MAX_AGE = 120


class Animal:
    def __init__(self, name, age, x, y, directionH):
        self.alive = True
        self.width = MAX_ANIMAL_HEIGHT
        self.height = MAX_ANIMAL_HEIGHT
        self.food = STARTING_FOOD
        self.name = name
        self.age = age
        self.x = x
        self.y = y
        self.directionH = directionH  # random 0 - left / 1 - right

    def __str__(self):
        return self.name + self.age + self.x + self.y + self.directionHre

    def get_food(self):
        return self.food

    def get_age(self):
        return self.age

    def dec_food(self):
        self.food -= 1
        return self.food

    def inc_age(self):
        self.age += 1
        return self.age

    def right(self):
        self.x += 1
        return self.x

    def left(self):
        self.x -= 1
        return self.x

    def get_position(self):
        return self.x, self.y

    def set_x(self, x):
        self.x = x
        return self.x

    def set_y(self, y):
        self.y = y
        return self.y

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

    def get_directionH(self):
        return self.directionH

    def set_directionH(self, directionH):
        self.directionH = directionH
        return self.directionH

    def get_alive(self):
        if self.food > 0 and self.age < 120:
            return True


    def get_size(self):
        return (self.width, 'x', self.height)

    def get_food_amount(self):
        return self.food

    def add_food(self, amount):
        self.food += amount
        return self.food

    def get_animal(self):
        pass
