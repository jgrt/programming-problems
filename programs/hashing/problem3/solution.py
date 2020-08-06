"""
https://practice.geeksforgeeks.org/problems/frequency-of-array-elements/0

Given an array A[] of N positive integers which can contain integers from 1 to N where elements can be repeated or
can be absent from the array. Your task is to count frequency of all elements from 1 to N.
output N size array of integers denoting the frequency of each element from 1 to N.

Constraints:
1 ≤ N ≤ 10^6
1 <= A[i] <= 10^6

Input: N = 5, arr = 2 3 2 3 5
Output: 0 2 2 0 1
"""
from pydantic import BaseModel, Field, validator
from typing import List
from collections import Counter


class ConstrainedArray(BaseModel):
    array: List[int] = Field(..., min_items=1, max_items=pow(10, 6))

    @validator("*", pre=True, each_item=True)
    def elements_must_be_in_range(cls, v):
        assert 1 <= v <= pow(10, 6), 'must be within range {}'.format([0, pow(10, 6)])
        return v


def elements_freq(arr: List[int]) -> List[int]:
    freq_dict = Counter(arr)
    return [freq_dict[i + 1] if i + 1 in freq_dict else 0 for i in range(len(arr))]


if __name__ == '__main__':
    array = [1, 2, 5, 5, 3]
    array = ConstrainedArray(array=array).array
    print(elements_freq(array))
