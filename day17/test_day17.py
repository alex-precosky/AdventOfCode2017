from day17 import node_list_c

def test_one_insert():
    node_list = node_list_c()

    step = 3
    node_list.do_insert(step)
    
    expected = [0, 1]
    actual = node_list.get_value_sequence()
    print(actual)

    assert expected == actual


def test_two_inserts():
    node_list = node_list_c()

    step = 3

    for i in range(2):
        node_list.do_insert(step)
    
    expected = [0, 2, 1]
    actual = node_list.get_value_sequence()
    print(actual)

    assert expected == actual


def test_nine_inserts():
    node_list = node_list_c()

    step = 3

    for i in range(9):
        node_list.do_insert(step)
    
    expected = [0, 9, 5, 7, 2, 4, 3, 8, 6, 1]
    actual = node_list.get_value_sequence()
    print(actual)

    assert expected == actual
