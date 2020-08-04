"""
https://practice.geeksforgeeks.org/problems/3-divisors/0

Given a value N.
The task is to find how many numbers less than or equal to N have numbers of divisors exactly equal to 3.

Constraints :
1 <= N <= 10^12

Input: N = 6
Output: 1
"""
from pydantic import BaseModel, Field
from math import sqrt


class ConstrainedInteger(BaseModel):
    value: int = Field(..., ge=1, le=pow(10, 12))


def three_divisors(n: int) -> int:
    l = int(sqrt(n+1))+1
    a = [True]*l
    for i in range(2, l):
        if a[i]:
            for j in range(i*2, l, i+2):
                a[j] = False
    a = [i**2 for i, ele in enumerate(a) if i > 1 and ele and i**2 <= n]
    return len(a)


if __name__ == '__main__':
    n = pow(10, 10)
    n = ConstrainedInteger(value=n).value
    print(three_divisors(n))
