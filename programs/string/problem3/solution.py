"""
https://practice.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not/0

Given strings s1 and s2, you need to find if s2 is a rotated version of the string s1.
The strings are lowercase.
return 1 if s2 is a rotated version of s1; else return 0.

Constraints:
1 <= |s1|, |s2| <= 10^7

Input: s1 = 'geeksforgeeks', s2 = 'forgeeksgeeks'
Output 1
Input: s1 = 'mightandmagic', s2 = 'andmagicmigth'
0
"""


def is_string_rotated(s1: str, s2: str):
    if not (1 <= len(s1) <= 10000000 or 1 <= len(s2) <= 10000000):
        return 'please enter valid length of string which is b/w 1 and 10000000'
    s1 += s1
    if s2 in s1:
        return 1
    return 0
