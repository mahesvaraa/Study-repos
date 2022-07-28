# (Ready for) Prime Time

https://www.codewars.com/kata/521ef596c106a935c0000519

We need prime numbers and we need them now!

Write a method that takes a maximum bound and returns all primes up to and including the maximum bound.

For example,

```python
11 = > [2, 3, 5, 7, 11]
```

# Solution

```python
def is_prime(num):
    if num < 2:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def prime(n):
    return [i for i in range(n + 1) if is_prime(i)]

```