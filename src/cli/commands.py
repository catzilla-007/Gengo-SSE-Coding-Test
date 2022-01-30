import click

from src.palindrome.is_palindrome import is_palindrome
from src.palindrome.get_longest_palindrome import get_longest_palindrome
from src.palindrome.divide_palindrome import divide_palindrome


levels = '''set what palindrome function to use\n
1: check if word is palindrome\n
2: get palindrome in a string\n
3: divide palindromes in a string
'''


@click.command()
@click.option('--level', default=1, help=levels)
@click.option('--string', default='hello', help='the string that will be checked against palindrome function')
def palindrome(level, string):
    try:
        palindrome_methods = {
            1: is_palindrome,
            2: get_longest_palindrome,
            3: divide_palindrome,
        }
        output = palindrome_methods[level](string)

        click.echo(f'level: {level}')
        click.echo(f'string: {string}')
        click.echo(f'result: {output}')
    except Exception as e:
        click.echo(f'Failed to run palindrome function {e}')
