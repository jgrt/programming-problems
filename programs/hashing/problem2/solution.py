"""
https://practice.geeksforgeeks.org/problems/array-subset-of-another-array/0

Given two arrays: arr1[0..m-1] of size m and arr2[0..n-1] of size n.
Task is to check whether arr2[] is a subset of arr1[] or not.
Both the arrays can be both unsorted or sorted. It may be assumed that elements in both array are distinct.
Return True if arr2 is subset of arr1 else False.

Constraints:
1 <= m,n <= 10^5
1 <= arr1[i], arr2[j] <= 10^5

Input: arr1 = 11 1 13 21 3 7
       arr2 = 11 3 7 1
Output: 1
"""
from pydantic import BaseModel, Field, validator
from typing import List
import random


class ConstrainedArrays(BaseModel):
    array1: List[int] = Field(..., min_items=1, max_items=pow(10, 5))
    array2: List[int] = Field(..., min_items=1, max_items=pow(10, 5))

    @validator("*", pre=True, each_item=True)
    def elements_must_be_in_range(cls, v):
        assert 0 <= v <= pow(10, 5), 'must be within range {}'.format([0, pow(10, 5)])
        return v

    @validator("array2", pre=True)
    def second_array_must_be_equal_or_smaller_than_first(cls, v, values):
        if 'array1' in values:
            assert len(v) <= len(values['array1']), 'second array must not be greater than first'
        return v


def is_subset(arr1: List[int], arr2: List[int]) -> bool:
    return all([j in arr1 for j in arr2])


if __name__ == '__main__':
    array1 = [11, 1, 13, 21, 3, 7, 11, 1, 13, 21, 3, 7]
    array2 = [11, 3]
    ConstrainedArrays(array1=array1, array2=array2)
    print(is_subset(array1, array2))
