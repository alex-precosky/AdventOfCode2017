from functools import reduce
import numpy as np

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


def knot_hash_round(input_string, lengths, pos_0, skip_0):

    pos = pos_0
    skip = skip_0

    for length in lengths:

        start = pos
        end = (start+length-1) % len(input_string)

        if length != 0:
            input_string = reverse_circular_sublist(input_string,
                                                      start,
                                                      end)

        pos = (pos + length + skip) % len(input_string)
        skip = skip+1
        
    return (input_string, pos, skip)


def densify_block( sparse_block ):
    return reduce( (lambda x,y: x ^ y), sparse_block)


def knot_hash(input_string):
    notched_string = list(range(256))


    ascii_lengths = [ord(char) for char in input_string]
    ascii_lengths += [17, 31, 73, 47, 23]

    # Then run 64 rounds of the knot hash
    pos = 0
    skip = 0
    for i in range(64):
        notched_string, pos, skip = knot_hash_round( notched_string,
                                                 ascii_lengths,
                                                 pos, 
                                                 skip )

    # Then densify 16 sets of 16 number long lists
    sparce_blocks = [notched_string[i:i+16] for i in range(0, 256, 16)]
    sparce_hashes = [densify_block(sparce_block) for sparce_block in sparce_blocks]

    return bytearray(sparce_hashes)

def count_bits(byte_array):    
    count = 0
    for byte in byte_array:
        count += bin(byte).count("1")
    return count


def bytearray_to_binary_list(byte_array):
    return_list = list()
    
    for byte in byte_array:
        byte_for_shifting = byte

        for i in range(8):
            bit = (byte_for_shifting & 0x80) != 0
            byte_for_shifting = byte_for_shifting << 1
            if bit == True:
                bit = 1
            else:
                bit = 0
            return_list.append(bit)

    return return_list


# given a starting point, grow around that to mark regions
def region_growing(hash_array, region_map, i, j, label):
    region_map[i, j] = label
    
    # check above
    if i > 0:
        if region_map[i-1][j] == 0 and hash_array[i-1][j] == 1:
            region_map = region_growing(hash_array, region_map, i-1, j, label)

    # check below
    if i < 127:
        if region_map[i+1][j] == 0 and hash_array[i+1][j] == 1:
            region_map = region_growing(hash_array, region_map, i+1, j, label)

    # check left
    if j > 0:
        if region_map[i][j-1] == 0 and hash_array[i][j-1] == 1:
            region_map = region_growing(hash_array, region_map, i, j-1, label)

    # check right
    if j < 127:
        if region_map[i][j+1] == 0 and hash_array[i][j+1] == 1:
            region_map = region_growing(hash_array, region_map, i, j+1, label)

    return region_map




if __name__ == "__main__":

    hash_array = list()

    squares_used = 0
    for i in range(128):
        input_key = f"jxqlasbh-{i}"
        hash = knot_hash(input_key)

        hash_array.append( bytearray_to_binary_list( hash ))

        squares_used += count_bits(hash)

    print(f"Part 1: {squares_used}")


    hash_np_array = np.array(hash_array)

    # keep track of which elements have been visited and which region they belong to
    region_map = np.zeros([128,128])

    # visit elements in the hash array, finding regions
    region_counter = 0
    for i in range(128):
        for j in range(128):
            # if not visited yet, spawn a new region
            if hash_np_array[i][j] == 1 and region_map[i][j] == 0:
                region_counter += 1
                region_map = region_growing(hash_np_array, region_map, i, j, region_counter)

    print(f"There were {region_counter} regions found")

    
