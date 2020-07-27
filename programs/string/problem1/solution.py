"""
https://practice.geeksforgeeks.org/problems/sort-the-string-in-descending-order/0

Given a string S containing only lower case alphabets, the task is to sort it in lexigraphically-descending order.

Constraints:
1 <= |S| <= 10^5

Input: S = geeks
Output: skgee

"""


def transform_str_char_desc_order(s: str) -> str:
    if not (1 <= len(s) <= 100000):
        return "Please enter string len between 1 and 100000"
    desc_char_str = "".join(sorted(list(s), reverse=True))
    return desc_char_str