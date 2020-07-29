import pytest
from mathematics.problem1.solution import create_pattern


def test_create_pattern_on_output_size():
    val = 4
    resp = create_pattern(val)
    assert len(resp) == val


def test_create_pattern_on_order_of_list_element():
    resp = create_pattern(3)
    assert list(resp[-1]) == sorted(list(resp[-1]), reverse=True)


def test_create_pattern_on_size_elements():
    val = 3
    resp = create_pattern(val)
    elements_len = list(map(len, resp))
    assert elements_len == [val*i for i in range(val, 0, -1)]
