def process_instruction_part1( instructions, pc ):
    # returns the new instruction set
    old_pc = pc
    instruction = instructions[pc]
    pc += instruction
    instructions[old_pc] = instructions[old_pc] + 1

    return [instructions, pc]


def process_instruction_part2( instructions, pc ):
    # returns the new instruction set
    old_pc = pc
    instruction = instructions[pc]
    pc += instruction

    if instruction >= 3:
        instructions[old_pc] = instructions[old_pc] - 1
    else:
        instructions[old_pc] = instructions[old_pc] + 1

    return [instructions, pc]


if __name__ == "__main__":
    file_lines = open("input.txt", "r").readlines()
    instructions = [int(line.strip()) for line in file_lines]
    
    pc = 0
    step_counter = 0
    while pc < len(instructions):
        instructions, pc = process_instruction_part1(instructions, pc)
        step_counter += 1
    print(f"Part 1: {step_counter} steps")


    file_lines = open("input.txt", "r").readlines()
    instructions = [int(line.strip()) for line in file_lines]
    pc = 0
    step_counter = 0
    while (pc < len(instructions)) and (pc >= 0):
        instructions, pc = process_instruction_part2(instructions, pc)
        step_counter += 1
    print(f"Part 2: {step_counter} steps")
    # not 360
    # note 3220. too low
