sel# Decimal to Factorial and Back

https://www.codewars.com/kata/54e320dcebe1e583250008fd

Coding decimal numbers with factorials is a way of writing out numbers in a base system that depends on factorials,
rather than powers of numbers.

In this system, the last digit is always 0 and is in base 0!. The digit before that is either 0 or 1 and is in base 1!.
The digit before that is either 0, 1, or 2 and is in base 2!, etc. More generally, the nth-to-last digit is always 0, 1,
2, ..., n and is in base n!.

Read more about it at: http://en.wikipedia.org/wiki/Factorial_number_system

**Example**

The decimal number 463 is encoded as "341010", because:

```
463 = 3×5! + 4×4! + 1×3! + 0×2! + 1×1! + 0×0!
```

If we are limited to digits 0..9, the biggest number we can encode is 10!-1 (= 3628799). So we extend 0..9 with letters
A..Z. With these 36 digits we can now encode numbers up to 36!-1 (= 3.72 × 1041)

Task
We will need two functions. The first one will receive a decimal number and return a string with the factorial
representation.

The second one will receive a string with a factorial representation and produce the decimal representation.

Given numbers will always be positive.

# Solution

```python
def dec_2_fact_string(n):
    i, res = 1, []
    d = {36: 'Z', 35: 'Y', 34: 'X', 33: 'W', 32: 'V', 31: 'U', 30: 'T',
         29: 'S', 28: 'R', 27: 'Q', 26: 'P', 25: 'O', 24: 'N', 23: 'M',
         22: 'L', 21: 'K', 20: 'J', 19: 'I', 18: 'H', 17: 'G', 16: 'F',
         15: 'E', 14: 'D', 13: 'C', 12: 'B', 11: 'A', 10: '10'}

    while n != 0:
        res.insert(0, n % i if n % i < 10 else d[n % i + 1])
        n //= i
        i += 1

    return ''.join(map(str, res))


from math import factorial

d2 = {'Z': 35, 'Y': 34, 'X': 33, 'W': 32, 'V': 31, 'U': 30, 'T': 29,
      'S': 28, 'R': 27, 'Q': 26, 'P': 25, 'O': 24, 'N': 23, 'M': 22,
      'L': 21, 'K': 20, 'J': 19, 'I': 18, 'H': 17, 'G': 16, 'F': 15,
      'E': 14, 'D': 13, 'C': 12, 'B': 11, 'A': 10}


def fact_string_2_dec(string):
    x, n = 0, len(string) - 1
    for i in string:
        x += int(i) * factorial(n) if i.isnumeric() else d2[i] * factorial(n)
        n -= 1
    return x
```