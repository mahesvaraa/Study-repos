# Primes in numbers

https://www.codewars.com/kata/54d512e62a5e54c96200019e

Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following
form :

```python
 "(p1**n1)(p2**n2)...(pk**nk)"
```

with the p(i) in increasing order and n(i) empty if n(i) is 1.

```python
Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
```

# Solution

```python
from collections import Counter


def prime_factors(n):
    def is_prime(num):
        if num < 2:
            return False
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True

    i, result, res = 2, '', []
    while n != 1:
        while n % i == 0:
            if is_prime(i):
                res.append(i)
                n /= i
                i = 2
                break
        else:
            i += 1

    for k, v in Counter(res).items():
        if v > 1:
            result += f'({k}**{v})'
        else:
            result += f'({k})'

```