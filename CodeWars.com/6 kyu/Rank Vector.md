# Rank Vector

https://www.codewars.com/kata/545f05676b42a0a195000d95

Given an array (or list) of scores, return the array of ranks for each value in the array. The largest value has rank 1,
the second largest value has rank 2, and so on. Ties should be handled by assigning the same rank to all tied values.
For example:

```python
ranks([9,3,6,10]) = [2,4,3,1]
```

and

```python
ranks([3,3,3,3,3,5,1]) = [2,2,2,2,2,1,7]
```

because there is one 1st place value, a five-way tie for 2nd place, and one in 7th place.

# Solution

```python
def ranks(a):
    return list(map(lambda x: 1 + sorted(a, reverse=True).index(x), a))
```