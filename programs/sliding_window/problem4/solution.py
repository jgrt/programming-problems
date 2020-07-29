"""
https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k/0

Given an array containing N integers and an integer S.
Your task is to find the length of the longest Sub-Array with sum of the elements equal to the given value S.

Return the required length of longest sub array. If no such sub-array exists return 0.

Constraints:
1<=N,S<=10^5
-10^5<=A[i]<=10^5

Input: S = 15, arr = 10 5 2 7 1 9
Output: 4
"""

from typing import List
from sliding_window.utils import InvalidSizeError, InvalidValueError, SolutionNotFound, EmptyArrayError


def validate(arr, s):
    """Constraints"""
    max_array_length = pow(10, 5)
    min_array_length = 1
    max_element_limit = pow(10, 5)
    min_element_limit = -pow(10, 5)

    if not arr:
        raise EmptyArrayError(message='Empty list found', array_length=0)

    array_length = len(arr)
    max_element = max(arr)
    min_element = min(arr)

    if not (array_length <= max_array_length):
        raise InvalidSizeError(message='Please enter valid length of list', array_length=array_length)
    if not (min_array_length <= s <= max_array_length):
        raise InvalidSizeError(message='Please enter sum value within range', sum_value=s,
                               range=[min_array_length, min_array_length])
    if not (max_element <= max_element_limit):
        raise InvalidValueError(message='Please enter list elements within specified range', max_value=max_element)
    if not (min_element >= min_element_limit):
        raise InvalidValueError(message="Please enter list of all positive integers", min_value=min_element)


def execute(arr, s):
    sub_lists = list()
    for i in range(len(arr) + 1):
        for j in range(i + 1, len(arr) + 1):
            if sum(arr[i:j]) == s:
                sub_lists.append(len(arr[i:j]))
    if not sub_lists:
        raise SolutionNotFound('No Solution Found', value=0)
    return max(sub_lists)


def find_max_sum_list_length(arr: List[int], s: int) -> int:
    validate(arr, s)
    return execute(arr, s)
