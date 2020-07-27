from problem3.solution import find_closest_number


def test_find_closest_number_on_divisible_by_m():
    n = 17
    m = 6
    resp = find_closest_number(n, m)
    assert resp%m == 0