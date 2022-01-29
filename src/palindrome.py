from math import floor


def is_palindrome(palindrome: str) -> bool:
    n = len(palindrome)
    for i in range(floor(n/2)):
        if palindrome[i] != palindrome[n-i-1]:
            return False
    return True
