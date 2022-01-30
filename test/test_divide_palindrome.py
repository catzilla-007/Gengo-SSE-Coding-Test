from pytest import mark

from src.palindrome.divide_palindrome import divide_palindrome


palindromes = [
    ('noonabbad', ['noon', 'abba', 'd']),
    ('hello', ['h', 'e', 'll', 'o']),
]


@mark.parametrize('string,expected', palindromes)
def test_divide_palindrome(string, expected):
    assert divide_palindrome(string) == expected
