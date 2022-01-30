from pytest import raises, mark

from src.errors import InvalidInputError
from src.validator import validate_palindrome_character


def test_valid_input():
    assert validate_palindrome_character('some character') is None


invalid_inputs = [
    14624,
    '',
    2.3,
]


@mark.parametrize('invalid_input', invalid_inputs)
def test_invalid_input(invalid_input):
    with raises(InvalidInputError):
        validate_palindrome_character(invalid_input)
