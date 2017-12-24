from day22 import read_input, infection_state_c
import numpy as np

def test_read_input():
    input_lines = ["..#", "#..", "..."]

    expected = np.array([[0, 0, 1], [1, 0, 0], [0, 0, 0]], dtype=int)
    actual = read_input(input_lines)

    assert np.array_equal(expected, actual) == True


def test_init_virus_state():
    input_lines = ["..#", "#..", "..."]

    n = 9

    infection_state = infection_state_c(n, read_input(input_lines))

    print(infection_state.current_x)

    assert 5 == infection_state.current_x
    assert 5 == infection_state.current_y


def test_sample_infection():

    input_lines = ["..#", "#..", "..."]

    n = 20

    infection_state = infection_state_c(n, read_input(input_lines))


    for i in range(70):
        infection_state.burst()
    
    expected = 41
    actual = infection_state.num_bursts_caused_infections

    assert expected == actual



def test_sample_infection_part2():

    input_lines = ["..#", "#..", "..."]

    n = 20

    infection_state = infection_state_c(n, read_input(input_lines))


    for i in range(100):
        infection_state.burst_part_2()
    
    expected = 26
    actual = infection_state.num_bursts_caused_infections

    assert expected == actual
