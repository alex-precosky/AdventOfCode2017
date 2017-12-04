from day4 import are_duplicates
from day4 import check_for_anagrams

def test_are_duplicates():
    expected = True
    target = "aa bb aa"
    actual = are_duplicates(target)

    assert expected == actual

def test_are_not_duplicates():
    expected = False
    target = "aa bb"
    actual = are_duplicates(target)

    assert expected == actual

def test_anagrams1():
    expected = False
    target = "abcde fghij"
    actual = check_for_anagrams(target)

    assert expected == actual

def test_anagrams2():
    expected = True
    target = "abcde xyz ecdab"
    actual = check_for_anagrams(target)

    assert expected == actual

def test_anagrams3():
    expected = False
    target = "a ab abc abd abf abj"
    actual = check_for_anagrams(target)

    assert expected == actual

def test_anagrams4():
    expected = False
    target = "iiii oiii ooii oooi oooo"
    actual = check_for_anagrams(target)

    assert expected == actual

def test_anagrams5():
    expected = True
    target = "oiii ioii iioi iiio"
    actual = check_for_anagrams(target)

    assert expected == actual
