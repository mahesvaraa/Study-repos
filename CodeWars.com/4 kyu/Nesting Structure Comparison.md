# Nesting Structure Comparison

https://www.codewars.com/kata/520446778469526ec0000001

Complete the function/method (depending on the language) to return true/True when its argument is an array that has the
same nesting structures and same corresponding length of nested arrays as the first array.

For example:

```python
# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

```

# Solution

```python
def same_structure_as(original, other):

    def func(arr):
        return list(filter(lambda x: x in ['[', ']', ','], str(arr).replace("']'", '#',).replace("'['", '%')))
    return func(original) == func(other) or func(original)[::-1] == func(other)


# Понравилось решение
# def nones(itr):
#     return [nones(a) if isinstance(a, (list, tuple)) else None for a in itr]


# def same_structure_as(a, b):
#     return nones(a) == nones(b) if type(a) == type(b) else False
```