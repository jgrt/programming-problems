from problem4.solution import check_sum_palindrome


def test_check_sum_palindrome_on_palindrome_yes():
    n = 128
    resp = check_sum_palindrome(n)
    sum_n = sum(list(map(int, str(n))))
    if resp == "YES":
        assert sum_n == int(str(sum_n)[::-1])