from enum import Enum, auto
import numpy as np
import pdb

class directions(auto):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

class node_states(Enum):
    CLEAN = 0
    INFECTED = 1
    WEAKENED = 2
    FLAGGED = 3

class infection_state_c:
    
    def __init__(self, n, input_array):
        # n is the size of a length of the virus array

        self.n = n
        self.direction = directions.UP

        m = input_array.shape[0]

        self.grid = np.zeros((n, n), dtype=int)
        self.grid[n//2:n//2+m, n//2:n//2+m] = input_array

        self.current_x = n//2 + m//2
        self.current_y = n//2 + m//2

        self.num_bursts_caused_infections = 0


    def burst(self):
        
        if self.grid[self.current_y][self.current_x] == 1:
            current_was_infected = True
        else:
            current_was_infected = False

        self.turn(current_was_infected)
        
        if current_was_infected is True:
            self.grid[self.current_y][self.current_x] = node_states.CLEAN.value
        else:
            self.grid[self.current_y][self.current_x] = node_states.INFECTED.value
            self.num_bursts_caused_infections += 1

        if self.direction == directions.UP:
            self.current_y -= 1
        elif self.direction == directions.RIGHT:
            self.current_x += 1
        elif self.direction == directions.DOWN:
            self.current_y += 1
        else:
            self.current_x -= 1


    def turn(self, is_right):
        current_direction = self.direction

        if current_direction == directions.UP:
            if is_right is True:
                new_direction = directions.RIGHT
            else:
                new_direction = directions.LEFT
        elif current_direction == directions.RIGHT:
            if is_right is True:
                new_direction = directions.DOWN
            else:
                new_direction = directions.UP
        elif current_direction == directions.DOWN:
            if is_right is True:
                new_direction = directions.LEFT
            else:
                new_direction = directions.RIGHT
        else:
            if is_right is True:
                new_direction = directions.UP
            else:
                new_direction = directions.DOWN

        self.direction = new_direction
                

    def burst_part_2(self):
        
        cell_before_state = self.grid[self.current_y][self.current_x]

        if cell_before_state == node_states.CLEAN.value:
            self.turn(is_right = False)
        elif cell_before_state == node_states.WEAKENED.value:
            pass # dont turn
        elif cell_before_state == node_states.INFECTED.value:
            self.turn(is_right = True)
        elif cell_before_state == node_states.FLAGGED.value:
            self.turn(is_right = True)
            self.turn(is_right = True)
        else:
            print("bad")

        if cell_before_state == node_states.CLEAN.value:
            new_state = node_states.WEAKENED
        elif cell_before_state == node_states.WEAKENED.value:
            new_state = node_states.INFECTED
            self.num_bursts_caused_infections += 1
        elif cell_before_state == node_states.INFECTED.value:
            new_state = node_states.FLAGGED
        elif cell_before_state == node_states.FLAGGED.value:
            new_state = node_states.CLEAN
        else:
            print("bad")

        self.grid[self.current_y][self.current_x] = new_state.value

        if self.direction == directions.UP:
            self.current_y -= 1
        elif self.direction == directions.RIGHT:
            self.current_x += 1
        elif self.direction == directions.DOWN:
            self.current_y += 1
        elif self.direction == directions.LEFT:
            self.current_x -= 1
        else:
            print("bad")


def read_input(input_lines):
    # list of strings returning a 2d numpy int array

    m = len(input_lines)
    return_array = np.zeros((m, m), dtype=int)

    for i, line in enumerate(input_lines):
        return_array[i,:] = [1 if char == '#' else 0 for char in line.strip()]

    return return_array


if __name__ == "__main__":
    
    input_lines = open("input.txt", "r").readlines()
    input_array = read_input(input_lines)

    n = 100
    infection_state = infection_state_c(10003, input_array)


    
    for i in range(10000):
        infection_state.burst()
        if i % 1000 == 0:
            print(f"Iteration {i}")
    
    print(f"Num bursts that caused infections: {infection_state.num_bursts_caused_infections}")


    n = 100
    input_lines = open("input.txt", "r").readlines()
    input_array = read_input(input_lines)
    infection_state = infection_state_c(10003, input_array)

    for i in range(10000000):
        infection_state.burst_part_2()
        if i % 1000 == 0:
            print(f"Iteration {i}")
    
    print(f"Num bursts that caused infections: {infection_state.num_bursts_caused_infections}")
