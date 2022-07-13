# Alphabetized

https://www.codewars.com/kata/5970df092ef474680a0000c9

Re-order the characters of a string, so that they are concatenated into a new string in "
case-insensitively-alphabetical-order-of-appearance" order. Whitespace and punctuation shall simply be removed!

The input is restricted to contain no numerals and only words containing the english alphabet letters.

**Example**:

```python
alphabetized("The Holy Bible") # "BbeehHilloTy"
```

# Solution

```python
from string import ascii_uppercase as letters
def alphabetized(s):
    s = (i for i in s if i.upper() in letters)
    return ''.join(sorted(s, key=lambda x: letters.index(x.upper()))) 
```