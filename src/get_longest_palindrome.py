from .validator import validate_palindrome_character


def get_longest_palindrome(palindrome: str) -> str:
    validate_palindrome_character(palindrome)

    def insert_characters(word: str, c='.') -> str:
        return c.join([i for i in word])

    def is_l_bound(point, w):
        return point - (w + 1) >= 0

    def is_r_bound(point, w):
        return point + w + 1 < n

    def is_char_same(point, w):
        return pal[point - (w + 1)] == pal[point + w + 1]

    pal = insert_characters(palindrome)
    n = len(pal)
    longest = ''

    for m in range(n):
        width = 0
        while is_l_bound(m, width) and is_r_bound(m, width) and is_char_same(m, width):
            width += 1

        if len(longest) < len(pal[m - width: m + width + 1]):
            longest = pal[m - width: m + width + 1]

    return longest.replace('.', '')
