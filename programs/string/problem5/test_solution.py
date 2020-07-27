from programs.string.problem5.solution import find_max_distinct_substr


def test_find_max_distinct_substr_on_valid_output_length():
    s = 'abababcdefab'
    resp = find_max_distinct_substr(s)
    assert resp <= len(s)