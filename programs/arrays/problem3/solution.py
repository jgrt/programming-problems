"""
https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence/1

Given an array A of integers.
The task is to complete the function which returns an integer denoting the length of the longest sub-sequence such that
elements in the sub-sequence are consecutive integers, the consecutive numbers can be in any order.

Return length of longest consecutive increasing sub-sequence present in the array.

Constraints:
1 <= N <= 1000
1 <= Ai <= 10^8

Input: N = 7, array = 1 9 3 10 4 20 2
Output: 4
"""
from pydantic import BaseModel, Field, validator
from typing import List


class ConstrainedArray(BaseModel):
    array: List[int] = Field(..., min_items=1, max_items=1000)

    @validator('*', pre=True, each_item=True)
    def element_must_be_in_range(cls, v):
        assert 1 <= v <= pow(10, 8),  'must be in range {}'.format([1, pow(10, 8)])
        return v


def find_longest_subseq(arr: List[int]) -> int:
    arr = sorted(arr)
    n = len(arr)
    max_ending = max_so_far = 1
    for i in range(n-1):
        if arr[i+1] == arr[i]+1:
            max_ending += 1
        else:
            max_ending = 1
        if max_so_far < max_ending:
            max_so_far = max_ending
    return max_so_far


if __name__ == '__main__':
    array = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
    ConstrainedArray(array=array)
    print(find_longest_subseq(array))

