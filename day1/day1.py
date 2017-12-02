
# The problem works on consecutive string characters, and the last character
# loops around and goes with the first character. So, make a new string
# that is like "abc" -> "abca"
def make_circular_string(in_string):
    return in_string + in_string[0]

# Compare consecutive numbers, add to accumulator if they're the same
def calculate_captcha_part_one(captcha):
    
    circular_captcha = make_circular_string(captcha)
    
    accumulator = 0
    # iterate through the numbers two at a time
    for current, current_plus_one in zip(circular_captcha, circular_captcha[1:]):

        if current == current_plus_one:
            accumulator += int(current)

    return accumulator

# For part two, compare numbers half way across the array instead, wrapping around
def calculate_captcha_part_two(captcha):
    
    captcha_length = len(captcha)

    accumulator = 0

    for i in range(captcha_length):
        index2 = int((i + captcha_length / 2) % captcha_length)
        if captcha[i] == captcha[index2]:
            accumulator += int(captcha[i])

    return accumulator



if __name__ == "__main__":
    infile = open("input.txt", "r")
    
    captcha = infile.readline()
    solution1 = calculate_captcha_part_one(captcha)

    print(f"The part 1 solution is: {solution1}")

    solution2 = calculate_captcha_part_two(captcha)

    print(f"The part 2 solution is: {solution2}")
