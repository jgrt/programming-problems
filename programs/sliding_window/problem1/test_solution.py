import pytest
from sliding_window.problem1.solution import find_cont_elements
from sliding_window.utils import InvalidValueError, EmptyArrayError


def test_find_cont_elements_on_empty_array():
    with pytest.raises(EmptyArrayError) as exc_info:
        find_cont_elements([], 5)
    assert exc_info.value.ctx.get('array_length', None) == 0


def test_find_cont_elements_on_min_element_error():
    arr = [1, -2]
    with pytest.raises(InvalidValueError) as exc_info:
        find_cont_elements(arr, 2)
    assert exc_info.value.ctx.get('min_value', None) == min(arr)


def test_find_cont_elements_on_max_element_error():
    arr = [1, pow(10, 11)]
    with pytest.raises(InvalidValueError) as exc_info:
        find_cont_elements(arr, 2)
    assert exc_info.value.ctx.get('max_value', None) == max(arr)


def test_find_cont_elements_on_valid_index_output():
    arr = [1, 2, 3, 7, 5]
    s = 12
    resp = find_cont_elements(arr, s)
    if resp:
        assert max(resp) <= len(arr) and min(resp) > -1


def test_find_cont_elements_on_sum():
    arr = [1, 2, 3, 7, 5]
    s = 12
    resp = find_cont_elements(arr, s)
    assert sum(arr[resp[0]:resp[1]]) == s
