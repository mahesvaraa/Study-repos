# Least Common Multiple

https://www.codewars.com/kata/5259acb16021e9d8a60010af

Write a function that calculates the least common multiple of its arguments; each argument is assumed to be a
non-negative integer. In the case that there are no arguments (or the provided array in compiled languages is empty),
return 1. If any argument is 0, return 0.

# Solution

```python
# from math import lcm
from functools import reduce


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mcd(n, m):
    return (n / gcd(n, m)) * m


def lcm(*args):
    lst = set(args)
    return reduce(mcd, lst) if lst else 1
```
