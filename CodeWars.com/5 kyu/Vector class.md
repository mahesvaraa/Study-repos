# Vector class

https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4

Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

```python
a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
```

If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

* a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__
  method, so that str(a) == '(1,2,3)')
* an equals method, to check that two vectors that have the same components are equal

**Note**: the test cases will utilize the user-provided equals method.

# Solution

```python
from operator import add, sub, mul


class Vector:

    def __init__(self, args):
        self.arg = args

    def add(self, arr):
        return Vector(list(map(sum, zip(self.arg, arr.arg))))

    def equals(self, c):
        return self.arg == c.arg

    def subtract(self, arr):
        return Vector(list(map(sub, self.arg, arr.arg)))

    def dot(self, arr):
        return sum(map(mul, self.arg, arr.arg))

    def norm(self):
        return sum(map(lambda x: pow(x, 2), self.arg)) ** 0.5

    def __str__(self):
        return str(tuple(self.arg)).replace(' ', '')
```