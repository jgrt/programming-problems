"""
https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k/0

Given an array of integers and a number K. Write a program to find the maximum sum of a sub array of size K.
Return the maximum sum of a sub array of size K.

Constraints:
1<=N<=10^5
1<=K<=N

Input: K = 2, arr = 100 200 300 400
Output: 700
"""
from typing import List

from sliding_window.utils import InvalidSizeError, EmptyArrayError


def validate(arr, k):
    """Constraints"""
    max_array_length = pow(10, 5)
    max_sub_array_length = max_array_length
    min_sub_array_length = 1

    if not arr:
        raise EmptyArrayError(message='Empty list found', array_length=0)

    array_length = len(arr)

    if not (array_length <= max_array_length):
        raise InvalidSizeError(message='Please enter valid length of list', array_length=array_length)
    if not (k <= max_sub_array_length):
        raise InvalidSizeError(message='Please enter valid length of sub array or k', sub_array_length=k)
    if not (k <= array_length):
        raise InvalidSizeError(message='sub array length(k) must be equal or smaller than given array length ',
                               sub_array_length=k)
    if not (k >= min_sub_array_length):
        raise InvalidSizeError(message='Please enter positive value of sub array(k)', sub_array_length=k)


def execute(arr, k):
    sub_lists_sum = list()
    for i in range(len(arr) + 1):
        if i + k > len(arr):
            break
        sub_lists_sum.append(sum(arr[i:i + k]))
    return max(sub_lists_sum)


def find_max_sum(arr: List[int], k: int) -> int:
    validate(arr, k)
    return execute(arr, k)
