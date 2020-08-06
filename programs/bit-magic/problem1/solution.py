"""
https://practice.geeksforgeeks.org/problems/missing-number-in-array/0

Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing,
the missing number is to be found.
Return the missing number.

Constraints:
1 ≤ N ≤ 10^7
1 ≤ C[i] ≤ 10^7

Input: N = 5, arr = 1 2 3 5
Output: 4
"""
from pydantic import BaseModel, Field, validator
from typing import List


class ConstrainedArray(BaseModel):
    elements: List[int] = Field(..., min_items=1, max_items=pow(10, 7))

    @validator("*", pre=True, each_item=True)
    def elements_must_be_in_range(cls, v):
        assert 1 <= v <= pow(10, 7), 'must be within range {}'.format([1, pow(10, 7)])
        return v


def find_missing_number(n: int, arr: List[int]) -> int:
    series_sum = int((n*(n+1))/2)
    given_series_sum = sum(arr)
    return series_sum - given_series_sum


if __name__ == '__main__':
    n = 14
    arr = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14]
    arr = ConstrainedArray(elements=arr).elements
    print(find_missing_number(n, arr))
