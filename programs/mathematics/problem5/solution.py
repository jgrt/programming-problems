"""
https://practice.geeksforgeeks.org/problems/print-the-kth-digit/0

Given two numbers A and B, find Kth digit from right of A^B.

Constraints:
1 <= A , B <=15
1 <= K <= |total digits in A^B|

Example:
    Input: A = 3, B = 3, K = 1
    Output: 7

"""


def find_kth_digit(a: int, b: int, k: int):
    if not (1 <= a <= 15 and 1 <= b <= 15 and k >= 1):
        return 'Provide positive integer, not neutral integer as 0'
    apb = pow(a, b)
    if len(str(apb)) < k:
        return 'Provide integer 1 and {}'.format(len(str(apb)))
    return int(str(apb)[::-1][k-1])
