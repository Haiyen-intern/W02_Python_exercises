import pytest

from lists_p01 import custom_len, pivot_list
from tuples_p01 import l1_distance


def test_custom_len():
    assert custom_len([1, 2, 3]) == 3
    assert custom_len([]) == 0


def test_pivot_list():
    assert pivot_list(3, [6, 4, 1, 7]) == [1, 3, 6, 4, 7]


def test_l1_distance():
    assert l1_distance((1, 2), (4, 6)) == 7