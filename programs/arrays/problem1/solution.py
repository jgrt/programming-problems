"""
https://practice.geeksforgeeks.org/problems/trapping-rain-water/0

Given an array arr[] of N non-negative integers representing height of blocks at index i as Ai where the width of
each block is 1. Compute how much water can be trapped in between blocks after raining.

Constraints:
3 <= N <= 10^7
0 <= Ai <= 10^8

Input: N = 4, Arr = 7 4 0 9
Output: 10
"""
from pydantic import BaseModel, Field, validator
from typing import List


class ConstrainedArray(BaseModel):
    elements: List[int] = Field(..., min_items=3, max_items=pow(10, 3))

    @validator("*", pre=True, each_item=True)
    def elements_must_be_in_range(cls, v):
        assert 0 <= v <= pow(10, 5), 'must be within range {}'.format([1, pow(10, 5)])
        return v


def water_restored(arr):
    n = len(arr)
    w = 0
    for i in range(1, n):
        left_max = i-1
        right_max = i+1
        # while left_max > 0 and right_max < n-1:
        while left_max > 0:
            if arr[left_max-1] > arr[left_max]:
                left_max = left_max-1
                left_max -= 1
        while right_max < n-1:
            if arr[right_max+1] > arr[right_max]:
                right_max = right_max+1
                right_max += 1
        print(i, left_max, right_max)


if __name__ == "__main__":
    arr = [1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    arr = ConstrainedArray(elements=arr).elements
    water_restored(arr)




