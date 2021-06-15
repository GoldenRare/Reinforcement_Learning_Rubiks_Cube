from enum import Enum


# Colors of a Rubik's Cube
class Color(Enum):
    RED = 0
    GREEN = 1
    ORANGE = 2
    BLUE = 3
    YELLOW = 4
    WHITE = 5


class RubiksCube:

    # Initializes a Rubik's Cube to its default configuration
    def __init__(self):
        # Squares are indexed by color and contains a bitboard of the location of the 9 colored squares
        # By default, most significant bits are the 9 white squares, then yellow, blue, orange, green, and red
        self.squares = default_rubiks_cube()


def default_rubiks_cube():
    squares = []
    init = 0b111111111
    for _ in Color:
        squares.append(init)
        init <<= 9
    return squares


cube = RubiksCube()
for c in Color:
    print("{0:b}".format(cube.squares[c.value]))

