import pytest
from sliding_window.problem3.solution import find_max_sum
from sliding_window.utils import InvalidSizeError, EmptyArrayError


def test_find_max_sum_on_empty_array():
    with pytest.raises(EmptyArrayError) as exc_info:
        find_max_sum([], 5)
    assert exc_info.value.ctx.get('array_length', None) == 0


def test_find_max_sum_on_valid_window_size():
    arr = [1, 2, 3, 4]
    k = 10
    with pytest.raises(InvalidSizeError) as exc_info:
        find_max_sum(arr, k)
    assert exc_info.value.ctx.get('sub_array_length', None) == k
