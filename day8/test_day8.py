from day8 import get_dest_reg
from day8 import get_increment
from day8 import get_opcode
from day8 import get_source_reg
from day8 import get_condition_amount

def test_get_dest_reg():
    target = "ewg dec 269 if u == 610"
    expected = "ewg"
    actual = get_dest_reg(target)

    assert expected == actual


def test_get_source_reg():
    target = "ewg dec 269 if u == 610"
    expected = "u"
    actual = get_source_reg(target)

    assert expected == actual


def test_get_increment():
    target = "ewg dec 269 if u == 610"
    expected = 269
    actual = get_increment(target)

    assert expected == actual

def test_get_negative_increment():
    target = "ewg dec -269 if u == 610"
    expected = -269
    actual = get_increment(target)

    assert expected == actual


def test_get_opcode_inc():
    target = "ewg inc -269 if u == 610"
    expected = 1
    actual = get_opcode(target)

    assert expected == actual


def test_get_opcode_dec():
    target = "ewg dec -269 if u == 610"
    expected = -1
    actual = get_opcode(target)

    assert expected == actual


def test_get_condition_amount():
    target = "ewg dec 269 if u == 610"
    expected = 610
    actual = get_condition_amount(target)

    assert expected == actual


def test_get_negative_condition_amount():
    target = "ewg dec 269 if u == -610"
    expected = -610
    actual = get_condition_amount(target)

    assert expected == actual
