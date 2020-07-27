"""
https://practice.geeksforgeeks.org/problems/print-the-pattern-set-1/1

You have given a number N. You need to return the pattern list for the given value of N.

Constraints:
    1 <= N <= 40

Example:

    Input: N = 3
    Output:
    3 3 3 2 2 2 1 1 1
    3 3 2 2 1 1
    3 2 1

"""


def create_pattern(n: int):
    if not (1 <= n <= 40):
        return 'Enter integer b/w 1 and 40'
    pattern_list = list(range(n, 0, -1))
    output_list = []
    for r in range(n, 0, -1):
        final_pattern = sorted(pattern_list*r, reverse=True)
        output_list.append(''.join(map(str, final_pattern)))
    return output_list