from src.validators import validate_palindrome_character


def __insert_characters(word: str, c='.') -> str:
    return c.join([i for i in word])


def __is_l_bound(point, w):
    return point - (w + 1) >= 0


def __is_r_bound(point, w, n):
    return point + w + 1 < n


def __is_char_same(point, w, pal):
    return pal[point - (w + 1)] == pal[point + w + 1]


def get_longest_palindrome(palindrome: str) -> str:
    validate_palindrome_character(palindrome)

    pal = __insert_characters(palindrome)
    n = len(pal)
    longest = ''

    for m in range(n):
        width = 0
        while __is_l_bound(m, width) and __is_r_bound(m, width, n) and \
                __is_char_same(m, width, pal):
            width += 1

        if len(longest) < len(pal[m - width: m + width + 1]):
            longest = pal[m - width: m + width + 1]

    return longest.replace('.', '')
