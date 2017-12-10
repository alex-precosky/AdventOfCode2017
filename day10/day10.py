from functools import reduce
import binascii

def reverse_circular_sublist(array, start, end):
    if end >= start:
        wraps=False
    else:
        wraps = True

    if wraps == False:
        subarray = array[start:end+1]
    else:
        subarray = array[start:] + array[:end+1]

    subarray.reverse()

    ptr = start
    i = 0
    while i < len(subarray):
        array[ptr] = subarray[i]
        i += 1
        ptr = (ptr+1) % len(array)

    return array

def part_1_hash(notched_string, lengths, pos_0, skip_0):

    pos = pos_0
    skip = skip_0

    for length in lengths:

        start = pos
        end = (start+length-1) % len(notched_string)

        if length != 0:
            notched_string = reverse_circular_sublist(notched_string,
                                                      start,
                                                      end)

        pos = (pos + length + skip) % len(notched_string)
        skip = skip+1
        
    return (notched_string, pos, skip)
    

def densify_block( sparse_block ):
    return reduce( (lambda x,y: x ^ y), sparse_block)
    

if __name__ == "__main__":
    inFile = open("input.txt", "r")
    lengths = inFile.readline().strip().split(",")

    notched_string = list(range(256))

    lengths = [int(length) for length in lengths]

    notched_string, pos, skip = part_1_hash(notched_string, lengths, 0, 0)

    part1 = notched_string[0] * notched_string[1]

    print(f"Part 1: {part1}")


    notched_string = list(range(256))
    inFile = open("input.txt", "r")
    chars = inFile.readline().strip()
    
    # Input for part two is the string lengths as the ascii values of the 
    # input file characters, plus a few specified extras thrown on
    ascii_lengths = [ord(char) for char in chars]
    ascii_lengths += [17, 31, 73, 47, 23]

    # Then run 64 rounds of the knot hash
    pos = 0
    skip = 0
    for i in range(64):
        notched_string, pos, skip = part_1_hash( notched_string,
                                                 ascii_lengths,
                                                 pos, 
                                                 skip )
        
    # Then densify 16 sets of 16 number long lists
    sparce_blocks = [notched_string[i:i+16] for i in range(0, 256, 16)]
    sparce_hashes = [densify_block(sparce_block) for sparce_block in sparce_blocks]

    # Finally, report the hash in hexadecimal
    part2 = binascii.hexlify(bytes(bytearray(sparce_hashes)))
    print( f"Part 2: {part2}" )

