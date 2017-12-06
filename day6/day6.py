#balance blocks between memory banks
#looks for memory bank with most blocks
#ties won by lowest-numbered memory bank
#these blocks are redistributred amon the banks. all blocks removed from the bank, then mmoves
#to the next highest-indexed bank and inserts one of the blocks. continues until ti runs out of blocks.
#wraps to first

#how many resitributions are done before a blocks-in-banks config that is produced that has been seen before

def find_source_bank(blocks):
    max_blocks_indices = [i for i,x in enumerate(blocks) if x==max(blocks)]
    return min(max_blocks_indices)

def check_if_combo_seen(combos_so_far, combo):
    if combo in combos_so_far:
        return True
    else:
        return False

def do_redistribution(blocks):
    source_bank = find_source_bank(blocks)
    num_banks = len(blocks)

    blocks_to_distribute = blocks[source_bank]
    blocks[source_bank] = 0
    i = (source_bank+1) % num_banks
    while blocks_to_distribute > 0:
        blocks[i] += 1
        blocks_to_distribute -= 1
        i = (i+1) % num_banks

    return blocks


def do_part_1(blocks):
    combos_so_far = list()
    combos_so_far.append(blocks.copy())

    done = False
    num_redistributions = 0
    while not done:

        blocks = do_redistribution(blocks)
        num_redistributions += 1

        if check_if_combo_seen(combos_so_far, blocks) == True:
            done = True
        else:
            combos_so_far.append(blocks.copy())
    
    
    num_cycles_until_repeat = num_redistributions- combos_so_far.index(blocks)
    print(f"Part 2: {num_cycles_until_repeat}")

    return num_redistributions


if __name__ == "__main__":
    blocks = open("input.txt").readline().strip().split()
    blocks = [int(x) for x in blocks]

    num_redistributions = do_part_1(blocks)


    # not 61
    print(f"Part 1: {num_redistributions}")

