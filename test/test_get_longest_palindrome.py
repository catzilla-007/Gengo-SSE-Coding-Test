from pytest import mark

from src.palindrome import get_longest_palindrome


palindromes = [
    ('abaxyzzyxf', 'xyzzyx'),
    ('amaiislee', 'ama'),
    ('nothine', ''),
]


@mark.parametrize('input,expected', palindromes)
def test_get_longest_palindrome(input, expected):
    assert get_longest_palindrome(input) == expected
