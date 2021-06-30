from enum import Enum


# Colors of a Rubik's Cube
class Color(Enum):
    RED = 0
    GREEN = 1
    ORANGE = 2
    BLUE = 3
    YELLOW = 4
    WHITE = 5


# Ways to rotate a Rubik's Cube according to https://ruwix.com/the-rubiks-cube/notation/advanced/
class Rotation(Enum):
    UP = 0
    UP_PRIME = 1


class RubiksCube:

    # Initializes a Rubik's Cube to its default configuration
    def __init__(self):
        # Squares are indexed by color and contains a bitboard of the location of the 9 colored squares
        # By default, most significant bits are the 9 white squares, then yellow, blue, orange, green, and red
        # For bits group of 9, the least significant bit is the bottom right, bottom middle, ..., middle right, ...,
        # top left. The sides of the cube are red, green, orange, and blue; bottom is white; top is yellow.
        # For bitboard reasons, assume by default you are facing the red side, and the rest of the sides are accessed by
        # turning the cube horizontally; the top (yellow) is accessed by turning the cube down; the bottom (white) is
        # accessed by turning the cube up.
        self.squares = default_rubiks_cube()

    def rotate_up(self):
        bitmask_sides = 0b111000000111000000111000000111000000
        bitmask_top_left_2 = 0b000100001000000000000000000000000000000000000
        bitmask_top_left_4 = 0b000000010000000000000000000000000000000000000
        bitmask_top_left_6 = 0b000000100000000000000000000000000000000000000
        bitmask_top_right_2 = 0b100001000000000000000000000000000000000000000
        bitmask_top_right_6 = 0b001000000000000000000000000000000000000000000
        bitmask_top_right_4 = 0b010000000000000000000000000000000000000000000
        erase_overflow = 0b111111111111111111111111111111111111

        for c in Color:
            # Find the bits on the bitmask
            extracted_bits_sides = self.squares[c.value] & bitmask_sides
            extracted_bits_top_left_2 = self.squares[c.value] & bitmask_top_left_2
            extracted_bits_top_left_4 = self.squares[c.value] & bitmask_top_left_4
            extracted_bits_top_left_6 = self.squares[c.value] & bitmask_top_left_6
            extracted_bits_top_right_2 = self.squares[c.value] & bitmask_top_right_2
            extracted_bits_top_right_6 = self.squares[c.value] & bitmask_top_right_6
            extracted_bits_top_right_4 = self.squares[c.value] & bitmask_top_right_4
            # Remove the bits on the bitmask
            self.squares[c.value] ^= extracted_bits_sides | extracted_bits_top_left_2 | extracted_bits_top_left_4 \
                                                          | extracted_bits_top_left_6 | extracted_bits_top_right_2 \
                                                          | extracted_bits_top_right_6 | extracted_bits_top_right_4
            # Perform the rotation
            self.squares[c.value] ^= (extracted_bits_sides << 27 | extracted_bits_sides >> 9) & erase_overflow
            self.squares[c.value] ^= extracted_bits_top_left_2 << 2 | extracted_bits_top_left_4 << 4 \
                                                                    | extracted_bits_top_left_6 << 6 \
                                                                    | extracted_bits_top_right_2 >> 2 \
                                                                    | extracted_bits_top_right_6 >> 6 \
                                                                    | extracted_bits_top_right_4 >> 4

    def rotate_up_prime(self):
        self.rotate_up()
        self.rotate_up()
        self.rotate_up()


def default_rubiks_cube():
    squares = []
    init = 0b111111111
    for _ in Color:
        squares.append(init)
        init <<= 9
    return squares


cube = RubiksCube()
for co in Color:
    print("{0:b}".format(cube.squares[co.value]))

cube.rotate_up()
cube.rotate_up_prime()
print('\n')
for co in Color:
    print("{0:b}".format(cube.squares[co.value]))

