from programs.string.problem2.solution import good_or_bad_str


def test_good_or_bad_str_on_bad_string_length():
    s = 'bcdaeiou??'
    resp = good_or_bad_str(s)
    if resp == 0:
        assert len(s) > 3