import Animal
import Fish
import Crab
import Shrimp
import Scalar
import Moly
import Ocypode

MAX_ANIMAL_HEIGHT = 8
MAX_ANIMAL_WIDTH = 8
MAX_CRAB_HEIGHT = 4
MAX_CRAB_WIDTH = 7
MAX_FISH_HEIGHT = 5
MAX_FISH_WIDTH = 8
WATERLINE = 3
FEED_AMOUNT = 10
MAX_AGE = 120


class Aqua:
    def __init__(self, aqua_width, aqua_height):
        self.turn = 0
        self.aqua_height = aqua_height
        self.aqua_width = aqua_width
        self.board = [' '] * self.aqua_height
        self.build_tank()
        self.anim = []

    def build_tank(self):
        x = self.aqua_width
        y = self.aqua_height
        box = [[' '] * x for _ in range(y)]
        box[2] = ['~'] * x
        box[y - 1] = ['_'] * x
        box[y - 1][0] = '\\'
        box[y - 1][x - 1] = '/'
        for i in range(len(box)):
            if i == y - 1:
                box[i][0] = '\\'
                box[i][x - 1] = '/'
            elif box[i][0] and box[i][x - 1] == " " or "~":
                box[i][0] = '|'
                box[i][x - 1] = '|'
        self.board = box
        return self.board

    def print_board(self):

        for j in self.board:
            print(*j)

    def get_board(self):
        return self.board

    def get_all_animal(self):
        """
        Returns the array that contains all the animals
        """
        return self.anim

    def is_collision(self, animal):
        """
        Returns True if the next step of the crab is a collision
        """
        for animal in self.anim:
            if isinstance(animal, Crab.Crab):
                if animal.directionH == 1:
                    for i in range(0, 3):
                        if animal.x >= self.aqua_width - 8:
                            continue
                        elif self.board[animal.y + i][animal.x + 8] == "*":
                            animal.directionH = 0
                elif animal.directionH == 0:
                    for i in range(0, 3):
                        if animal.x <= 2:
                            continue
                        elif self.board[animal.y + i][animal.x - 2] == "*":
                            animal.directionH = 1
                else:
                    return False

    def print_animal_on_board(self, animal: Animal):
        if isinstance(animal, Scalar.Scalar):
            b = animal.get_animal()
            self.board[animal.y][animal.x:animal.x + 8] = b[0][0:]
            self.board[animal.y + 1][animal.x:animal.x + 8] = b[1][0:]
            self.board[animal.y + 2][animal.x:animal.x + 8] = b[2][0:]
            self.board[animal.y + 3][animal.x:animal.x + 8] = b[3][0:]
            self.board[animal.y + 4][animal.x:animal.x + 8] = b[4][0:]

        elif isinstance(animal, Moly.Moly):
            b = animal.get_animal()
            self.board[animal.y][animal.x:animal.x + 8] = b[0][0:]
            self.board[animal.y + 1][animal.x:animal.x + 8] = b[1][0:]
            self.board[animal.y + 2][animal.x:animal.x + 8] = b[2][0:]

        elif isinstance(animal, Ocypode.Ocypode):
            b = animal.get_animal()
            self.board[animal.y][animal.x:animal.x + 7] = b[0][0:]
            self.board[animal.y + 1][animal.x:animal.x + 7] = b[1][0:]
            self.board[animal.y + 2][animal.x:animal.x + 7] = b[2][0:]
            self.board[animal.y + 3][animal.x:animal.x + 7] = b[3][0:]

        elif isinstance(animal, Shrimp.Shrimp):
            b = animal.get_animal()
            self.board[animal.y][animal.x:animal.x + 7] = b[0][0:]
            self.board[animal.y + 1][animal.x:animal.x + 7] = b[1][0:]
            self.board[animal.y + 2][animal.x:animal.x + 7] = b[2][0:]

        return self.board

    def delete_animal_from_board(self, animal: Animal):
        if isinstance(animal, Scalar.Scalar):
            self.board[animal.y][animal.x:animal.x + 8] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.board[animal.y + 1][animal.x:animal.x + 8] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.board[animal.y + 2][animal.x:animal.x + 8] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.board[animal.y + 3][animal.x:animal.x + 8] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.board[animal.y + 4][animal.x:animal.x + 8] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        elif isinstance(animal, Moly.Moly):
            self.board[animal.y][animal.x:animal.x + 8] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.board[animal.y + 1][animal.x:animal.x + 8] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.board[animal.y + 2][animal.x:animal.x + 8] = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        elif isinstance(animal, Ocypode.Ocypode):
            self.board[animal.y][animal.x:animal.x + 7] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.board[animal.y + 1][animal.x:animal.x + 7] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.board[animal.y + 2][animal.x:animal.x + 7] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.board[animal.y + 3][animal.x:animal.x + 7] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']

        elif isinstance(animal, Shrimp.Shrimp):
            self.board[animal.y][animal.x:animal.x + 7] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.board[animal.y + 1][animal.x:animal.x + 7] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.board[animal.y + 2][animal.x:animal.x + 7] = [' ', ' ', ' ', ' ', ' ', ' ', ' ']

        return self.board

    def add_fish(self, name, age, x, y, directionH, directionV, fish_type):
        """
        Adding fish to the aquarium
        """
        if fish_type == 'sc':
            fish = Scalar.Scalar(name, age, x, y, directionH, directionV)
        elif fish_type == "mo":
            fish = Moly.Moly(name, age, x, y, directionH, directionV)
        else:
            raise ValueError('no such type')
        self.anim.append(fish)
        self.print_animal_on_board(fish)
        return True

    def add_crab(self, name, age, x, y, directionH, crabtype):
        """
        Adding crab to the aquarium
        """
        if crabtype == 'sh':
            crab = Shrimp.Shrimp(name, age, x, y, directionH)
        elif crabtype == 'oc':
            crab = Ocypode.Ocypode(name, age, x, y, directionH)
        else:
            raise ValueError('no such type')

        self.anim.append(crab)
        self.print_animal_on_board(crab)
        return True

    def check_if_free(self, x, y) -> bool:
        """
       method for checking whether the position is empty before inserting a new animal
       """

        for i in range(0, 9):
            for j in range(0, 6):
                if self.board[y + j][x + i] == '*':
                    return False
        return True

    def left(self, a):
        self.delete_animal_from_board(a)
        a.x -= 1
        return self.print_animal_on_board(a)

    def right(self, a):
        self.delete_animal_from_board(a)
        a.x += 1
        return self.print_animal_on_board(a)

    def up(self, a):
        self.delete_animal_from_board(a)
        a.y -= 1
        return self.print_animal_on_board(a)

    def down(self, a):

        self.delete_animal_from_board(a)
        a.y += 1
        return self.print_animal_on_board(a)

    def next_turn(self):
        """
        Managing a single step
        """
        animal_copy = self.anim.copy()
        for anim in animal_copy:
            if isinstance(anim, Animal.Animal):
                if self.turn % 10 == 0:
                    anim.dec_food()
                if self.turn % 100 == 0:
                    anim.inc_age()
                if anim.die():
                    self.delete_animal_from_board(anim)
                    print(str(anim.name) + ' died in good health')
                    self.anim.remove(anim)
                    continue
            if isinstance(anim, Crab.Crab):
                if anim.starvation():
                    print('The crab ' + str(anim.name) + ' died at the age of ' + str(anim.age) +
                          ' years\nBecause he ran out of food!')
                    self.delete_animal_from_board(anim)
                    self.anim.remove(anim)
                    continue
                if anim.directionH == 1:
                    if anim.x == self.aqua_width - 8:
                        anim.directionH = 0
                        self.delete_animal_from_board(anim)
                        self.print_animal_on_board(anim)
                    elif not self.is_collision(anim):
                        self.right(anim)
                    else:
                        self.left(anim)
                else:
                    if anim.x == 1:
                        anim.directionH = 1
                        self.delete_animal_from_board(anim)
                        self.print_animal_on_board(anim)
                    elif not self.is_collision(anim):
                        self.left(anim)
                    else:
                        self.right(anim)
            elif isinstance(anim, Fish.Fish):
                if anim.starvation():
                    print('The fish ' + str(anim.name) + ' died at the age of ' + str(anim.age) +
                          ' years\nBecause he ran out of food!')
                    self.delete_animal_from_board(anim)
                    self.anim.remove(anim)
                    continue
                elif anim.directionH == 1:
                    if anim.x == self.aqua_width - 9:
                        anim.directionH = 0
                        self.delete_animal_from_board(anim)
                        self.print_animal_on_board(anim)
                    else:
                        self.right(anim)
                    if anim.y != 3 and anim.directionV == 1:
                        self.up(anim)
                    elif anim.y == 3 and anim.directionV == 1:
                        anim.directionV = 0
                    if anim.y != self.aqua_height - 10 and anim.directionV == 0:
                        self.down(anim)
                    elif anim.y == self.aqua_height - 10 and anim.directionV == 0:
                        anim.directionV = 1
                elif anim.directionH == 0:
                    if anim.x == 1:
                        anim.directionH = 1
                        self.delete_animal_from_board(anim)
                        self.print_animal_on_board(anim)
                    else:
                        self.left(anim)
                    if anim.y != 3 and anim.directionV == 1:
                        self.up(anim)
                    elif anim.y == 3 and anim.directionV == 1:
                        anim.directionV = 0
                    if anim.y != self.aqua_height - 10 and anim.directionV == 0:
                        self.down(anim)
                    elif anim.y == self.aqua_height - 10 and anim.directionV == 0:
                        anim.directionV = 1
        self.turn += 1

    def print_all(self):
        """
        Prints all the animals in the aquarium
        """
        for i in self.anim:
            print(i)

    def feed_all(self):
        """
        feed all the animals in the aquarium
        """
        for animal in self.anim:
            animal.add_food(10)

    def add_animal(self, name, age, x, y, directionH, directionV, animal_type):

        if animal_type == 'sc' or animal_type == 'mo':
            if x > self.aqua_width - 9:
                x = self.aqua_width - 9
            if animal_type == 'sc':
                if y >= self.aqua_height - 10:
                    y = self.aqua_height - 10
            elif animal_type == 'mo':
                if y >= self.aqua_height - 8:
                    y = self.aqua_height - 8
            if self.check_if_free(x, y):
                return self.add_fish(name, age, x, y, directionH, directionV, animal_type)
            else:
                print('The place is not available! Please try again later')
        elif animal_type == 'oc' or animal_type == 'sh':
            if x > self.aqua_width - 8:
                x = self.aqua_width - 8
            if animal_type == 'oc':
                y = self.aqua_height - 5
                if self.check_if_free(x - 2, y - 1):
                    return self.add_crab(name, age, x, y, directionH, animal_type)
                else:
                    print('The place is not available! Please try again later')
            elif animal_type == 'sh':
                y = self.aqua_height - 4
                if self.check_if_free(x - 1, y - 2):
                    return self.add_crab(name, age, x, y, directionH, animal_type)
        else:
            return False

    def several_steps(self) -> None:
        """
        Managing several steps
        :rtype: object
        """
        while True:
            try:
                x = int(input('How many steps do you want to take?'))
            except ValueError:
                print('')
            else:
                break
        for i in range(0, x):
            self.next_turn()


