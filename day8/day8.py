import re
from enum import Enum

class TestOperator(Enum):
    GE = 1,
    EQ = 2,
    LT = 3,
    GT = 4,
    LE = 5,
    NE = 6

def get_dest_reg(instruction):
    m = re.match("[a-z]+", instruction)

    return m.group(0)

def get_opcode(instruction):
    # return 1 for inc and -1 for dec

    if instruction.find("inc") != -1:
        return 1

    if instruction.find("dec") != -1:
        return -1

    return 0


def get_source_reg(instruction):
    m = re.search("(?<=if )[a-z]+", instruction)

    return m.group(0)


def get_increment(instruction):

    m = re.search("[\-0-9]+(?= if)", instruction)

    return int(m.group(0))


def get_condition_amount(instruction):
    m = re.search("[\-\d]+$", instruction)

    return int(m.group(0))


def get_test_operator(instruction):
    if instruction.find(" == ") != -1:
        return TestOperator.EQ

    if instruction.find(" >= ") != -1:
        return TestOperator.GE

    if instruction.find(" <= ") != -1:
        return TestOperator.LE

    if instruction.find(" < ") != -1:
        return TestOperator.LT

    if instruction.find(" > ") != -1:
        return TestOperator.GT

    if instruction.find(" != ") != -1:
        return TestOperator.NE


def run_instruction(instruction, regfile):
    # produces the new regfile

    opcode = get_opcode(instruction)
    source_reg = get_source_reg(instruction)
    dest_reg = get_dest_reg(instruction)
    increment_amount = get_increment(instruction)
    condition_amount = get_condition_amount(instruction)
    test_operator = get_test_operator(instruction)

    if source_reg not in regfile:
        regfile[source_reg] = 0

    if dest_reg not in regfile:
        regfile[dest_reg] = 0

    condition_passes = False

    if test_operator == TestOperator.EQ:
        if regfile[source_reg] == condition_amount:
            condition_passes = True
    elif test_operator == TestOperator.GE:
        if regfile[source_reg] >= condition_amount:
            condition_passes = True
    elif test_operator == TestOperator.LE:
        if regfile[source_reg] <= condition_amount:
            condition_passes = True
    elif test_operator == TestOperator.LT:
        if regfile[source_reg] < condition_amount:
            condition_passes = True
    elif test_operator == TestOperator.GT:
        if regfile[source_reg] > condition_amount:
            condition_passes = True
    elif test_operator == TestOperator.NE:
        if regfile[source_reg] != condition_amount:
            condition_passes = True

    if condition_passes == True:
        #print(instruction)
        regfile[dest_reg] += (increment_amount * opcode)
        #print(regfile)


    return regfile

if __name__ == "__main__":

    regfile = dict()

    instructions = open("input.txt", "r").readlines()
    instructions = [instruction.strip() for instruction in instructions]

    all_max_register_values = list()

    for instruction in instructions:
        regfile = run_instruction(instruction, regfile)
        all_max_register_values.append(max(regfile.values()))

    max_register_value = max(regfile.values())
    print(f"Max register value is: {max_register_value}")

    all_time_max = max(all_max_register_values)
    print(f"All time max register value is: {all_time_max}")
