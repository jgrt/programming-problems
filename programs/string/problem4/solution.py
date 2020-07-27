"""
https://practice.geeksforgeeks.org/problems/non-repeating-character/0

Given a string S consisting of lowercase Latin Letters. Find the first non repeating character in S.
return the first non repeating character present in string. Return -1 if there is no non repeating character.

Constraints:
1 <= |S| <= 10^4

Input: S = hello
Output: h
Input: S = zxvczbtxyzvy
Output: c
Input: S = xxyyzz
Output: -1
"""


def find_non_repeating_char(s: str) -> (str, int):
    if not (1 <= len(s) <= 10000):
        return "Enter valid length of string"
    s_list = list(s)
    for i, char in enumerate(s_list):
        rem_str = "".join(s_list[:i]) + "".join(s_list[i+1:])
        if char not in rem_str:
            return char
    return -1