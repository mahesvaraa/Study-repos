# The Clockwise Spiral

https://www.codewars.com/kata/536a155256eb459b8700077e

**Do you know how to make a spiral? Let's test it!**

Classic definition: A spiral is a curve which emanates from a central point, getting progressively farther away as it
revolves around the point.

Your objective is to complete a function createSpiral(N) that receives an integer N and returns an NxN two-dimensional
array with numbers 1 through NxN represented as a clockwise spiral.

Return an empty array if N < 1 or N is not int / number

**Examples:**

```python

N = 3
Output: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

1
2
3
8
9
4
7
6
5    
```

```python
N = 4
Output: [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

1
2
3
4
12
13
14
5
11
16
15
6
10
9
8
7
```

```python
N = 5
Output: [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]

1
2
3
4
5
16
17
18
19
6
15
24
25
20
7
14
23
22
21
8
13
12
11
10
9
```

# Solutuion

```python
def create_spiral(n):
    if not isinstance(n, int) or n < 1:
        return []
    m = n
    a = [[0] * m for _ in range(n)]

    i, j, d = 0, 0, 0
    moves = ((0, 1,), (1, 0,), (0, -1,), (-1, 0,),)
    for k in range(1, n * m + 1):
        a[i][j] = k
        for l in range(4):
            newD = (d + l) % 4
            di, dj = moves[newD]
            newI, newJ = i + di, j + dj
            if 0 <= newI < n and 0 <= newJ < m and a[newI][newJ] == 0:
                i, j, d = newI, newJ, newD
                break
    return a
```