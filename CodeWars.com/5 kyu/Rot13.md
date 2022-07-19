# Rot13

https://www.codewars.com/kata/530e15517bc88ac656000716

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet
should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

# Solution

```python
from string import ascii_lowercase as al, ascii_uppercase as au
def rot13(text):
    al2, au2 = al[13:] + al[:13], au[13:] + au[:13]
    trans_table = str.maketrans(dict(zip(al + au, al2 + au2)))
    return text.translate(trans_table)
```