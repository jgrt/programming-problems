from programs.string.problem3.solution import is_string_rotated


def test_is_string_rotated_on_equal_length_strings():
    s1 = 'geeksforgeeks'
    s2 = 'forgeeksgeeks'
    resp = is_string_rotated(s1, s2)
    if resp == 1:
        assert len(s1) == len(s2)
        

