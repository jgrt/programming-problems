"""
https://practice.geeksforgeeks.org/problems/triangular-number/0

Check whether the number is Triangular or not.
A number is termed as triangular number if we can represent it in the form of triangular grid of points such that
the points form an equilateral triangle and each row contains as many points as the row number,
i.e., the first row has one point, second row has two points, third row has three points and so on.
The starting triangular numbers are 1, 3 (1+2), 6 (1+2+3), 10 (1+2+3+4).

If the number is Triangular then return 1 otherwise 0.

Constraints:
1 <= N <= 10^7

Input: N = 4
Output: 0
Input: N = 15
Output: 1
"""
from pydantic import BaseModel, Field
from math import sqrt


class ConstrainedInteger(BaseModel):
    value: int = Field(..., ge=1, le=pow(10, 7))


def is_triangular_number(n: int) -> int:
    """
    natural number series sum formula:
    n(n+1)/2
    let N is sum of from 1 to n numbers
    n(n+1)/2 = N
    n^2 + n = 2N
    (n +1/2)^2 = 2N + 1/4
    n + 1/2 = sqrt(1+8N)/2
    n = (sqrt(1+8N)-1)/2
    """
    tri_s = (sqrt(1+8*n)-1)/2
    if int(tri_s) == tri_s:
        return 1
    return 0


if __name__ == '__main__':
    n = 345
    n = ConstrainedInteger(value=n).value
    print(is_triangular_number(n))
