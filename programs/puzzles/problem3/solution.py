""""
https://practice.geeksforgeeks.org/problems/is-square/0

Given four different points in space. Find whether these points can form a square or not.
return "Yes" if it is square else "No".

Constraints:
1 ≤ x1, x2, x3, x4, y1, y2, y3, y4 ≤ 100

Input: (20, 10), (10, 20), (20, 20), (10, 10)
Output: Yes
"""
from pydantic import BaseModel, Field, validator
from typing import List, Tuple


class ConstrainedArray(BaseModel):
    elements: List[Tuple[int, int]] = Field(..., min_items=4, max_items=4)

    @validator("*", pre=True, each_item=True)
    def elements_must_be_in_range(cls, v):
        assert 1 <= v <= 100, 'must be in range {}'.format([1, 100])
        return v


def is_square(coor: List[Tuple[int, int]]) -> bool:
    s = sorted(coor, key=lambda t: (t[0], t[1]))
    a = s[2][0] - s[0][0]
    b = s[3][0] - s[1][0]
    c = s[1][1] - s[0][1]
    d = s[3][1] - s[2][1]
    if len({a, b, c, d}) == 1:
        return True
    return False


if __name__ == '__main__':
    l = [(20, 10), (10, 20), (20, 20), (10, 10)]
    coor = ConstrainedArray(elements=l).elements
    print(is_square(coor))
