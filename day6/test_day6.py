from day6 import find_source_bank, check_if_combo_seen, do_redistribution, do_part_1

def test_find_source_bank():
    target = [1,5,5,2]
    expected = 2
    actual = find_source_bank(target)

    print(actual)
    assert expected == actual

def test_check_if_combo_seen():
    combos = [[1,2,3,4],]
    combo = [1,2,3,4]
    expected = True
    
    actual = check_if_combo_seen(combos, combo)
    assert expected == actual

def test_check_if_combo_not_seen():
    combos = [[1,2,3,4],]
    combo = [1,2,3,5]
    expected = False
    
    actual = check_if_combo_seen(combos, combo)
    assert expected == actual


def test_do_redistribution():
    blocks = [0, 2, 7, 0]
    expected = [2, 4, 1, 2]

    actual = do_redistribution(blocks)
    print(actual)

    assert expected == actual

def test_do_part_1():
    blocks = [0, 2, 7, 0]
    expected = 5
    actual = do_part_1(blocks)

    assert expected == actual
