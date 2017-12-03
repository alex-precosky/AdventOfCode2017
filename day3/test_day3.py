from day3 import TravelToSquare

def test_1():
    expected = 0
    actual, x = TravelToSquare(1)
    assert expected == actual

def test_12():
    expected = 3
    actual, x = TravelToSquare(12)
    assert expected == actual

def test_23():
    expected = 2
    actual, x = TravelToSquare(23)
    assert expected == actual

def test_1024():
    expected = 31
    actual, x = TravelToSquare(1024)
    assert expected == actual
