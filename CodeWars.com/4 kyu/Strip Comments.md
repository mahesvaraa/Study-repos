# Strip Comments

https://www.codewars.com/kata/51c8e37cee245da6b40000bd

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace
at the end of the line should also be stripped out.

**Example:**

Given an input string of:

```python
apples, pears # and bananas
grapes
bananas !apples
```

The output expected would be:

```python
apples, pears
grapes
bananas
```

The code would be called like so:

```python
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
```

# Solution

```python
def strip_comments(strng, markers):

    strng = strng.splitlines()
    for i, v in enumerate(strng):
        for j in markers:
            if j in strng[i]:
                strng[i] = strng[i][:strng[i].index(j)].rstrip()
    return '\n'.join(strng)
```