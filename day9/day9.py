from copy import copy

class stream_state_c():
    nest_level = 0
    score = 0
    escaping = False
    in_garbage = False
    garbage_count = 0

def process_char(ch, stream_state):
    # returns the new stream state

    prev_stream_state = copy(stream_state)

    if stream_state.escaping == True:
        stream_state.escaping = False
        return stream_state
    elif ch == "!":
        stream_state.escaping = True
        return stream_state
    elif ch == "<":
        stream_state.in_garbage = True
    elif ch == ">":
        stream_state.in_garbage = False
    elif ch == "{" and stream_state.in_garbage == False:
        stream_state.nest_level += 1
    elif ch == "}" and stream_state.in_garbage == False:
        stream_state.score += stream_state.nest_level
        stream_state.nest_level -= 1

    if stream_state.in_garbage == True and stream_state.escaping == False and ch != ">" and prev_stream_state.in_garbage == True:
        stream_state.garbage_count += 1

    return stream_state


def process_stream(stream):
    # returns the final stream state

    stream_state = stream_state_c()

    for ch in stream:
        stream_state = process_char(ch, stream_state)

    return stream_state


if __name__ == "__main__":
    inputline = open("input.txt", "r").readline().strip()

    state = process_stream(inputline)
    score = state.score
    garbage_count = state.garbage_count

    print(f"Part 1 score: {score}")
    print(f"Part 2 garbage count: {garbage_count}")
    # less than 10538
