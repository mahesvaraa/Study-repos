# Next bigger number with the same digits

https://www.codewars.com/kata/55983863da40caa2c900004e

Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its
digits. For example:

```python
12 ==> 21
513 ==> 531
2017 ==> 2071
```

```python
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
```

If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

```python
9 ==> -1
111 ==> -1
531 ==> -1
```

```python
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil
```

# Solution

```python
from itertools import permutations


def next_bigger(n):
    if str(n) == ''.join(sorted(str(n), reverse=True)):
        return -1
    for i, v in enumerate(str(n), 1):
        for j in sorted(permutations(str(n).replace(str(n)[:-i], ''))):
            #print(j)
            if int(str(n)[:-i] + ''.join(j)) > n:
                return int(str(n)[:-i] + ''.join(j))
    else:
        return -1
```