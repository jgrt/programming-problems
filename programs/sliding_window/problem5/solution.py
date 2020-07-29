"""
https://practice.geeksforgeeks.org/problems/subarray-with-0-sum/0

Given an array a[] of N positive and negative numbers.
Find if there is a sub-array (of size at-least one) with 0 sum.

Return 1 if there exist a sub-array of size at least 1 with sum equal to 0 else return 0

Constraints:
1 <= N <= 10^4
-10^5 <= a[i] <= 10^5

Input: arr = [4, 2, -3, 1, 6]
Output: 1
"""

from typing import List, Tuple, Union
from sliding_window.utils import InvalidSizeError, InvalidValueError, SolutionNotFound, EmptyArrayError


def validate(arr):
    """Constraints"""
    max_array_length = pow(10, 4)
    max_element_limit = pow(10, 5)
    min_element_limit = -pow(10, 5)

    if not arr:
        raise EmptyArrayError(message='Empty list found', array_length=0)

    array_length = len(arr)
    max_element = max(arr)
    min_element = min(arr)

    if not (array_length <= max_array_length):
        raise InvalidSizeError(message='Please enter valid length of list', array_length=array_length)
    if not (max_element <= max_element_limit):
        raise InvalidValueError(message='Please enter list elements within specified range', max_value=max_element)
    if not (min_element >= min_element_limit):
        raise InvalidValueError(message='Please enter list elements within specified range', min_value=min_element)


def execute(arr):
    for i in range(len(arr) + 1):
        for j in range(i + 1, len(arr) + 1):
            if sum(arr[i:j]) == 0:
                return 1
    raise SolutionNotFound('No Solution Found', value=0)


def find_zero_sum_sub_array(arr: List[int]) -> int:
    validate(arr)
    return execute(arr)
