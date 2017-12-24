# want to find all possible bridges

# put pieces in a set. each item is a 2-tuple

# look through set for valid parts


valid_bridges = []

def parse_line(line):
    # returns a two tuple representing the piece
    tokens = tuple(line.strip().split("/"))
    piece = ( int(tokens[0]), int(tokens[1]) )
    return piece


def lines_to_set(lines):
    return_set = set()
    pieces = [parse_line(line) for line in lines]

    [return_set.add(piece) for piece in pieces]
    
    return return_set


def find_valid_pieces(piece_set, connector):
    
    valid_pieces = []

    for piece in piece_set:
        if connector in piece:
            valid_pieces.append(piece)

    return tuple(valid_pieces)


def build_bridge(pieces_left_set, pieces_used_set, connector):

    valid_pieces = find_valid_pieces(pieces_left_set, connector)

  #  print(f"valid pieces: {valid_pieces}")

    for valid_piece in valid_pieces:

        next_connector = valid_piece[0]
        if valid_piece[0] == connector:
            next_connector = valid_piece[1]

       # print(f"piece: {valid_piece}  next_connector: {next_connector}")

        # remove piece from the piece set the next recursion level gets
        next_level_pieces_left_set = pieces_left_set.copy()
        next_level_pieces_left_set.remove(valid_piece)

        next_level_pieces_used_set = pieces_used_set.copy()
        next_level_pieces_used_set.add(valid_piece)

        build_bridge(next_level_pieces_left_set, next_level_pieces_used_set, next_connector)


    if len(valid_pieces) == 0:
        valid_bridges.append(pieces_used_set)
        

def calc_bridge_strength(bridge):
    strength = 0

    for piece in bridge:
        strength += piece[0]
        strength += piece[1]

    return strength


if __name__ == "__main__":
    
    lines = open("input.txt", "r").readlines()
    
    piece_set = lines_to_set(lines)
    pieces_used_set = set()

    build_bridge(piece_set, pieces_used_set, 0)

    max_strength = 0
    max_length = 0

    for bridge in valid_bridges:
        strength = calc_bridge_strength(bridge)
        length = len(bridge)

        if strength > max_strength:
            max_strength = strength

        if length > max_length:
            max_length = length


    strength_of_max_length = 0
    for bridge in valid_bridges:
        if len(bridge) == max_length:
            strength = calc_bridge_strength(bridge)
            if strength > strength_of_max_length:
                strength_of_max_length = strength

    print(f"Max strength: {max_strength}")
    print(f"Strength of max length: {strength_of_max_length}")

    # not 600
