from day11 import cancel_opposite_movements
from day11 import simplify_movements
from day11 import cancel_adjacent_movements

def test_cancel_opposites_1():
    target = ["n", "n", "s"]

    expected = ["n",]
    actual = cancel_opposite_movements(target)

    assert expected == actual


def test_cancel_opposites_2():
    target = ["n", "s"]

    expected = []
    actual = cancel_opposite_movements(target)

    assert expected == actual


def test_cancel_opposites_3():
    target = ["n", "nw"]

    expected = ["n", "nw"]
    actual = cancel_opposite_movements(target)

    assert expected == actual


def test_cancel_adjacent_movements_1():
    target = ["ne", "ne", "ne"]

    expected = ["ne", "ne", "ne"]
    actual = cancel_adjacent_movements(target)

    assert expected == actual
    


def test_part1_1():
    target = ["ne", "ne", "ne"]

    expected = ["ne", "ne", "ne"]
    actual = simplify_movements(target)

    assert expected == actual


def test_part1_2():
    target = ["ne", "ne", "sw", "sw"]

    expected = []
    actual = simplify_movements(target)

    assert expected == actual


def test_part1_3(): 
    target = ["ne", "ne", "s", "s"]

    expected = ["se", "se"] 
    actual = simplify_movements(target)

    assert expected == actual


def test_part1_4(): 
    target = ["se", "sw", "se", "sw", "sw"]

    expected = ["sw", "s", "s"] 
    actual = simplify_movements(target)

    assert expected == actual

