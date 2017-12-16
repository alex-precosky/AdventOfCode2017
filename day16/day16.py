import collections


def spin(programs_letters, n):
    d = collections.deque(programs_letters)
    d.rotate(n)

    return "".join(d)


def swap(programs_letters, program1, program2):
    programs_list = list(programs_letters)
    temp = programs_list[program1]

    programs_list[program1] = programs_list[program2]
    programs_list[program2] = temp

    return "".join(programs_list)


def execute_move(move, programs_letters):

    if move[0] == "s":
        distance = int(move.split('s')[1])
        programs_letters = spin(programs_letters, distance)
    elif move[0] == "x":
        programs = move[1:].split("/")
        programs_letters = swap(programs_letters, int(programs[0]), int(programs[1]))
    elif move[0] == "p":
        programs = move[1:].split("/")
        # get the ascii code of the letter, then subtract from that so that a = 0
        program1 = programs_letters.find(move[1])
        program2 = programs_letters.find(move[3])

        programs_letters = swap(programs_letters, program1, program2)

    return programs_letters


def execute_moves(moves, programs):
    # returns the programs_letters after all of the moves have been performed
    for move in moves:
        programs = execute_move(move, programs)

    return programs






if __name__ == "__main__":

    inputline = open("input.txt", "r").readline()
    moves = inputline.split(",")

    programs = "abcdefghijklmnop"

    programs_reordered = execute_moves(moves, programs)
    programs_reordered_part1 = programs_reordered

    print(f"part 1: {programs_reordered}")

    dp_lut = dict()


    # part 2    
    programs_reordered = programs
    for iteration in range(1000000000):
        if programs_reordered in dp_lut:
            programs_reordered = dp_lut[programs_reordered]
        else:
            programs_before = programs_reordered
            programs_reordered = execute_moves(moves, programs_reordered)
            dp_lut[programs_before] = programs_reordered

        if iteration % 10000 == 0:
            print(iteration)

print(programs_reordered)
