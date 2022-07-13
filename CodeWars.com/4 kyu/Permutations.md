# Permutations

https://www.codewars.com/kata/5254ca2719453dcc0b00027d

In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. This
means, you have to shuffle all letters from the input in all possible orders.

**Examples**:

```python

* With input 'a'
* Your function should return: ['a']
* With input 'ab'
* Your function should return ['ab', 'ba']
* With input 'aabb'
* Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
```

The order of the permutations doesn't matter.

# Solution

```python
from itertools import permutations as pm
def permutations(string):
    return list(map(''.join, sorted(set(pm(string)))))
```