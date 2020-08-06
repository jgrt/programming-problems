"""
https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0

Given an array of positive integers. Your task is to find the leaders in the array.
Note: An element of array is leader if it is greater than or equal to all the elements to its right side.
Also, the rightmost element is always a leader.

Constraints:
1 <= N <= 10^7
0 <= Ai <= 10^7

Input: N = 6, array = 16 17 4 3 5 2
Output: 17 5 2
"""
from pydantic import BaseModel, Field, validator
from typing import List
import time


class ConstrainedArray(BaseModel):
    elements: List[int] = Field(..., min_items=1, max_items=pow(10, 7))

    @validator("*", pre=True, each_item=True)
    def elements_must_be_in_range(cls, v):
        assert 0 <= v <= pow(10, 7), 'must be in range {}'.format([1, pow(10, 7)])
        return v


def find_leaders(arr: List[int]) -> List[int]:
    n = len(arr)

    if n == 1:
        return arr
    if arr == list(set(arr)):
        return arr[n-1:n]
    leaders = [arr[i] for i in range(n - 1) if max(arr[i + 1:]) < arr[i]]
    leaders.append(arr[-1])
    return leaders


if __name__ == '__main__':
    array = [1, 2, 3, 4]
    ConstrainedArray(elements=array)
    print(find_leaders(array))

