from day5 import process_instruction_part1

def test_1():
    instructions = [0, 3, 0, 1, -3]
    expected_instructions = [1, 3, 0, 1, -3]
    expected_pc = 0

    actual, pc = process_instruction_part1(instructions, 0)

    assert expected_instructions == actual
    assert expected_pc == pc

def test_2():
    instructions = [1, 3, 0, 1, -3]
    expected_instructions = [2, 3, 0, 1, -3]
    expected_pc = 1

    actual, pc = process_instruction_part1(instructions, 0)

    assert expected_instructions == actual
    assert expected_pc == pc


def test_3():
    instructions = [2, 3, 0, 1, -3]
    expected_instructions = [2, 4, 0, 1, -3]
    expected_pc = 4

    actual, pc = process_instruction_part1(instructions, 1)

    assert expected_instructions == actual
    assert expected_pc == pc

