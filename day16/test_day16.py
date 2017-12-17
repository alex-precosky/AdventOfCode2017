from day16 import spin, swap, execute_moves


def test_spin():
    programs = "abcde"

    expected = "eabcd"

    actual = spin(programs, 1)

    assert expected == actual


def test_swap():
    programs = "eabcd"

    expected = "eabdc"

    actual = swap(programs, 3, 4)

    assert expected == actual



def test_part1_example_moves():
    programs = "abcde"
    moves = ["s1", "x3/4", "pe/b"]



    expected = "baedc"
    
    actual = execute_moves(moves, programs)

    print(actual)
    assert expected == actual
