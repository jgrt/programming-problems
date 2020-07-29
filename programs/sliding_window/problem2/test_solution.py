import pytest
from sliding_window.problem2.solution import find_distinct_elements
from sliding_window.utils import InvalidSizeError, InvalidValueError, EmptyArrayError


def test_find_distinct_elements_on_empty_array():
    with pytest.raises(EmptyArrayError) as exc_info:
        find_distinct_elements([], 5)
    assert exc_info.value.ctx.get('array_length', None) == 0


def test_find_distinct_elements_on_min_element_error():
    arr = [1, -2]
    with pytest.raises(InvalidValueError) as exc_info:
        find_distinct_elements(arr, 2)
    assert exc_info.value.ctx.get('min_value', None) == min(arr)


def test_find_distinct_elements_on_max_element_error():
    arr = [1, pow(10, 11)]
    with pytest.raises(InvalidValueError) as exc_info:
        find_distinct_elements(arr, 2)
    assert exc_info.value.ctx.get('max_value', None) == max(arr)


def test_find_distinct_elements_on_valid_window_size():
    arr = [1, 2, 3, 4]
    k = 10
    with pytest.raises(InvalidSizeError) as exc_info:
        find_distinct_elements(arr, k)
    assert exc_info.value.ctx.get('sub_array_length', None) == k


def test_find_distinct_elements_on_output_list_size():
    arr = [1, 2, 3, 4, 3]
    k = 4
    expected_output_size = 2
    resp = find_distinct_elements(arr, k)
    assert len(resp) == expected_output_size


def test_find_distinct_elements_on_distinct_element_size():
    arr = [1, 2, 3, 4, 3]
    k = 4
    expected_output = len(set(arr))
    resp = find_distinct_elements(arr, k)
    assert max(resp) <= expected_output
