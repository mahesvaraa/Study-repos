# Break camelCase

https://www.codewars.com/kata/5208f99aee097e6552000148

Complete the solution so that the function will break up camel casing, using a space between words.

**Example**

```python

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```

# Solution

```python
def solution(s):
    return ''.join(i if i.islower() else ' ' + i for i in s  )
```