def is_palindrome(palindrome: str) -> bool:
    n = len(palindrome)
    for i in range(n//2):
        if palindrome[i] != palindrome[n-i-1]:
            return False
    return True


def get_longest_palindrome(palindrome: str) -> str:
    def insert_characters(word: str, c='.') -> str:
        return c.join([i for i in word])

    def is_l_bound(point, w):
        return point - (w + 1) >= 0

    def is_r_bound(point, w):
        return point + w + 1 < n

    def is_char_same(point, w):
        return p[point - (w + 1)] == p[point + w + 1]

    p = insert_characters(palindrome)
    n = len(p)
    longest = ''

    for m in range(n):
        width = 0
        while is_l_bound(m, width) and is_r_bound(m, width) and is_char_same(m, width):
            width += 1

        if len(longest) < len(p[m - width: m + width + 1]):
            longest = p[m - width: m + width + 1]

    longest = longest.replace('.', '')
    if len(longest) <= 1:
        return ''

    return longest