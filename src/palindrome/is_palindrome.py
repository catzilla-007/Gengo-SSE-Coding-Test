from src.validator import validate_palindrome_character


def is_palindrome(palindrome: str) -> bool:
    validate_palindrome_character(palindrome)
    n = len(palindrome)
    for i in range(n//2):
        if palindrome[i] != palindrome[n-i-1]:
            return False
    return True
