import numpy as np


def subdivide(ary):
    # returns a 2d list of numpy arrays

    if ary.shape[0] % 2 == 0:
        step = 2
    else:
        step = 3


    dim = ary.shape[0]

    return_list = []

    for i in range(0, dim, step):
        row = []
        for j in range(0, dim, step):
            sub_ary = ary[i:i+step, j:j+step]
            row.append(sub_ary)
        return_list.append(row)

    return return_list


def compare_patterns( pat1, pat2 ):
    # compare the two patterns, as numpy arrays, rotating and flipping pat2 all around

    if np.array_equal( pat1, pat2 ):
        return True


    
    return False


def parse_pattern(pattern_line):
    # return [pattern before, pattern after], both numpy arrays
    split_list = pattern_line.split(" => ")
    before_string = split_list[0]
    after_string = split_list[1]

    dim_before = len(before_string.split("/")[0])
    dim_after = dim_before + 1

    before_pattern = np.zeros([dim_before, dim_before], dtype=np.int)
    after_pattern = np.zeros([dim_after, dim_after], dtype=np.int)

    before_strings = before_string.split("/")
    for i in range(dim_before):
        for j in range(dim_before):
            if before_strings[i][j] == "#":
                before_pattern[i][j] = 1
            else:
                before_pattern[i][j] = 0


    after_strings = after_string.split("/")
    for i in range(dim_after):
        for j in range(dim_after):
            if after_strings[i][j] == "#":
                after_pattern[i][j] = 1
            else:
                after_pattern[i][j] = 0

    return [before_pattern, after_pattern]


def join_subdivisions(subdivisions_before):
    # returns a 2d numpy array by joining the 2d list of 2d numpy arrays

    dim_subdivision = len(subdivisions_before)
    step = subdivisions_before[0][0].shape[0]
    dim_overall = dim_subdivision*step

    ary_joined = np.zeros([dim_overall, dim_overall], dtype=np.int)

    for i in range(0, dim_overall, step):
        for j in range(0, dim_overall, step):                        
            ary_joined[i:i+step, j:j+step] = subdivisions_before[i//step][j//step]

    return ary_joined

def add_pattern_transformations(patterns):
    return_patterns = []
    
    for pattern in patterns:
        
        before_pattern = pattern[0]
        return_patterns.append( [before_pattern, pattern[1]] ) 
        return_patterns.append( [np.rot90(before_pattern), pattern[1]] ) 
        return_patterns.append( [np.rot90(np.rot90(before_pattern)), pattern[1]] ) 
        return_patterns.append( [np.rot90(np.rot90(np.rot90(before_pattern))), pattern[1]] ) 

        return_patterns.append( [np.flip(before_pattern, 0), pattern[1]] ) 
        return_patterns.append( [np.flip(np.rot90(before_pattern), 0), pattern[1]] ) 
        return_patterns.append( [np.flip(np.rot90(np.rot90(before_pattern)),0 ), pattern[1]] ) 
        return_patterns.append( [np.flip(np.rot90(np.rot90(np.rot90(before_pattern))), 0), pattern[1]] ) 

    return return_patterns

def load_patterns(lines):
    patterns = []
    
    for line in lines:
        patterns.append( parse_pattern( line ) )

    patterns = add_pattern_transformations(patterns)
    return patterns


def find_result_pattern(subdivision, patterns):
    for pattern in patterns:

        before_pattern = pattern[0]

        if compare_patterns(before_pattern, subdivision) == True:
            result_pattern = pattern[1] # 1 is the after_pattern

    return result_pattern


def find_result_pattern_in_dict(subdivision, pattern_dict):
    
    before_pattern = np.array_str(subdivision)
    result_pattern = pattern_dict[ before_pattern ]
    
    return result_pattern


def patterns_to_dict(patterns):
    return_dict = dict()

    for pattern in patterns:

        before_pattern = pattern[0]
        after_pattern = pattern[1]

        key = np.array_str(before_pattern)

        return_dict[key] = after_pattern

    return return_dict
        

def do_iteration(grid, patterns, pattern_dict):
    subdivisions_before = subdivide(grid)

    subdivisions_after = []

    for subdivision_before_row in subdivisions_before:
        subdivisions_after_row = []
        for subdivision in subdivision_before_row:
            result_pattern = find_result_pattern_in_dict(subdivision, pattern_dict)
            subdivisions_after_row.append(result_pattern)
        subdivisions_after.append(subdivisions_after_row)

    grid = join_subdivisions(subdivisions_after)

    return grid

def count_on(grid):
    # count the number of pixels that are on
    return grid.sum()

if __name__ == "__main__":

    seed = np.array([[0,1,0],[0,0,1],[1,1,1]], dtype=np.int)

    input_lines = open("input.txt", "r").readlines()

    patterns = load_patterns(input_lines)

    pattern_dict = patterns_to_dict(patterns)

    num_iterations = 18

    grid = seed

    for it in range(num_iterations):
        grid = do_iteration(grid, patterns, pattern_dict)
        print(grid)
        num_on = count_on(grid)
        print(f"Number of on pixels: {num_on}  Iteration: {it}")
