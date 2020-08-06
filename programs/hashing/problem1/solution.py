"""
https://practice.geeksforgeeks.org/problems/nuts-and-bolts-problem/0

Given a set of N nuts of different sizes and N bolts of different sizes.
There is a one-one mapping between nuts and bolts. Match nuts and bolts efficiently.

output the matched array of nuts and bolts in separate lines,.
return the elements in the following order ! # $ % & * @ ^ ~

Constraints:
1 <= N <= 9

Input: array1 = ^ & % @ # * $ ~ !, array2 = ~ # @ % & * $ ^ !
Output: ! # $ % & * @ ^ ~
        ! # $ % & * @ ^ ~
"""
from pydantic import BaseModel, Field, validator
from typing import List, Tuple


class ConstrainedArrays(BaseModel):
    array1: List[str] = Field(..., min_items=1, max_items=9)
    array2: List[str] = Field(..., min_items=1, max_items=9)

    @validator('array2', pre=True)
    def items_must_be_same(cls, v, values):
        if 'array1' in values:
            assert set(v) == set(values['array1'])
        return v


def sort_arrays(arr1: List[str], arr2: List[str]) -> Tuple[List[str], List[str]]:
    defined_order = ['!', '#', '$', '%', '&', '*', '@', '^', '~']
    defined_order_dict = {i: e for i, e in enumerate(defined_order)}
    f, s = zip(*[(e, e) for i, e in defined_order_dict.items() if e in arr1])
    return f, s


if __name__ == '__main__':
    array1 = ['@', '%', '$', '#', '^']
    array2 = ['%', '@', '#', '$', '^']
    ConstrainedArrays(array1=array1, array2=array2)
    print(sort_arrays(array1, array2))
