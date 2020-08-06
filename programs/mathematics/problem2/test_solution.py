import pytest
from mathematics.problem2.solution import arithmetic_progression


def test_arithmetic_progression_on_progression():
    a = 2
    b = 4
    n = 11
    resp = arithmetic_progression(a, b, n)
    resp1 = arithmetic_progression(a, b, n-1)
    assert abs(b) - abs(a) == abs(resp) - abs(resp1)
