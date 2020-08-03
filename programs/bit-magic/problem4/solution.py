"""
https://practice.geeksforgeeks.org/problems/swap-all-odd-and-even-bits/0

Given an unsigned integer N. The task is to swap all odd bits with even bits.
For example, if the given number is 23 (00010111), it should be converted to 43(00101011).
Here, every even position bit is swapped with adjacent bit on right side and every odd position bit is swapped with adjacent
on left side.
Return the converted number.

Constraints:
1 ≤ N ≤ 100

Input: N = 23
Output: 43
"""
from pydantic import BaseModel, Field


class ConstrainedInteger(BaseModel):
    value: int = Field(..., ge=1, le=100)


def swap_bits(value: int) -> int:
    bin_repr = list(f"{value:08b}")
    for i in range(0, len(bin_repr)-1, 2):
        bin_repr[i], bin_repr[i+1] = bin_repr[i+1], bin_repr[i]
    return int("".join(bin_repr), 2)


if __name__ == '__main__':
    value = 43
    value = ConstrainedInteger(value=value).value
    print(swap_bits(value))
