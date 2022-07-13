# Caesar Cipher Helper

https://www.codewars.com/kata/526d42b6526963598d0004db

Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the
alphabet by however many spots the cipher was initialized to.

**For example:**

```python
c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'
```

If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
The shift will always be in range of [1, 26].

# Solution

```python
from string import ascii_uppercase


class CaesarCipher(object):

    def __init__(self, shift):
        self.alphabet = ascii_uppercase
        self.step = shift

    def encode(self, st):
        return ''.join(self.alphabet[(self.alphabet.index(char) + self.step) % len(self.alphabet)] if char in self.alphabet else char for char in st.upper())

    def decode(self, st):
        return ''.join(self.alphabet[(self.alphabet.index(char) - self.step) % len(self.alphabet)] if char in self.alphabet else char for char in st.upper())
```