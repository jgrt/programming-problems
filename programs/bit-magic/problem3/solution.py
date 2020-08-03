"""
https://practice.geeksforgeeks.org/problems/flip-bits/0

Given an array arr[] consisting of 0’s and 1’s.
A flip operation is one in which you turn 1 into 0 and a 0 into 1.
You have to do at most one “Flip” operation of a sub-array.
Then finally display maximum number of 1 you can have in the array.

output a single integer representing the maximum number of 1's you can have in the array after at most one flip operation.

Constraints:
1 <= N <= 10^4
0 <= arr[i] <= 1

Input: arr = 1 0 0 1 0
Output: 4
"""
from pydantic import BaseModel, Field, validator
from typing import List


class ConstrainedArray(BaseModel):
    elements: List[int] = Field(..., min_items=1, max_items=pow(10, 4))

    @validator("*", pre=True, each_item=True)
    def elements_must_be_in_range(cls, v):
        assert 0 <= v <= 1, 'must be in range {}'.format([0, 1])
        return v


def flip_bits(arr: List[int]) -> int:
    zero_bits_seq = []
    n = len(arr)
    return 1


if __name__ == '__main__':
    arr = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]
    arr = ConstrainedArray(elements=arr).elements
    print(flip_bits(arr))