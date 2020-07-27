"""
https://practice.geeksforgeeks.org/problems/good-or-bad-string/0

a String S is composed of lowercase alphabets and wildcard characters i.e. '?'.
Here, '?' can be replaced by any of the lowercase alphabets.
Now you have to classify the given String on the basis of following rules:

If there are more than 3 consonants together or more than 5 vowels together, the String is considered to be "BAD".
A String is considered "GOOD" only if it is not “BAD”.

For each test case,  return "1"  if string is GOOD, else return "0".

Constraints:
1 <= |S| <= 100

Input: S = bcdaeiou??
Output: 0
"""


def good_or_bad_str(s: str):
    if not (1 <= len(s) <= 100):
        return "please enter string with length b/w 1 and 100"
    vowels = ['a', 'e', 'i', 'o', 'u']
    wild_char = '?'
    str_vowels = []
    str_consonants = []
    for str in s:
        if str in vowels:
            str_vowels.append(str)
            str_consonants.append('/')
        elif str is wild_char:
            str_vowels.append(str)
            str_consonants.append(str)
        else:
            str_consonants.append(str)
            str_vowels.append('/')
    str_vowels = "".join(str_vowels).replace("?", "a").split("/")
    str_consonants = "".join(str_consonants).replace("?", "b").split('/')
    vowels_max = len(max(str_vowels, key=len))
    consonants_max = len(max(str_consonants, key=len))
    if vowels_max > 5 or consonants_max > 3:
        return 0
    return 1


print(good_or_bad_str('oa?a?avee'))

