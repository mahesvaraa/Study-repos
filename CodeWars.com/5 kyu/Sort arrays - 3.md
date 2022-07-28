# Sort arrays - 3

https://www.codewars.com/kata/51f42b1de8f176db5a0002ae

This time the input is a sequence of course-ids that are formatted in the following way:

name-yymm
The return of the function shall first be sorted by yymm, then by the name (which varies in length).

# Solution

```python
def sort_me(courses):
    return sorted(courses, key=lambda x: (int(x.split('-')[1]), x.split('-')[0], len(x.split('-')[0])))
```