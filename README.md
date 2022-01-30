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


## Palindrome functionalities

