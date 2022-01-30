from .errors import InvalidInputError


def validate_palindrome_character(palindrome: str) -> None:
    if not isinstance(palindrome, str):
        raise InvalidInputError('Input should be a string')
    if len(palindrome) <= 0:
        raise InvalidInputError('Characters should be one or more')
