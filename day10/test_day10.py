from day10 import reverse_circular_sublist
from day10 import part_1_hash
from day10 import densify_block

def test_reverse_circular_sublist():
    inputList = [1, 2, 3, 4, 5, 6]
    start = 2
    end = 4

    expected = [1, 2, 5, 4, 3, 6]
    actual = reverse_circular_sublist( inputList, start, end )

    assert expected == actual


def test_reverse_circular_sublist_with_wrap():
    inputList = [1, 2, 3, 4, 5, 6]
    start = 4
    end = 2

    expected = [1, 6, 5, 4, 3, 2]
    actual = reverse_circular_sublist( inputList, start, end )

    assert expected == actual


def test_reverse_circular_sublist_with_wrap_odd():
    inputList = [1, 2, 3, 4, 5]
    start = 4
    end = 2

    expected = [2, 1, 5, 4, 3]
    actual = reverse_circular_sublist( inputList, start, end )

    assert expected == actual


def test_reverse_3():
    inputList = [1, 2, 3, 4, 5]
    start = 3
    end = 4

    expected = [1, 2, 3, 5, 4]
    actual = reverse_circular_sublist( inputList, start, end )

    assert expected == actual


def test_part_1_example():

    lengths = [3, 4, 1, 5]
    notched_string = list(range(5))

    expected = [3, 4, 2, 1, 0]
    actual, pos, skip = part_1_hash(notched_string, lengths, 0, 0)

    assert expected == actual

def test_densify_hash():
    sparse_block = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]

    expected = 64
    actual = densify_block(sparse_block)

    assert expected == actual
