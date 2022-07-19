# Greed is Good

https://www.codewars.com/kata/5270d0d18625160ada0000e4

Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw
according to these rules. You will always be given an array with five six-sided dice values.

```python
 Three
1
's => 1000 points
Three
6
's =>  600 points
Three
5
's =>  500 points
Three
4
's =>  400 points
Three
3
's =>  300 points
Three
2
's =>  200 points
One
1 = > 100
points
One
5 = > 50
point
```

A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (
contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

```python
 Throw
Score
---------   ------------------
5
1
3
4
1
250: 50(
for the 5) + 2 * 100 ( for the 1s)
1
1
1
3
1
1100: 1000(
for three 1s) + 100 ( for the other 1)
2
4
4
5
4
450: 400(
for three 4s) + 50 ( for the 5) 
```

In some languages, it is possible to mutate the input to the function. This is something that you should never do. If
you mutate the input, you will not be able to pass all the tests.

# Solution

```python
from collections import Counter


def score(dice):
    x = Counter(dice)
    res = 0
    for key, val in x.items():
        if val >= 3:
            res += (key * 100 if key != 1 else key * 1000)
            if key in [1, 5]:
                res += ((val - 3) * key * 10 if key != 1 else (val - 3) * 100)
        elif key in [1, 5]:
            res += (val * key * 10 if key != 1 else val * 100)
    return res
```