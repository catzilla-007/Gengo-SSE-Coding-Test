# Palindrome emordnilaP

From Merriam Webster's definition, a [palindrome](https://www.merriam-webster.com/dictionary/palindrome) 
is a word, verse, or sentence (such as "Able was I ere I saw Elba") or a number (such as 1881) 
that reads the same backward or forward.

Palindromes are one of the introductory problems we normally encounter
during academic days, it helped us understand and practice our sense of
string manipulation and array management.


## Setup

This project runs on `pipenv` and `python 3` so we recommend using `pipenv` in a python 3 environment.

```shell
$ pipenv install
```

## Usage

**Level 1: Checking if a string is a palindrome**

```shell
$ pipenv run palindrome --level=1 --string=aba

level: 1
string: aba
result: True
```

**Level 2: Get the longest palindrome in a string**

```shell
$ pipenv run palindrome --level=2 --string=asabada

level: 2
string: asabada
result: aba
```

**Level 3: Split string to palindromes**

```shell
$ pipenv run palindrome --level=3 --string=asabada

level: 3
string: asabada
result: ['s', 'aba', 'ada']
```


## Palindrome functionalities introspection

**Level 1: Checking if a string is a palindrome**

How do we technically validate if a string is a palindrome? How can we write it in code?
Well the logic for checking if a string is a palindrome is pretty straightforward.

Consider this string: `abcba`, now lets try folding this like a piece of paper vertically

```
a   a
 b b
  c
```

Notice a pattern? If yes, then you've got the idea now, checking if a string is a palindrome is
simply comparing if both ends of the string are the same.

This can be done with time complexity of **O(n)**.

As for the space complexity, since we really don't store temporary arrays
and only use a copy of the original string, we could say that it is within **Ω(n)**

**Level 2: Get the longest palindrome in a string**