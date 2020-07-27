"""
https://practice.geeksforgeeks.org/problems/series-ap/0

Given the first 2 terms A and B of an Arithmetic Series, tell the Nth term of the series.

Constraints:
    -10^3 <= A, B <= 10^3
    1 <= N <= 10000

Example:
For A=2, B=3 , Nth = 4 Output will be 5

"""


def arithmetic_progression(a: int, b: int, n: int):
    if not (-1000 <= a <= 1000 and -1000 <= b <= 1000):
        return 'choose numbers between -1000 to 1000'
    if not (1 <= n <= 10000):
        return 'choose nth number between 1 to 10000'
    d = abs(b) - abs(a)
    if d == 0:
        return "Both a and b are same"
    nth = a + (n - 1) * d
    return nth
