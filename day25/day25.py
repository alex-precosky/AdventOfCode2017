import numpy as np


class state_c:
    state = 'A'
    n = 100000
    tape = np.zeros(n)
    position = int(n/2)

    # the state transition table uses a dictionary
    # key is (current state, current tape value)
    # value is (value to write, 1 for move to right 0 for left, next state)
    next_state = dict()
    next_state[('A', 0)] = (1, 1, 'B')
    next_state[('A', 1)] = (0, 0, 'C')
    next_state[('B', 0)] = (1, 0, 'A')
    next_state[('B', 1)] = (1, 0, 'D')
    next_state[('C', 0)] = (1, 1, 'D')
    next_state[('C', 1)] = (0, 1, 'C')
    next_state[('D', 0)] = (0, 0, 'B')
    next_state[('D', 1)] = (0, 1, 'E')
    next_state[('E', 0)] = (1, 1, 'C')
    next_state[('E', 1)] = (1, 0, 'F')
    next_state[('F', 0)] = (1, 0, 'E')
    next_state[('F', 1)] = (1, 1, 'A')

    def step(self):
        value = self.tape[self.position]

        next_state_values = self.next_state[(self.state, value)]

        self.tape[self.position] = next_state_values[0]

        direction = next_state_values[1]
        if direction == 1:
            self.position += 1
        else:
            self.position -= 1

        self.state = next_state_values[2]

    def get_checksum(self):
        return self.tape.sum()


if __name__ == "__main__":
    n_steps = 12656374

    state = state_c()

    for i in range(n_steps):
        if i % 1000 == 0:
            print(i)

        state.step()

    part1_checksum = state.get_checksum()
    print(f"Part 1 checksum: {part1_checksum}")
