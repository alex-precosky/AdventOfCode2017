from itertools import permutations
from itertools import combinations

def are_duplicates(passphrase):
    tokens = passphrase.strip().split(' ')

    if len(tokens) > len(set(tokens)):
        return True
    else:
        return False

def check_for_anagrams(passphrase):
    tokens = passphrase.strip().split(' ')

    # make all combinations of 2 tokens
    token_pairs = combinations(tokens, 2)

    for token_pair in token_pairs:
        p1 = list(set(permutations(token_pair[0])))  # convert it through a set to remove duplicates
        p2 = list(set(permutations(token_pair[1])))

        all_permutations = p1+p2

        if len(all_permutations) > len(set(all_permutations)):
            return True

    return False


if __name__ == "__main__":
    infile = open("input.txt", "r")
    lines_with_duplicates = [are_duplicates(line) for line in infile.readlines()]
    
    num_valid = 0
    for line in lines_with_duplicates:
        if line==False:
            num_valid += 1
    

    print(f"{num_valid} do not have duplicates")


    infile.close()
    
    infile = open("input.txt", "r")
    lines_with_anagrams = [check_for_anagrams(line) for line in infile.readlines()]

    num_valid = 0
    for line in lines_with_anagrams:
        if line==False:
            num_valid += 1


    print(f"{num_valid} do not have anagrams")
