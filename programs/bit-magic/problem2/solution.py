"""
https://practice.geeksforgeeks.org/problems/help-nobita/0

Given a string S of lowercase characters, find out whether the summation of 'X' and 'Y' is even or odd,
where X is the count of characters which occupy even positions in english alphabets and have even frequency,
and Y is the count of characters which occupy odd positions in english alphabets and have odd frequency.

Return EVEN if X+Y is even else ODD.

Constraints:
1 <= |S| <= 1000

Input: S = abbbcc
Output: ODD
"""
from pydantic import BaseModel, Field


is_even = lambda x: 1 if x % 2 == 0 else 0
is_odd = lambda x: 1 if x % 2 != 0 else 0


class ConstrainedString(BaseModel):
    value: str = Field(..., min_length=1, max_length=pow(10, 3), regex='[a-z]')


def even_or_odd(value: str) -> str:
    letters = list('abcdefghijklmnopqrstuvwxyz')
    letter_count = dict()
    for i in value:
        if i in letter_count:
            count = letter_count[i]
            letter_count[i] = count + 1
        else:
            letter_count[i] = 1
    x = y = 0
    for k, v in letter_count.items():
        letter_index = letters.index(k) + 1
        letter_occurrences = v
        if is_even(letter_index) and is_even(letter_occurrences):
            x += 1
        if is_odd(letter_index) and is_odd(letter_occurrences):
            y += 1
    if is_even(x + y):
        return 'EVEN'
    return 'ODD'


if __name__ == '__main__':
    val = 'nobitaa'
    value = ConstrainedString(value=val).value
    print(even_or_odd(value))
