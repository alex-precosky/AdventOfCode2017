def generate_value(previous_value, multiplier, divisor):
    return previous_value * multiplier % divisor
    
def compare_lowest_16_bits(value1, value2):
    value1_masked = value1 & 0x0000FFFF
    value2_masked = value2 & 0x0000FFFF

    if value1_masked == value2_masked:
        return True
    else:
        return False


if __name__ == "__main__":
    generatorA_start = 634
    generatorB_start = 301

    generatorA_multiplier = 16807
    generatorB_multiplier = 48271

    divisor = 2147483647

    equality_count1 = 0
    valueA = generatorA_start
    valueB = generatorB_start

    # for i in range(40000000):
    #     if i % 1000 == 0:
    #         print(f"Iteration {i}")

    #     valueA = generate_value(valueA, generatorA_multiplier, divisor)
    #     valueB = generate_value(valueB, generatorB_multiplier, divisor)

    #     if compare_lowest_16_bits(valueA, valueB) == True:
    #         equality_count1 += 1


#    print(f"Equality count: {equality_count1}")


    equality_count2 = 0
    valueA = generatorA_start
    valueB = generatorB_start

    for i in range(5000000):
        if i % 1000 == 0:
            print(f"Iteration {i}")

        valueA = generate_value(valueA, generatorA_multiplier, divisor)
        while valueA % 4 != 0:
            valueA = generate_value(valueA, generatorA_multiplier, divisor)

        valueB = generate_value(valueB, generatorB_multiplier, divisor)
        while valueB % 8 != 0:
            valueB = generate_value(valueB, generatorB_multiplier, divisor)

        if compare_lowest_16_bits(valueA, valueB) == True:
            equality_count2 += 1


    print(f"Equality count: {equality_count2}")
