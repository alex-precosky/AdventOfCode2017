import queue

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

        if opcode == "snd":
            self.last_frequency_played = self.load_operand_value(tokens[1])
            self.pc += 1

            if self.outqueue is not None:
                self.outqueue.put(self.last_frequency_played)
                self.num_values_sent += 1

        elif opcode == "rcv":
            operand = self.load_operand_value(tokens[1])

            if operand != 0:
                self.last_frequency_recovered = self.last_frequency_played

            if self.inqueue is not None:
                if self.inqueue.empty() is False:
                    queue_value = self.inqueue.get()                    
                    self.regfile[tokens[1]] = queue_value
                    self.is_stalled = False
                    self.pc += 1  # only advance the pc if there was a queue item
                else:
                    self.is_stalled = True

        elif opcode == "jgz":

            compare_value = self.load_operand_value(tokens[1])
            jump_distance = self.load_operand_value(tokens[2])

            if compare_value > 0:
                self.pc += jump_distance
            else:
                self.pc += 1

        elif opcode == "set":
            dest = tokens[1]
            token_2 = tokens[2]

            src = self.load_operand_value(token_2)

            self.regfile[dest] = src
            self.pc += 1

        elif opcode == "add":
            dest = tokens[1]
            token_2 = tokens[2]

            src = self.load_operand_value(token_2)

            if dest not in self.regfile:
                self.regfile[dest] = 0
            self.regfile[dest] = self.regfile[dest] + src
            self.pc += 1

        elif opcode == "mul":
            dest = tokens[1]
            token_2 = tokens[2]

            src = self.load_operand_value(token_2)

            if dest not in self.regfile:
                self.regfile[dest] = 0
            self.regfile[dest] = self.regfile[dest] * src
            self.pc += 1

        elif opcode == "mod":
            dest = tokens[1]
            token_2 = tokens[2]

            src = self.load_operand_value(token_2)

            if dest not in self.regfile:
                self.regfile[dest] = 0
            self.regfile[dest] = self.regfile[dest] % src
            self.pc += 1


if __name__ == "__main__":

    cpu = cpu_c()

    instructions = open("input.txt", "r").readlines()
    instructions = [i.strip() for i in instructions]

    finished = False

    while finished is False:
        instruction = instructions[cpu.pc]
        cpu.run_instruction(instruction)
        if cpu.last_frequency_recovered != 0:
            part1_recovered_frequency = cpu.last_frequency_recovered
            finished = True

    print(f"Part 1: {part1_recovered_frequency}")

    queue_0to1 = queue.Queue()
    queue_1to0 = queue.Queue()

    cpu0 = cpu_c(queue_0to1, queue_1to0)
    cpu1 = cpu_c(queue_1to0, queue_0to1)
    cpu0.regfile["p"] = 0
    cpu1.regfile["p"] = 1


    finished = False
    finished_0 = False
    finished_1 = False
    while finished is False:

        if cpu0.pc < len(instructions):
            instruction0 = instructions[cpu0.pc]
            cpu0.run_instruction(instruction0)
        else:
            finished_0 = True

        if cpu1.pc < len(instructions):
            instruction1 = instructions[cpu1.pc]
            cpu1.run_instruction(instruction1)

        else:
            finished_1 = True

        if (cpu0.is_stalled is True and cpu1.is_stalled is True) or (cpu0.is_stalled is True and finished_1 is True) or (finished_0 is True and cpu1.is_stalled is True):
            part2_values_sent = cpu1.num_values_sent
            finished = True

    print(f"Part 2: {part2_values_sent}")
    # more than 254
