"""
https://practice.geeksforgeeks.org/problems/game-of-xor/0

You are given an array A[] of size N.
Now, we call the value of an array the bit-wise XOR of all elements it contains.
For example, the value of the array [1,2,3] = 1^2^3.
Now, Your task is to find the bit-wise XOR of the values of all sub arrays of array A.

Constraints:
1 <= N <= 1000
1 <= A[] <= 10000

Input: arr = 1 2 3
Output: 2
"""
from pydantic import BaseModel, Field, validator
from typing import List


class ConstrainedArray(BaseModel):
    elements: List[int] = Field(..., min_items=1, max_items=pow(10, 3))

    @validator("*", pre=True, each_item=True)
    def elements_must_be_in_range(cls, v):
        assert 1 <= v <= pow(10, 4), 'must be within range {}'.format([1, pow(10, 4)])
        return v


def game_of_xor(a: List[int]) -> int:
    n = len(a)
    if n % 2 == 0:
        return 0
    xor = 0
    for i in range(n+1):
        for j in range(i+1, n+1):
            sa = a[i:j]
            partial_xor = 0
            for k in range(len(sa)):
                partial_xor = partial_xor ^ sa[k]
            xor = xor ^ partial_xor
    return xor


if __name__ == '__main__':
    arr = [1, 2, 3]
    arr = ConstrainedArray(elements=arr).elements
    print(game_of_xor(arr))
