import numpy as np
from enum import Enum


class direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class maze_state_c:

    def __init__(self, maze_text):

        self.position_y = 0
        self.direction = direction.DOWN

        self.maze = self.read_maze(maze_text)
        self.position_x = self.find_maze_start_x(self.maze)

        self.letters_visited = []

    def step_maze(self):
        # returns True if finished the maze. otherwise, false

        print(f"x={self.position_x} y={self.position_y}")

        x = self.position_x
        y = self.position_y
        direction = self.direction
        char = self.maze[y][x]

        if char == b'|' or char == b'-':
            if direction == direction.DOWN:
                self.position_y += 1
            elif direction == direction.UP:
                self.position_y -= 1
            elif direction == direction.RIGHT:
                self.position_x += 1
            else:
                self.position_x -= 1
        elif char == b'+':
            if direction == direction.UP or direction == direction.DOWN:
                if self.maze[y][x-1] == '':
                    self.direction = direction.RIGHT
                    self.position_x += 1
                    print("right")
                else:
                    self.direction = direction.LEFT
                    self.position_x -= 1
            else:
                if self.maze[y-1][x] == '':
                    self.direction = direction.DOWN
                    self.position_y += 1
                else:
                    self.direction = direction.UP
                    self.position_y -= 1
        else:
            self.letters_visited.append(chr(ord(char)))

            if direction == direction.UP:
                self.position_y -= 1
            elif direction == direction.DOWN:
                self.position_y += 1
            elif direction == direction.LEFT:
                self.position_x -= 1
            else:
                self.position_x += 1

            if self.maze[self.position_y][self.position_x] == '':
                return True

        return False

    def read_maze(self, lines):
        # returns an numpy array of the input file. top left character is [0][0]

        width = 0
        for line in lines:
            if len(line) > width:
                width = len(line)

        height = len(lines)

        return_array = np.chararray((height, width))

        for i in range(height):
            for j in range(width):
                return_array[i][j] = lines[i][j]

        return return_array

    def find_maze_start_x(self, maze):
        # returns (x,y) of the entry point of the maze

        line0 = maze[0]
        x = 0
        for char in line0:

            if char == b"|":
                return x
            else:
                x += 1


if __name__ == "__main__":
    maze_lines = open("input.txt", "r").readlines()
    maze_state = maze_state_c(maze_lines)

    finished = False
    step_counter = 0
    while finished is not True:
        step_counter += 1
        finished = maze_state.step_maze()

    letters_visited = ''.join(maze_state.letters_visited)
    print(f"Part 1: {letters_visited}")
    print(f"Part 2: {step_counter}")
