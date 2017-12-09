from day9 import process_stream


def test_1():
    stream = "{}"

    state = process_stream(stream)

    expected = 1
    actual = state.score

    assert expected == actual


def test_2():
    stream = "{{{}}}"

    state = process_stream(stream)

    expected = 6
    actual = state.score

    assert expected == actual


def test_3():
    stream = "{{},{}}"

    state = process_stream(stream)

    expected = 5
    actual = state.score

    assert expected == actual


def test_4():
    stream = "{{{},{},{{}}}}"

    state = process_stream(stream)

    expected = 16
    actual = state.score

    assert expected == actual


def test_4():
    stream = "{{{},{},{{}}}}"

    state = process_stream(stream)

    expected = 16
    actual = state.score

    assert expected == actual


def test_5():
    stream = "{<a>,<a>,<a>,<a>}"

    state = process_stream(stream)

    expected = 1
    actual = state.score

    assert expected == actual


def test_6():
    stream = "{{<ab>},{<ab>},{<ab>},{<ab>}}"

    state = process_stream(stream)

    expected = 9
    actual = state.score

    assert expected == actual


def test_6():
    stream = "{{<ab>},{<ab>},{<ab>},{<ab>}}"

    state = process_stream(stream)

    expected = 9
    actual = state.score

    assert expected == actual


def test_7():
    stream = "{{<!!>},{<!!>},{<!!>},{<!!>}}"

    state = process_stream(stream)

    expected = 9
    actual = state.score

    assert expected == actual


def test_7():
    stream = "{{<!!>},{<!!>},{<!!>},{<!!>}}"

    state = process_stream(stream)

    expected = 9
    actual = state.score

    assert expected == actual


def test_8():
    stream = "{{<a!>},{<a!>},{<a!>},{<ab>}}"

    state = process_stream(stream)

    expected = 3
    actual = state.score

    assert expected == actual


def test_garbage_1():
    stream = "<>"

    state = process_stream(stream)

    expected = 0
    actual = state.garbage_count

    assert expected == actual


def test_garbage_2():
    stream = "<random characters>"

    state = process_stream(stream)

    expected = 17
    actual = state.garbage_count
    print(actual)

    assert expected == actual


def test_garbage_3():
    stream = "<<<<>"

    state = process_stream(stream)

    expected = 3
    actual = state.garbage_count
    print(actual)

    assert expected == actual


def test_garbage_4():
    stream = "<{!>}>"

    state = process_stream(stream)

    expected = 2
    actual = state.garbage_count
    print(actual)

    assert expected == actual


def test_garbage_5():
    stream = "<!!>"

    state = process_stream(stream)

    expected = 0
    actual = state.garbage_count
    print(actual)

    assert expected == actual



