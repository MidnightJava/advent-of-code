# copied from https://github.com/RichRat/pyxercise/blob/master/util/vector.py

import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from utils.math_util import greatest_common_divisor

# integer vector class for handling vectors pointing to position in a 2d list
# note: < and > apply to both x and y
class IntVector2:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return IntVector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return IntVector2(self.x - other.x, self.y - other.y)

    def __mul__(self, factor):
        return IntVector2(self.x * factor, self.y * factor)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

    def __mod__(self, mod_vect):
        return  IntVector2(self.x % mod_vect.x, self.y % mod_vect.y)

    def of_grid(self, grid):
        return grid[self.y][self.x]

    def set_grid(self, grid, val):
        grid[self.y][self.x] = val

    def is_in_bounds(self, grid):
        return 0 <= self.y < len(grid) and 0 <= self.x < len(grid[0])

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __hash__(self):
        return hash(str(self))

    def normalize(self):
        gcd = greatest_common_divisor(abs(self.x), abs(self.y))
        return IntVector2(int(self.x / gcd), int(self.y / gcd))

    def to_tuple(self):
        return self.x, self.y


def to_vect_list(tuples: list[(int, int)]):
    return [IntVector2(x, y) for x, y in tuples]

null_vector = IntVector2(0,0)



#### test code ####
# a = IntVector2(1,2)
# b = IntVector2(2,1)
#
# print("Vect test result " + str((a + b) * 2 - IntVector2(1,3) == IntVector2(5,3)))
# print("vect norm test " + str(IntVector2(12,3).normalize() == IntVector2(4, 1)))