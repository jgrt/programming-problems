"""
https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not/0

Given two arrays A and B of equal size, the task is to find if given arrays are equal or not.
Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements
may be different though.
Return 1 if arrays are equal otherwise 0.
Constraints:
1 <= N <= 10^7
0 <= A[],B[] <= 10^18

Input: arr1 = 1 2 5 4 0, arr2 = 2 4 5 0 1
Output: 1
"""
from pydantic import BaseModel, Field, validator
from typing import List
import random


class ConstrainedArrays(BaseModel):
    array1: List[int] = Field(..., min_items=1, max_items=pow(10, 7))
    array2: List[int] = Field(..., min_items=1, max_items=pow(10, 7))

    @validator("*", pre=True, each_item=True)
    def elements_must_be_in_range(cls, v):
        assert 0 <= v <= pow(10, 18), 'must be within range {}'.format([0, pow(10, 18)])
        return v


def arrays_equal_or_not(arr1: List[int], arr2: List[int]) -> int:
    if len(arr1) != len(arr2):
        return 0
    if sorted(arr1) == sorted(arr2):
        return 1
    return 0


if __name__ == '__main__':
    array1 = [random.randrange(0, pow(10, 17)) for _ in range(pow(10, 6))]
    array2 = array1.copy()
    ConstrainedArrays(array1=array1, array2=array2)
    print(arrays_equal_or_not(array1, array2))
