"""
https://practice.geeksforgeeks.org/problems/count-squares/0

Given a sample space S consisting of all perfect squares starting from 1, 4, 9 and so on.
You are given a number N, you have to return the number of integers less than N in the sample space S.

Constraints :
1<=N<=10^18

Input: N = 9
Output: 2
"""
from pydantic import BaseModel, Field
from math import sqrt


class ConstrainedInteger(BaseModel):
    value: int = Field(..., ge=1, le=pow(10, 18))


def count_squares(n: int) -> int:
    return int(sqrt(n-1))


if __name__ == '__main__':
    n = pow(10, 16)
    n = ConstrainedInteger(value=n).value
    print(count_squares(n))
