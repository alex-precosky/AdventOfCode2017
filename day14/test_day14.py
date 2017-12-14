from day14 import bytearray_to_binary_list

def test_bytearray_to_binary_list():
    input = bytearray([0x14])

    expected = [0, 0, 0, 1, 0, 1, 0, 0]
    
    actual = bytearray_to_binary_list(input)

    assert expected == actual


