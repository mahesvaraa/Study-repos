# Lazy Repeater

https://www.codewars.com/kata/51fc3beb41ecc97ee20000c3

The makeLooper() function (make_looper in Python) takes a string (of non-zero length) as an argument. It returns a
function. The function it returns will return successive characters of the string on successive invocations. It will
start back at the beginning of the string once it reaches the end.

**For example:**

```python
abc = make_looper('abc')
abc()  # should return 'a' on this first call
abc()  # should return 'b' on this second call
abc()  # should return 'c' on this third call
abc()  # should return 'a' again on this fourth call
```

# Solution

```python
from collections import deque


class make_looper:

    def __init__(self, string):
        self.d = deque(string)

    def __call__(self):
        self.d.rotate(1)
        return self.d[-1]


""" OR """

from itertools import cycle


def make_looper2(string):
    return cycle(string).__next__
```