import re



class program_record:
    child_program_names = list()
    weight = 0
    name = ""


def parse_input_line(line):

    # returns a program_record
    line_program_record = program_record()

    m = re.search('[a-z]+', line)
    line_program_record.name = m.group(0)
    
    m = re.search('(?<=\()\d+', line)
    line_program_record.weight = int(m.group(0))

    line_child_part = line.split(">")

    if len(line_child_part) == 2:
        line_program_record.child_program_names = [name.strip() for name in line_child_part[1].split(",")]
        

    return line_program_record


def get_stack_weight(root_program_record, program_dict):
    sum = 0
    for child_name in root_program_record.child_program_names:
        sum += get_stack_weight(program_dict[child_name], program_dict)

    sum += root_program_record.weight
    return sum

def get_uneven_stack(root_program_record, program_dict):
    # find the even stack by looking for the one heavier than average
    # returns the program record
    average_weight = 0

    for child_name in root_program_record.child_program_names:
        child_record = program_dict[child_name]
        weight = get_stack_weight(child_record, program_dict)
        print(f"{child_name} -> {weight}")
        average_weight += weight

    average_weight /= len(root_program_record.child_program_names)
    for child_name in root_program_record.child_program_names:
        child_record = program_dict[child_name]
        weight = get_stack_weight(child_record, program_dict)
        if weight > average_weight:
            return child_record

if __name__ == "__main__":

    program_dict = dict()

    lines = [line.strip() for line in open("input.txt").readlines()]

    # parse each tree node and put in a dictionary with the program name as the key
    for line in lines:
        line_record = parse_input_line(line)
        program_dict[ line_record.name ] = line_record

    # for part 1, look for elements with no parent
    root_program_name = ""
    for name in program_dict.keys():
        no_parent = False
        for record in program_dict.values():
            if name in record.child_program_names:
                no_parent = True

        if no_parent == False:
            print(f"Program {name} is at the bottom of the stack")
            root_program_name = name

    # get the weight of the root program's children:
    root_program = program_dict[root_program_name]
    for name in program_dict["bntzksk"].child_program_names:
        print(name)

    uneven_stack = root_program
    while uneven_stack is not None:
        print(f"{uneven_stack.name} is unbalanced. Root's weight: {uneven_stack.weight}")
        uneven_stack = get_uneven_stack(uneven_stack, program_dict)

    # to get part 2 answer, look at the weight of the first level unbalanced stack and 
    # the weight of the root of the last parent node before the leaves. Take weight off of
    # that element so that the first level unbalanced stack will have the same weight as its
    # siblings


