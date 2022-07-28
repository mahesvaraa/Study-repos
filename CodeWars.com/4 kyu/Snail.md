# Snail Sort

https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling
clockwise.

```python
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

snail(array) #=> [1,2,3,6,9,8,7,4,5]
```

For better understanding, please follow the numbers of the next array consecutively:

```python
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
```

This image will illustrate things more clearly:

![](http://www.haan.lu/files/2513/8347/2456/snail.png)

# Solution

```python
import itertools
def snail(arr):
    res = []
    while arr:
        res.append(arr[0])
        arr = list(reversed(list(zip(*arr[1:]))))
    return list(itertools.chain(*res))


# https://stackoverflow.com/questions/726756/print-two-dimensional-array-in-spiral-order
```