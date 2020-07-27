"""
https://practice.geeksforgeeks.org/problems/closest-number/0

Given non-zero two integers N and M. The problem is to find the number closest to N and divisible by M.
If there are more than one such number, then output the one having maximum absolute value.

Constraints:
    -1000 <= N, M <= 1000

Example:
    Input: N = 13, M = 4
    Output: 12
"""


def find_closest_number(n: int, m: int):
    if not (-1000 <= n <= 1000 and -1000 <= m <= 1000):
        return 'choose numbers between -1000 to 1000'
    q, r = divmod(n, m)
    if r == 0:
        return n
    first_closest = q*m
    second_closest = m*(q+1)
    dist1 = abs(n) - abs(first_closest)
    dist2 = abs(second_closest) - abs(n)
    if dist1 == dist2:
        if abs(first_closest) > abs(second_closest):
            return first_closest
        return second_closest
    elif abs(dist1) > abs(dist2):
        return second_closest

    return first_closest