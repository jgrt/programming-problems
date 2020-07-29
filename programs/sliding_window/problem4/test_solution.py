import pytest
from sliding_window.problem4.solution import find_max_sum_list_length
from sliding_window.utils import InvalidValueError, EmptyArrayError


def test_find_max_sum_list_length_on_empty_array():
    with pytest.raises(EmptyArrayError) as exc_info:
        find_max_sum_list_length([], 5)
    assert exc_info.value.ctx.get('array_length', None) == 0


def test_find_max_sum_list_length_on_min_element_error():
    arr = [1, -pow(10, 10)]
    with pytest.raises(InvalidValueError) as exc_info:
        find_max_sum_list_length(arr, 2)
    print(exc_info.value.ctx.get('min_value', None))
    assert exc_info.value.ctx.get('min_value', None) == min(arr)


def test_find_max_sum_list_length_on_max_element_error():
    arr = [1, pow(10, 11)]
    with pytest.raises(InvalidValueError) as exc_info:
        find_max_sum_list_length(arr, 2)
    assert exc_info.value.ctx.get('max_value', None) == max(arr)


def test_find_max_sum_list_length_on_output_list_size():
    arr = [1, 2, 3, 4, 3]
    k = 4
    resp = find_max_sum_list_length(arr, k)
    assert resp <= len(arr)
