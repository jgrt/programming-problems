from programs.string.problem4.solution import find_non_repeating_char
from collections import Counter


def test_find_non_repeating_char_on_uniqueness():
    s = 'hello'
    resp = find_non_repeating_char(s)
    counts = Counter(s)
    if resp != -1:
        assert counts[resp] == 1


def test_find_non_repeating_char_on_not_found():
    s = 'aabbcc'
    resp = find_non_repeating_char(s)
    counts = Counter(s)
    if resp == -1:
        assert min(list(counts.values())) > 1
