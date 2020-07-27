"""
https://practice.geeksforgeeks.org/problems/longest-distinct-characters-in-string/0

Given a string S, find and return length of the longest substring with all distinct characters.
For example, for input "abca", the output is 3 as "abc" is the longest substring with all distinct characters.

Constraints:
1 ≤ |S| ≤ 10000

Input: S = abababcdefababcdab
Output: 6
"""


def find_max_distinct_substr(s: str) -> str:
    if not (1 <= len(s) <= 10000):
        return "Please enter valid length of string"
    str_list = list(s)
    sub_strings = list()
    for i, char in enumerate(str_list):
        if i == 0:
            sub_strings.append(char)
        elif str_list[i] not in sub_strings[-1]:
            sub_strings[-1] = sub_strings[-1]+char
        else:
            sub_strings.append(char)

    return len(max(sub_strings, key=len))