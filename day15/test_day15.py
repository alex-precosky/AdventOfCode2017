from day15 import generate_value

generatorA_multiplier = 16807
divisor = 2147483647
seedA = 65
seedB = 8921

def test_generate_value_a1():
    expected = 1092455
    actual = generate_value(seedA, generatorA_multiplier, divisor)

    assert expected == actual

def test_generate_value_a2():
    expected = 1181022009
    
    num1 = generate_value(seedA, generatorA_multiplier, divisor)
    actual = generate_value(num1, generatorA_multiplier, divisor)

    assert expected == actual
