generatorA_start = 634
generatorB_start = 301

generatorA_multiplier = 16807
generatorB_multiplier = 48271

divisor = 2147483647


def generate_value(previous_value, multiplier, divisor):
    return previous_value * multiplier % divisor


def compare_lowest_16_bits(value1, value2):
    value1_masked = value1 & 0xFFFF
    value2_masked = value2 * 0xFFFF
