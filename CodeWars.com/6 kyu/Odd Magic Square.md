# Odd Magic Square

https://www.codewars.com/kata/570b69d96731d4cf9c001597

Your task is to create a magic square for any positive odd integer N. The magic square contains the integers from 1 to N
* N, arranged in an NxN matrix, such that the columns, rows and both main diagonals add up to the same number.

Note: use have to use the Siamese method for this task.

Examples:

```python
n = 3
result = [
  [8, 1, 6],
  [3, 5, 7],
  [4, 9, 2]
]

```

```python
n = 5
result = [
  [17, 24,  1,  8, 15],
  [23,  5,  7, 14, 16],
  [ 4,  6, 13, 20, 22],
  [10, 12, 19, 21,  3],
  [11, 18, 25,  2,  9]
]
```

# Solution

```python
from math import floor
from itertools import chain
def magic_square(n):
    x = [[0 for i in range(n)] for j in range(n)]
    z, i, j = 1, 0, floor(n / 2)
    while 0 in chain(*x):
        if x[i % n][j % n] != 0:
            i, j = i + 2, j - 1
        x[i % n][j % n] = z
        z, i, j = z + 1, i - 1, j + 1
    return x
```