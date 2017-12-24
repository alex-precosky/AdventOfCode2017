class cpu_c():

    def __init__(self, outqueue=None, inqueue=None):
        self.regfile = dict()
        self.pc = 0
        self.last_frequency_played = 0
        self.last_frequency_recovered = 0
        self.outqueue = outqueue
        self.inqueue = inqueue
        self.num_values_sent = 0
        self.is_stalled = False
        self.num_mul_calls = 0


    def load_operand_value(self, operand):
        # if it's a literal, return the literal
        # if it's a register, return the value from the register
        try:
            operand_value = int(operand)
        except ValueError:
            if operand in self.regfile:
                operand_value = self.regfile[operand]
            else:
                self.regfile[operand] = 0
                operand_value = 0

        return operand_value

    def run_instruction(self, instruction):
        tokens = instruction.split(" ")

        opcode = tokens[0]

        if opcode == "jnz":

            compare_value = self.load_operand_value(tokens[1])
            jump_distance = self.load_operand_value(tokens[2])

            if compare_value != 0:
                self.pc += jump_distance
            else:
                self.pc += 1

        elif opcode == "set":
            dest = tokens[1]
            token_2 = tokens[2]

            src = self.load_operand_value(token_2)

            self.regfile[dest] = src
            self.pc += 1


        elif opcode == "sub":
            dest = tokens[1]
            token_2 = tokens[2]

            src = self.load_operand_value(token_2)

            if dest not in self.regfile:
                self.regfile[dest] = 0
            self.regfile[dest] = self.regfile[dest] - src
            self.pc += 1


        elif opcode == "mul":
            dest = tokens[1]
            token_2 = tokens[2]

            src = self.load_operand_value(token_2)

            if dest not in self.regfile:
                self.regfile[dest] = 0
            self.regfile[dest] = self.regfile[dest] * src
            self.pc += 1

            self.num_mul_calls += 1






if __name__ == "__main__":

    cpu = cpu_c()

    instructions = open("input.txt", "r").readlines()
    instructions = [i.strip() for i in instructions]

    finished = False

    while finished is False:
        instruction = instructions[cpu.pc]
        cpu.run_instruction(instruction)
        if cpu.pc > len(instructions) - 1 or cpu.pc < 0:
            part1_num_mul_calls = cpu.num_mul_calls
            finished = True

            

    part1_num_mul_calls = cpu.num_mul_calls
    print(f"Part 1: {part1_num_mul_calls}")


 

        


