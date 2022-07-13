# Back and forth then Reverse!

https://www.codewars.com/kata/60cc93db4ab0ae0026761232

**Task**
A list S will be given. You need to generate a list T from it by following the given process:

1. Remove the first and last element from the list S and add them to the list T.
2. Reverse the list S
3. Repeat the process until list S gets emptied.

The above process results in the depletion of the list S. Your task is to generate list T without mutating the input
List S.

**Example**

```python
S = [1,2,3,4,5,6]
T = []

S = [2,3,4,5] => [5,4,3,2]
T = [1,6]

S = [4,3] => [3,4]
T = [1,6,5,2]

S = []
T = [1,6,5,2,3,4]
return T
```

**Note**

* size of S goes up to 10^6
* Keep the efficiency of your code in mind.
* Do not mutate the Input.

# Solution

```python
def arrange(s):
    t = [s[0]] if len(s) > 0 else []
    for i in range(1, len(s) // 2 + 1, 2):
        if i > 0:
            t += [s[-i]]
        if i != len(s) - i:
            t += [s[-i - 1]]
        if i not in (len(s) - i, len(s) - i - 1):
            t += [s[i]]
        if i not in (len(s) - i, len(s) - i - 1, len(s) - i - 2):
            t += [s[i + 1]]

    return t

```