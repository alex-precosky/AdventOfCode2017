from enum import Enum
import numpy as np





def are_opposites(movement1, movement2):
    if (movement1 == "n" and movement2 == "s") or \
       (movement1 == "s" and movement2 == "n") or \
       (movement1 == "ne" and movement2 == "sw") or \
       (movement1 == "sw" and movement2 == "ne") or \
       (movement1 == "se" and movement2 == "nw") or \
       (movement1 == "nw" and movement2 == "se"):
        return True
    else:
        return False


def get_adjacent_resultant(movement1, movement2):
    if (movement1 == "n" and movement2 == "se") or \
       (movement1 == "se" and movement2 == "n"):
        return "ne"
    
    if(movement1 == "ne" and movement2 == "s") or \
       (movement1 == "s" and movement2 == "ne"):
        return "se"

    if(movement1 == "se" and movement2 == "sw") or \
       (movement1 == "sw" and movement2 == "se"):
        return "s"

    if(movement1 == "s" and movement2 == "nw") or \
       (movement1 == "nw" and movement2 == "s"):
        return "sw"

    if(movement1 == "sw" and movement2 == "n") or \
       (movement1 == "n" and movement2 == "sw"):
        return "nw"

    if(movement1 == "nw" and movement2 == "ne") or \
       (movement1 == "ne" and movement2 == "nw"):
        return "n"

    # if we reach here, there's no adjacency
    return None


def cancel_adjacent_movements(movements):
    # for each movement, look for a movement that could be cancelle dout

    # mark which movements we'll elminate
    eliminate = [False for i in range(len(movements))]

    # and elements we'll add
    replacements = []

    for i, movement_i in enumerate(movements):
        j = i+1
        for movement_j in movements[i+1:]:

            if eliminate[i] != True and eliminate[j] != True:
                resultant = get_adjacent_resultant(movement_i, movement_j)
                if resultant is not None:                
                    eliminate[i] = True
                    eliminate[j] = True
                    replacements.append(resultant)
            j += 1
    
    return_list = [movement for i, movement in enumerate(movements) if eliminate[i] != True]
    return_list.extend(replacements)
    return return_list

from itertools import compress
def cancel_adjacent_movements_2(movements):
    # for each movement, look for a movement that could be cancelle dout

    # mark which movements we'll elminate
    keep = [True for i in range(len(movements))]

    # and elements we'll add
    replacements = []

    for i, movement_i in enumerate(movements):
        j = i+1
        for movement_j in movements[i+1:]:

            if keep[i] != False and keep[j] != False:
                resultant = get_adjacent_resultant(movement_i, movement_j)
                if resultant is not None:                
                    keep[i] = False
                    keep[j] = False
                    replacements.append(resultant)
            j += 1
    
    return_list = list(compress(movements, keep))
    return_list.extend(replacements)
    return return_list



def cancel_opposite_movements(movements):
    # for each movement, look for a movement that could be cancelled out

    # mark which movements we'll elminate
    eliminate = [False for i in range(len(movements))]

    for i, movement_i in enumerate(movements):
        j = i+1
        for movement_j in movements[i+1:]:

            if eliminate[i] != True and eliminate[j] != True:
                if are_opposites(movement_i, movement_j):
                    eliminate[i] = True
                    eliminate[j] = True
            j += 1
    
    return [movement for i, movement in enumerate(movements) if eliminate[i] != True]


def simplify_movements(movements):
    simplified_1 = cancel_opposite_movements(movements)
    simplified_2 = cancel_adjacent_movements(simplified_1)
    return simplified_2


if __name__ == "__main__":
    movements = open("input.txt", "r").readline().strip().split(",")
    num_movements = len(movements) 

    simplified_movements = simplify_movements(movements)
    num_simplified_movements = len(simplified_movements)

    print(f"# movements: {num_movements}  # simplified movements: {num_simplified_movements}")


    # for part 2, keep building subsets of the movement list
    max_steps = 0
    incremental_movements = []

    for i in range(len(movements)):
        incremental_movements.append(movements[i])
        incremental_movements = simplify_movements(incremental_movements)

        num_simplified_movements = len(incremental_movements)

        if num_simplified_movements > max_steps:
            max_steps = num_simplified_movements

        print(f"Part 2 iteration {i} of {num_movements}")

    print(f"Maximum distance: {max_steps}")
