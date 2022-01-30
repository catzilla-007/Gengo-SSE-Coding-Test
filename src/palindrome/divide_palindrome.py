from .get_longest_palindrome import get_longest_palindrome


def divide_palindrome(word: str):
    p = word
    divided = []
    while p:
        pal = get_longest_palindrome(p)
        pos = word.find(pal)
        divided.append((pos, pal))
        p = p.replace(pal, '')

    divided.sort(key=lambda x: x[0])
    return [x[1] for x in divided]
