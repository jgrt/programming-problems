"""
https://practice.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1

Given an array of integers and a number K.
Find the count of distinct elements in every window of size K in the array.

Return the values denoting counts of distinct numbers in all windows of size k in the array A[].

Constraints:
1 <= K <= N <= 10^5
1 <= A[i] <= 10^5 , for each valid i

Input: K = 4, arr = 1 2 1 3 4 2 3
Output: 3 4 4 3
"""
from typing import List, Union
from sliding_window.utils import InvalidSizeError, InvalidValueError, EmptyArrayError


def validate(arr, k):
    """Constraints"""
    max_array_length = pow(10, 5)
    max_sub_array_length = pow(10, 5)
    min_sub_array_length = 1
    max_element_limit = pow(10, 5)
    min_element_limit = 1

    if not arr:
        raise EmptyArrayError(message='Empty list found', array_length=0)
    if not k:
        raise EmptyArrayError(message='Zero length of sub array found', array_length=0)

    array_length = len(arr)
    max_element = max(arr)
    min_element = min(arr)

    if not (array_length <= max_array_length):
        raise InvalidSizeError(message='Please enter valid length of list', array_length=array_length)
    if not (k <= max_sub_array_length):
        raise InvalidSizeError(message='Please enter valid length of sub array or k', sub_array_length=k)
    if not (k >= min_sub_array_length):
        raise InvalidSizeError(message='Please enter positive value of k or sub array length', sub_array_length=k)
    if not (k <= array_length):
        raise InvalidSizeError(message='sub array length(k) must be equal or smaller than given array length ',
                               sub_array_length=k)
    if not (max_element <= max_element_limit):
        raise InvalidValueError(message='Please enter list elements within specified range', max_value=max_element)
    if not (min_element >= min_element_limit):
        raise InvalidValueError(message="Please enter list of all positive integers", min_value=min_element)


def execute(arr, k):
    distinct_elements = list()
    for i in range(len(arr) + 1):
        if i + k > len(arr):
            break
        distinct_elements.append(len(set(arr[i:i + k])))
    return distinct_elements


def find_distinct_elements(arr: List[int], k: int) -> List[int]:
    validate(arr, k)
    return execute(arr, k)
