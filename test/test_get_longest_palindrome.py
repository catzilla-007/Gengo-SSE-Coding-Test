from pytest import mark

from src.palindrome.get_longest_palindrome import get_longest_palindrome


palindromes = [
    ('abaxyzzyxf', 'xyzzyx'),
    ('amaiislee', 'ama'),
    ('a', 'a'),
]


@mark.parametrize('param,expected', palindromes)
def test_get_longest_palindrome(param, expected):
    assert get_longest_palindrome(param) == expected
