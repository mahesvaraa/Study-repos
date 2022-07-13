# Integers: Recreation One

https://www.codewars.com/kata/55aa075506463dac6600010d

1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246. Squaring these divisors we get: 1, 60516, 4, 15129, 9,
6724, 36, 1681. The sum of these squares is 84100 which is 290 * 290.

Task
Find all integers between m and n (m and n integers with 1 <= m <= n) such that the sum of their squared divisors is
itself a square.

We will return an array of subarrays or of tuples (in C an array of Pair) or a string. The subarrays (or tuples or
Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the
squared divisors.

**Example**:

```python

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
```

The form of the examples may change according to the language, see "Sample Tests".

# Solution

```python
from itertools import chain

def list_squared(x, y):
    result = []
    for i in range(x, y + 1):
        divs = lambda n: chain(*((d, n // d) for d in range(1, int(n ** 0.5) + 1) if n % d == 0))
        res = list(set(divs(i)))
        sum_ = (sum(list(map(lambda x: x ** 2, res))))
        if sum_ ** 0.5 == int(sum_ ** 0.5):
            result.append([i, sum_])
    return result
```