# Counting Change Combinations

https://www.codewars.com/kata/541af676b589989aed0009e7

Write a function that counts how many different ways you can make change for an amount of money, given an array of coin
denominations. For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2:

```python
1+1+1+1, 1+1+2, 2+2.
```

The order of coins does not matter:

```python
1+1+2 == 2+1+1
```

Also, assume that you have an infinite amount of coins.

Your function should take an amount to change and an array of unique denominations for the coins:

```python
count_change(4, [1,2]) # => 3
count_change(10, [5,2,3]) # => 4
count_change(11, [5,7]) # => 0
```

# Solution

```python
def count_change(summa, nominals, lastindex=0, lst=None, res=None):
    if res is None:
        res = []
    if lst is None:
        lst = []
    if summa == 0:
        res.append(lst)

    else:
        for i in range(lastindex, len(nominals)):
            if nominals[i] <= summa:
                #cnt += 1
                count_change(summa - nominals[i], nominals, i, lst + [nominals[i]], res)
    return len(res)
```