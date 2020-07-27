from programs.string.problem1.solution import transform_str_char_desc_order


def test_transform_str_char_desc_order_on_equal_length():
    s = 'for'
    resp = transform_str_char_desc_order(s)
    assert len(s) == len(resp)


def test_transform_str_char_desc_order_on_same_characters():
    s = 'for'
    resp = transform_str_char_desc_order(s)
    assert sorted(list(s)) == sorted(list(resp))