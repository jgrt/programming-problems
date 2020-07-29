import pytest
from sliding_window.problem5.solution import find_zero_sum_sub_array
from sliding_window.utils import InvalidValueError, EmptyArrayError


def test_find_zero_sum_sub_array_on_empty_array():
    with pytest.raises(EmptyArrayError) as exc_info:
        find_zero_sum_sub_array([])
    assert exc_info.value.ctx.get('array_length', None) == 0


def test_find_zero_sum_sub_array_on_min_element_error():
    arr = [1, -pow(10, 10)]
    with pytest.raises(InvalidValueError) as exc_info:
        find_zero_sum_sub_array(arr)
    assert exc_info.value.ctx.get('min_value', None) == min(arr)


def test_find_zero_sum_sub_array_on_max_element_error():
    arr = [1, pow(10, 11)]
    with pytest.raises(InvalidValueError) as exc_info:
        find_zero_sum_sub_array(arr)
    assert exc_info.value.ctx.get('max_value', None) == max(arr)


def test_find_zero_sum_sub_array_on_zero_sum():
    arr = [4, 2, -3, 1, 6]
    resp = find_zero_sum_sub_array(arr)
    assert min(arr) <= 0
