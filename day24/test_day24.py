from day24 import parse_line, lines_to_set, find_valid_pieces

def test_parse_line():
    line = "50/41"

    actual = parse_line(line)

    print(actual)

    assert 50 in actual
    assert 41 in actual


def test_lines_to_set():
    lines = ["50/41", "19/43"]

    expected = {(19, 43), (50, 41)}
    actual = lines_to_set(lines)

    assert expected == actual


def test_find_valid_pieces():
    piece_set = {(0,2), (2,2), (2,3), (3,4), (3,5), (0,1), (10,1), (9,10)}

    expected = ((0,1), (0,2))
    actual = find_valid_pieces(piece_set, 0)

    assert expected == actual
