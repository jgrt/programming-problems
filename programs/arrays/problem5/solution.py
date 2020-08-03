"""
https://practice.geeksforgeeks.org/problems/count-possible-triangles/0

Given an unsorted array of positive integers.
Find the number of triangles that can be formed with three different array elements as lengths of three sides of triangles.

Constraints:
3 <= N <= 10^3
1 <= arr[i] <= 10^5

Input: array = 3 5 4
Output: 1
"""
from pydantic import BaseModel, Field, validator
from typing import List
import time


class ConstrainedArray(BaseModel):
    elements: List[int] = Field(..., min_items=3, max_items=pow(10, 3))

    @validator("*", pre=True, each_item=True)
    def elements_must_be_in_range(cls, v):
        assert 1 <= v <= pow(10, 5), 'must be within range {}'.format([1, pow(10, 5)])
        return v


def is_valid_triangle(*args):
    if len(set(args)) != 3:
        return 0
    if sum(args) <= 2*max(args):
        return 0
    return 1


def find_triangles(arr):
    # arr = ConstrainedArray(elements=arr).elements
    # arr = sorted(set(arr))
    triangles = 0
    n = len(arr)
    for i in range(0, n):
        for j in range(i, n):
            for k in range(j, n):
                triangles += is_valid_triangle(arr[i], arr[j], arr[k])
    return triangles


if __name__ == "__main__":
    input_array = list([3, 5, 4])
    arr = ConstrainedArray(elements=input_array).elements
    arr = sorted(set(arr))
    start = time.time()
    print(find_triangles(input_array))
    end = time.time()
    print(end-start)
