# Find the unique string

https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3

There is an array of strings. All strings contains similar letters except one. Try to find it!

```python
find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a'])  # => 'BbBb'
find_uniq(['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba'])  # => 'foo'
```

Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only
spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.

# Solution

```python
def find_uniq(arr):
    d = {}
    for i in arr:
        d.setdefault(''.join(sorted(set(i.lower()))), 0)
        d[''.join(sorted(set(i.lower())))] += 1
    return min(arr, key=lambda x: d[''.join(sorted(set(x.lower())))])
```