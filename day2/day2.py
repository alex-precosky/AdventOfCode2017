import numpy as np


# subtract the largest integer in the text line minus the smallest
def process_line_part1(line):

    tokens = np.array(line.split('\t'))

    int_tokens = np.array([int(a) for a in tokens])

    line_difference = int_tokens.max() - int_tokens.min()

    return line_difference


# find the only two numbers that evenly divide in the row then divide them
def process_line_part2(line):

    tokens = np.array(line.split('\t'))

    int_tokens = np.array([int(a) for a in tokens])

    int_tokens.sort()
    print(int_tokens)
    int_tokens = int_tokens[::-1]

    for i, token1 in enumerate(int_tokens):
        for token2 in int_tokens[i+1:]:

            if token1 % token2 == 0:
                return token1 / token2


if __name__ == "__main__":
    infile = open("input.txt")
    differences = [process_line_part1(line) for line in infile.readlines()]
    infile.close()

    infile = open("input.txt")
    quotients = [process_line_part2(line) for line in infile.readlines()]

    print("Part 1")
    print(np.array(differences).sum())

    print("Part 2")
    print(np.array(quotients).sum())
