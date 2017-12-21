from day18 import cpu_c
import queue


def test_ex1():
    instruction = "set a 1"

    cpu = cpu_c()

    cpu.run_instruction(instruction)

    expected = 1
    actual = cpu.regfile["a"]

    assert expected == actual


def test_ex2():

    cpu = cpu_c()

    cpu.run_instruction("set a 1")
    cpu.run_instruction("add a 2")

    expected = 3
    actual = cpu.regfile["a"]

    assert expected == actual


def test_ex3():

    cpu = cpu_c()

    cpu.run_instruction("set a 1")
    cpu.run_instruction("add a 2")
    cpu.run_instruction("mul a a")

    expected = 9
    actual = cpu.regfile["a"]

    assert expected == actual


def test_ex4():

    cpu = cpu_c()

    cpu.run_instruction("set a 1")
    cpu.run_instruction("add a 2")
    cpu.run_instruction("mul a a")
    cpu.run_instruction("mod a 5")

    expected = 4
    actual = cpu.regfile["a"]

    assert expected == actual


def test_part2():

    queue_0to1 = queue.Queue()
    queue_1to0 = queue.Queue()

    cpu0 = cpu_c(queue_0to1, queue_1to0)
    cpu1 = cpu_c(queue_1to0, queue_0to1)
    cpu0.regfile["p"] = 0
    cpu1.regfile["p"] = 1

    instructions = ["snd 1", "snd 2", "snd p", "rcv a", "rcv b", "rcv c", "rcv d"]

    finished = False
    finished_0 = False
    finished_1 = False

    it = 0
    while finished is False and it < 10:

        it += 1

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

        print(f"i0: {instruction0}   i1: {instruction1}    q_0to1: {queue_0to1.qsize()} q_1to0: {queue_1to0.qsize()}")   

    assert part2_values_sent == 4
