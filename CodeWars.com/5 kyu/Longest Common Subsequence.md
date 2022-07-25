# Longest Common Subsequence

https://www.codewars.com/kata/52756e5ad454534f220001ef

Write a function called LCS that accepts two sequences and returns the longest subsequence common to the passed in
sequences.

**Subsequence**
A subsequence is different from a substring. The terms of a subsequence need not be consecutive terms of the original
sequence.

**Example subsequence**
Subsequences of "abc" = "a", "b", "c", "ab", "ac", "bc" and "abc".

**LCS examples**

```python
lcs("abcdef", "abc") = > returns
"abc"
lcs("abcdef", "acf") = > returns
"acf"
lcs("132535365", "123456789") = > returns
"12356"
```

Notes

* Both arguments will be strings
* Return value must be a string
* Return an empty string if there exists no common subsequence
* Both arguments will have one or more characters (in JavaScript)
* All tests will only have a single longest common subsequence. Don't worry about cases such as LCS( "1234", "3412" ),
  which would have two possible longest common subsequences: "12" and "34".

Note that the Haskell variant will use randomized testing, but any longest common subsequence will be valid.

Note that the OCaml variant is using generic lists instead of strings, and will also have randomized tests (any longest
common subsequence will be valid).

# Solution

```python
from itertools import combinations
import re


def lsc(st1, st2):
    max_st, min_st = sorted((st1, st2), key=len)
    for i in range(len(min_st) + 1):
        lst = list(filter(lambda x: x[1] is not None, (
            map(lambda x: (''.join(x), re.search('.*'.join(x), max_st) and re.search('.*'.join(x), min_st)),
                combinations(min_st, i)))))
        if lst:
            mx = lst[0][0]
    return mx
```