from day19 import maze_state_c


def test_find_maze_start():
    maze_lines = open("sample_input.txt", "r").readlines()

    maze_state = maze_state_c(maze_lines)

    maze_start = maze_state.position_x

    expected = 5
    actual = maze_start

    assert expected == actual

def test_sample_maze():

    maze_lines = open("sample_input.txt", "r").readlines()
    maze_state = maze_state_c(maze_lines)

    finished = False
    while finished is not True:
        finished = maze_state.step_maze()

    expected = "ABCDEF"
    actual = ''.join(maze_state.letters_visited)

    print(actual)
    assert expected == actual
