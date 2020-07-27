"""
https://practice.geeksforgeeks.org/problems/sum-of-digit-is-pallindrome-or-not/0

Write a program to check if the sum of digits of a given number N is a palindrome number or not.

Constraints:
    10 <= N <= 1000

Example:
    Input: N = 56
    Output: Yes

    Input: N = 98
    Output: No
"""


def check_sum_palindrome(n: int) -> str:
    if n <= 10:
        return 'Enter bigger number then 10'
    sum_n = sum(list(map(int, str(n))))
    reverse_sum_n = int(str(sum_n)[::-1])
    if sum_n == reverse_sum_n:
        return 'YES'
    return 'NO'
