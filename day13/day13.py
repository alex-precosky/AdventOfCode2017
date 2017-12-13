class scanner_c:
    position = 0
    range = 0
    direction = 1 # 1 means increasing in position, 0 means decreasing

class game_state_c:
    packet_depth = -1
    scanner_states = dict()
    depths_caught = dict() # depth : severity

def step(game_state, delaying):

    if delaying == False:
        # move the packet ahead one
        game_state.packet_depth += 1

        # check if caught, but only if there's a scanner at this depth
        packet_depth = game_state.packet_depth
        if packet_depth in game_state.scanner_states:
            scanner_position = game_state.scanner_states[packet_depth].position
            if scanner_position == 0:
                game_state.depths_caught[packet_depth] = packet_depth * game_state.scanner_states[packet_depth].range


    # advance the scanner positions
    for value in game_state.scanner_states.values():
        if value.direction == 1:
            value.position += 1
            if value.position == value.range-1:
                value.direction = 0
        else:
            value.position -= 1
            if value.position == 0:
                value.direction = 1

    return game_state


def fast_delay(game_state, delay):
    for key, value in game_state.scanner_states.items():
        i = delay % ((value.range-1) * 2)
        if i > value.range-1:
            i = 2*(value.range-1) - i
        value.position = i

        if (delay // (value.range-1)) % 2 == 0:
            value.direction = 1
        else:
            value.direction = 0

        game_state.scanner_states[key] = value
    
#    for state in game_state.scanner_states.values():
#        print(state.direction)

    return game_state

def reset_game_state(game_state):
    game_state.packet_depth = -1
    game_state.depths_caught = dict()
    for key, value in game_state.scanner_states.items():
        game_state.scanner_states[key].position = 0
        game_state.scanner_states[key].direction = 1

    return game_state
  


if __name__ == "__main__":
    # simulating a firewall game. the AoC problem doesn't call it a game
    # but it sounds like one
    
    in_file = open("input.txt", "r")

    # build a dictionary of {depth: scanner_c}
    scanners = dict()

    for line in in_file.readlines():
        numbers = line.strip().split(":")
        depth = int(numbers[0])
        range = int(numbers[1])
        
        scanner = scanner_c()
        scanner.depth = depth
        scanner.range = range
        scanner.position = 0
        scanners[depth] = scanner


    # initialize the game
    game_state = game_state_c()
    game_state.scanner_states = scanners
    game_state.packet_depth = -1

    # find the maximum depth of the scanners
    max_depth = 0
    for key, value in game_state.scanner_states.items():
        if value.depth > max_depth:
            max_depth = value.depth


    while game_state.packet_depth < max_depth:
        game_state = step(game_state, False)

    total_severity = 0
    for severity in game_state.depths_caught.values():
        total_severity += severity

    print(f"Total severity: {total_severity}")
    

    # Part 2
    finished = False
    current_delay = 0
    while finished == False:
        game_state = reset_game_state(game_state)
        
        game_state = fast_delay(game_state, current_delay)

        is_severity = False
        while game_state.packet_depth < max_depth:
            game_state = step(game_state, False)
            print(f"{current_delay} {game_state.packet_depth}")
            if game_state.packet_depth in game_state.depths_caught:
                is_severity = True
                break
    
        
        if is_severity == False:
            finished = True
        else:
            if current_delay % 100 == 0:
                print(f"{current_delay} {game_state.packet_depth}")
            current_delay += 1

    print(f"Delay required for no severity: {current_delay}")

