from pytest import mark

from src.palindrome.is_palindrome import is_palindrome


valid_palindromes = [
    'aba',
    'qwertyytrewq',
    'zxcxz',
]


@mark.parametrize('palindrome', valid_palindromes)
def test_string_is_palindrome(palindrome):
    assert is_palindrome(palindrome) is True


invalid_palindromes = [
    'facebook',
    'gengo',
    'aahhaas',
]


@mark.parametrize('words', invalid_palindromes)
def test_string_is_not_palindrome(words):
    assert is_palindrome(words) is False


# test invalid input