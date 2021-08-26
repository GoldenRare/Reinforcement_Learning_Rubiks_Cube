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
    LEFT = 2
    LEFT_PRIME = 3
    FRONT = 4
    FRONT_PRIME = 5


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
        # Standard 9 side rotation
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

    def rotate_left(self):
        bitmask_front_left_45 = 0b100100100
        bitmask_top_right_36 = 0b100100100000000000000000000000000000000000000
        bitmask_back_left_14 = 0b001000000000000000000000000
        bitmask_back_left_20 = 0b000001000000000000000000000
        bitmask_back_left_26 = 0b000000001000000000000000000
        bitmask_bottom_right_23 = 0b000000100000000000000000000000000000000000000000000000
        bitmask_bottom_right_29 = 0b000100000000000000000000000000000000000000000000000000
        bitmask_bottom_right_35 = 0b100000000000000000000000000000000000000000000000000000
        # Standard 9 side rotation
        bitmask_left_left_2 = 0b000100001000000000000000000000000000
        bitmask_left_left_4 = 0b000000010000000000000000000000000000
        bitmask_left_left_6 = 0b000000100000000000000000000000000000
        bitmask_left_right_2 = 0b100001000000000000000000000000000000
        bitmask_left_right_6 = 0b001000000000000000000000000000000000
        bitmask_left_right_4 = 0b010000000000000000000000000000000000

        for c in Color:
            # Find the bits on the bitmask
            extracted_bits_front_left_45 = self.squares[c.value] & bitmask_front_left_45
            extracted_bits_top_right_36 = self.squares[c.value] & bitmask_top_right_36
            extracted_bits_back_left_14 = self.squares[c.value] & bitmask_back_left_14
            extracted_bits_back_left_20 = self.squares[c.value] & bitmask_back_left_20
            extracted_bits_back_left_26 = self.squares[c.value] & bitmask_back_left_26
            extracted_bits_bottom_right_23 = self.squares[c.value] & bitmask_bottom_right_23
            extracted_bits_bottom_right_29 = self.squares[c.value] & bitmask_bottom_right_29
            extracted_bits_bottom_right_35 = self.squares[c.value] & bitmask_bottom_right_35
            extracted_bits_left_left_2 = self.squares[c.value] & bitmask_left_left_2
            extracted_bits_left_left_4 = self.squares[c.value] & bitmask_left_left_4
            extracted_bits_left_left_6 = self.squares[c.value] & bitmask_left_left_6
            extracted_bits_left_right_2 = self.squares[c.value] & bitmask_left_right_2
            extracted_bits_left_right_6 = self.squares[c.value] & bitmask_left_right_6
            extracted_bits_left_right_4 = self.squares[c.value] & bitmask_left_right_4
            # Remove the bits on the bitmask
            self.squares[c.value] ^= extracted_bits_front_left_45 | extracted_bits_top_right_36 \
                                                                  | extracted_bits_back_left_14 \
                                                                  | extracted_bits_back_left_20 \
                                                                  | extracted_bits_back_left_26 \
                                                                  | extracted_bits_bottom_right_23 \
                                                                  | extracted_bits_bottom_right_29 \
                                                                  | extracted_bits_bottom_right_35 \
                                                                  | extracted_bits_left_left_2 \
                                                                  | extracted_bits_left_left_4 \
                                                                  | extracted_bits_left_left_6 \
                                                                  | extracted_bits_left_right_2 \
                                                                  | extracted_bits_left_right_6 \
                                                                  | extracted_bits_left_right_4
            # Perform the rotation
            self.squares[c.value] ^= extracted_bits_front_left_45 << 45 | extracted_bits_top_right_36 >> 36 \
                                                                        | extracted_bits_back_left_14 << 14 \
                                                                        | extracted_bits_back_left_20 << 20 \
                                                                        | extracted_bits_back_left_26 << 26 \
                                                                        | extracted_bits_bottom_right_23 >> 23 \
                                                                        | extracted_bits_bottom_right_29 >> 29 \
                                                                        | extracted_bits_bottom_right_35 >> 35 \
                                                                        | extracted_bits_left_left_2 << 2 \
                                                                        | extracted_bits_left_left_4 << 4 \
                                                                        | extracted_bits_left_left_6 << 6 \
                                                                        | extracted_bits_left_right_2 >> 2 \
                                                                        | extracted_bits_left_right_6 >> 6 \
                                                                        | extracted_bits_left_right_4 >> 4

    def rotate_left_prime(self):
        self.rotate_left()
        self.rotate_left()
        self.rotate_left()

    def rotate_front(self):
        bitmask_right_left_42 = 0b100000000000
        bitmask_right_left_38 = 0b100000000000000
        bitmask_right_left_34 = 0b100000000000000000
        bitmask_top_right_21 = 0b100000000000000000000000000000000000000
        bitmask_top_right_23 = 0b10000000000000000000000000000000000000
        bitmask_top_right_25 = 0b1000000000000000000000000000000000000
        bitmask_left_left_3 = 0b1000000000000000000000000000000000
        bitmask_left_left_7 = 0b1000000000000000000000000000000
        bitmask_left_left_11 = 0b1000000000000000000000000000
        bitmask_bottom_right_20 = 0b100000000000000000000000000000000000000000000000000000
        bitmask_bottom_right_22 = 0b10000000000000000000000000000000000000000000000000000
        bitmask_bottom_right_24 = 0b1000000000000000000000000000000000000000000000000000
        # Standard 9 side rotation
        bitmask_front_left_2 = 0b000100001
        bitmask_front_left_4 = 0b000000010
        bitmask_front_left_6 = 0b000000100
        bitmask_front_right_2 = 0b100001000
        bitmask_front_right_6 = 0b001000000
        bitmask_front_right_4 = 0b010000000

        for c in Color:
            # Find the bits on the bitmask
            extracted_bits_right_left_42 = self.squares[c.value] & bitmask_right_left_42
            extracted_bits_right_left_38 = self.squares[c.value] & bitmask_right_left_38
            extracted_bits_right_left_34 = self.squares[c.value] & bitmask_right_left_34
            extracted_bits_top_right_21 = self.squares[c.value] & bitmask_top_right_21
            extracted_bits_top_right_23 = self.squares[c.value] & bitmask_top_right_23
            extracted_bits_top_right_25 = self.squares[c.value] & bitmask_top_right_25
            extracted_bits_left_left_3 = self.squares[c.value] & bitmask_left_left_3
            extracted_bits_left_left_7 = self.squares[c.value] & bitmask_left_left_7
            extracted_bits_left_left_11 = self.squares[c.value] & bitmask_left_left_11
            extracted_bits_bottom_right_20 = self.squares[c.value] & bitmask_bottom_right_20
            extracted_bits_bottom_right_22 = self.squares[c.value] & bitmask_bottom_right_22
            extracted_bits_bottom_right_24 = self.squares[c.value] & bitmask_bottom_right_24
            extracted_bits_front_left_2 = self.squares[c.value] & bitmask_front_left_2
            extracted_bits_front_left_4 = self.squares[c.value] & bitmask_front_left_4
            extracted_bits_front_left_6 = self.squares[c.value] & bitmask_front_left_6
            extracted_bits_front_right_2 = self.squares[c.value] & bitmask_front_right_2
            extracted_bits_front_right_6 = self.squares[c.value] & bitmask_front_right_6
            extracted_bits_front_right_4 = self.squares[c.value] & bitmask_front_right_4
            # Remove the bits on the bitmask
            self.squares[c.value] ^= extracted_bits_right_left_42 | extracted_bits_right_left_38 \
                                                                  | extracted_bits_right_left_34 \
                                                                  | extracted_bits_top_right_21 \
                                                                  | extracted_bits_top_right_23 \
                                                                  | extracted_bits_top_right_25 \
                                                                  | extracted_bits_left_left_3 \
                                                                  | extracted_bits_left_left_7 \
                                                                  | extracted_bits_left_left_11 \
                                                                  | extracted_bits_bottom_right_20 \
                                                                  | extracted_bits_bottom_right_22 \
                                                                  | extracted_bits_bottom_right_24 \
                                                                  | extracted_bits_front_left_2 \
                                                                  | extracted_bits_front_left_4 \
                                                                  | extracted_bits_front_left_6 \
                                                                  | extracted_bits_front_right_2 \
                                                                  | extracted_bits_front_right_6 \
                                                                  | extracted_bits_front_right_4
            # Perform the rotation
            self.squares[c.value] ^= extracted_bits_right_left_42 << 42 | extracted_bits_right_left_38 << 38 \
                                                                        | extracted_bits_right_left_34 << 34 \
                                                                        | extracted_bits_top_right_21 >> 21 \
                                                                        | extracted_bits_top_right_23 >> 23 \
                                                                        | extracted_bits_top_right_25 >> 25 \
                                                                        | extracted_bits_left_left_3 << 3 \
                                                                        | extracted_bits_left_left_7 << 7 \
                                                                        | extracted_bits_left_left_11 << 11 \
                                                                        | extracted_bits_bottom_right_20 >> 20 \
                                                                        | extracted_bits_bottom_right_22 >> 22 \
                                                                        | extracted_bits_bottom_right_24 >> 24 \
                                                                        | extracted_bits_front_left_2 << 2 \
                                                                        | extracted_bits_front_left_4 << 4 \
                                                                        | extracted_bits_front_left_6 << 6 \
                                                                        | extracted_bits_front_right_2 >> 2 \
                                                                        | extracted_bits_front_right_6 >> 6 \
                                                                        | extracted_bits_front_right_4 >> 4

    def rotate_front_prime(self):
        self.rotate_front()
        self.rotate_front()
        self.rotate_front()


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

cube.rotate_left()
cube.rotate_up()
cube.rotate_up()
cube.rotate_front()
cube.rotate_left_prime()
cube.rotate_up_prime()
cube.rotate_up_prime()
cube.rotate_left_prime()
cube.rotate_front_prime()

cube.rotate_front()
cube.rotate_left()
cube.rotate_up()
cube.rotate_up()
cube.rotate_left()
cube.rotate_front_prime()
cube.rotate_up_prime()
cube.rotate_up_prime()
cube.rotate_left_prime()

print('\n')
for co in Color:
    print("{0:b}".format(cube.squares[co.value]))

