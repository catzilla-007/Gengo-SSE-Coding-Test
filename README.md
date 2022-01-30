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
simply comparing if both ends until the center of the string are the same.

This can be done with time complexity of **O(n)** since we only need to iterate the string in `n/2` time.

As for the space complexity, since we really don't store temporary arrays
and only use a copy of the original string, we could say that it is within **Ω(n)**



**Level 2: Get the longest palindrome in a string**

Getting the longest palindrome substring in a string is quite a bit more complex compared to the first level.
Contrary to the first logic, this time we need to check starting from the center of the 'supposed-to-be' palindrome.

With this we need to consider some scenarios first: what if the palindrome is even like `aabbaa`? Then it might be
challenging finding the center compared to `aabaa`. With this adding extra characters between the characters in the
string will be useful.

`aabbaa` can be transformed to `a.a.b.b.a.a`

The characters doesn't need to be a period, as long as the inserted characters are the same. This will prove neutral
when comparing both ends of the palindrome.

Now, how do we get a palindrome substring? Well, we need to check every character as the center of the palindrome.
Consider this example: `a.s.a.b.a.e.c`, the palindrome is `a.b.a`.

Now, we try to fold it starting from the center while checking incrementally if both ends are the same. If not, then we
look for another candidate center. Lets check below scenario:


```
a
  . s . a . b . a . e . c
```

```
  .
a   s . a . b . a . e . c
```

...and so forth... until...

```
            b
a . s . a .   . a . e . c
```

```
            b
          .   .
a . s . a       a . e . c
```

```
            b
          .   .
        a       a
a . s .           . e . c
```

We then store the highest 'fold' we found. And so, we continue...

```
              .
a . s . a . b   a . e . c
```

until the end of the string. At the end, it will return the longest palindrome we found.

Time complexity for this one is actually still **O(n)** since we loop the string once,
and we also loop characters starting from our candidate 'center'. But we know that 
the length of that loop will be less than `n`.

Space complexity is about **Ω(n)** since we really didn't store much information and only records
the longest string we found and worst case scenario for the longest palindrome is `n`.



**Level 3: Split string to palindromes**

Splitting subset palindromes in a string can be an extension of the last level. We can get the largest palindrome
in a string and then removing that subset to the original string until the original string is blank.

Time complexity of this will be `O(n^2)` since the worst case is that there is no palindrome in a string and then we
also use the previous level's function inside the loop which has a complexity of **O(n)**.

Space complexity for this is **Ω(2n)** since we store divided substrings in an array and the total size of the
substrings are n and also the space complexity from the last level (level2).
