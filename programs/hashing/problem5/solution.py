"""
https://practice.geeksforgeeks.org/problems/first-element-to-occur-k-times/0

Given an array of N integers.
The task is to find the first element that occurs K number of times.
If no element occurs K times then return -1.

Constraints:
1 <= N, K <= 10^5
1<= A <= 10^6

Input: N = 7, K = 2, arr = 1 7 4 3 4 8 7
Output: 7
"""
from pydantic import BaseModel, Field, validator
from collections import Counter
from typing import List


class ConstrainedArray(BaseModel):
    elements: List[int] = Field(..., ge=1, le=pow(10, 5))
    count: int = Field(..., ge=1, le=pow(10, 5))

    @validator("elements", pre=True, each_item=True)
    def elements_must_be_in_range(cls, v):
        assert 1 <= v <= pow(10, 6), 'must be within range {}'.format([1, pow(10, 6)])
        return v

    @validator('count', pre=True)
    def count_must_be_less_or_equal_array_size(cls, v, values):
        if 'elements' in values and v > len(values['elements']):
            raise ValueError('k is greater than length of given array')
        return v


def first_element_to_occur_k_times(a: List[int], count: int) -> int:
    if len(a) == len(set(a)) and count > 1:
        return -1
    ele_freq = Counter(a)
    fdic = dict(filter(lambda item: count == item[1], ele_freq.items()))
    if bool(fdic):
        return list(fdic.keys())[0]
    return -1


if __name__ == '__main__':
    arr = [11, 4, 3, 4, 8, 7, 1, 3, 1, 3]
    k = 2
    values = ConstrainedArray(elements=arr, count=k)
    print(first_element_to_occur_k_times(arr, k))
