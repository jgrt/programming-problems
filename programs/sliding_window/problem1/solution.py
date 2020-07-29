"""
https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

Given an unsorted array A of size N of non-negative integers,
find a continuous sub-array which adds to a given number S.

Return the starting and ending positions of first such occuring sub array from the left if sum equals to sub array,
else return -1.

1 <= N <= 10^7
0 <= A[i]<= 10^10

Input: S = 12, arr = 1 2 3 7 5
Output: (1, 3)
"""
from typing import List, Tuple
from sliding_window.utils import InvalidSizeError, InvalidValueError, SolutionNotFound, EmptyArrayError


def validate(arr):
    """Constraints"""
    max_array_length = pow(10, 7)
    max_element_limit = pow(10, 10)
    min_element_limit = 0

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
        raise InvalidValueError(message="Please enter list of all positive integers", min_value=min_element)


def execute(arr, s):
    for i in range(len(arr) + 1):
        for j in range(i + 1, len(arr) + 1):
            if sum(arr[i:j]) == s:
                return i, j
    raise SolutionNotFound('No Solution Found', value=-1)


def find_cont_elements(arr: List[int], s: int) -> Tuple[int, int]:
    validate(arr)
    return execute(arr, s)
