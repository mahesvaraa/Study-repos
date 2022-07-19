# Simple Pig Latin

https://www.codewars.com/kata/520b9d2ad5c005041100000f

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks
untouched.

**Examples**

```python
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
```

# Solution

```python
def pig_it(text):
    return ' '.join([v[1:] + v[0] + 'ay' if v.isalpha() else v for v in text.split()])
```