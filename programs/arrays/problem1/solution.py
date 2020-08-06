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


def water_restored(arr: List[int]) -> int:
    n = len(arr)
    w = 0
    left_max = arr[0]
    right_max = max(arr[1:])
    for i in range(n-1):
        if arr[i] > left_max:
            left_max = arr[i]
        if arr[i] == right_max:
            right_max = max(arr[i + 1:])
        h = min(left_max, right_max)
        w += max(h - arr[i], 0)
    return w


if __name__ == "__main__":
    array = [3, 0, 0, 2, 0, 4]

    ConstrainedArray(elements=array)
    print(water_restored(array))
