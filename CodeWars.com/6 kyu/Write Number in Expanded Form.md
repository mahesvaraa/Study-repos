# Write Number in Expanded Form

https://www.codewars.com/kata/5842df8ccbd22792a4000245

You will be given a number and you will need to return it as a string in Expanded Form. For example:

```python
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
```

NOTE: All numbers will be whole numbers greater than 0.

# Solution

```python
def expanded_form(n):
    dec = len(str(n)) - 1
    res = []
    while dec > 0:
        x = n  - n % (10 ** dec)
        res.append(x)
        n = n - x
        dec = len(str(n)) - 1
    if str(n)[-1] != '0':
        res.append(n % 10 )
    return ' + '.join(map(str, res))
```