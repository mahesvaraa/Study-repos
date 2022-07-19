# String incrementer

https://www.codewars.com/kata/54a91a4883a7de5d7800009c

Your job is to write a function which increments a string, to create a new string.

* If the string already ends with a number, the number should be incremented by 1.
* If the string does not end with a number. the number 1 should be appended to the new string.

**Examples:**

```python
foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100
```

Attention: If the number has leading zeros the amount of digits should be considered.

# Solutuion

```python
def increment_string(strng):
    res, idx = '', len(strng)
    for i in strng[::-1]:
        if i.isnumeric():
            res += i
            idx -= 1
        else:
            break
    res = res[::-1]
    return strng[:idx] + f'{int(res) + 1 if res else 1:0{len(res)}}'
```