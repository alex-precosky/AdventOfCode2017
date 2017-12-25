import numpy as np
from day21 import subdivide, join_subdivisions

def test_subdivide_even():
    ary = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
    subdivs = subdivide(ary)
    
    expected_subdivs = np.array([[1,2],[5,6]])

    assert np.array_equal(expected_subdivs, subdivs[0][0]) == True


def test_subdivide_odd():
    ary = np.array([[1,2,3], [4,5,6], [7,8,9]])
    subdivs = subdivide(ary)

    assert np.array_equal(subdivs[0][0], ary) == True


def test_join_subdivisions():
    a1 = np.array([[1, 2], [5, 6]])
    a2 = np.array([[3, 4,], [7, 8]])
    a3 = np.array([[9, 10], [13, 14]])
    a4 = np.array([[11, 12], [15, 16]])

    ary = [ [a1, a2], [a3, a4] ]

    expected = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

    actual = join_subdivisions(ary)

    assert np.array_equal(expected, actual) == True

