# Hamming Numbers

https://www.codewars.com/kata/526d84b98f428f14a60008da

A Hamming number is a positive integer of the form 2^i * 3^j * 5^k, for some non-negative integers i, j, and k.

Write a function that computes the nth smallest Hamming number.

**Specifically**:

* The first smallest Hamming number is 1 = 2^0 * 3^0 * 5^0
* The second smallest Hamming number is 2 = 2^1 * 3^0 * 5^0
* The third smallest Hamming number is 3 = 2^0 * 3^1 * 5^0
* The fourth smallest Hamming number is 4 = 2^2 * 3^0 * 5^0
* The fifth smallest Hamming number is 5 = 2^0 * 3^0 * 5^1
* The 20 smallest Hamming numbers are given in the Example test fixture.

Your code should be able to compute the first 5 000 ( LC: 400, Clojure: 2 000, NASM, C, C++, Go and Rust: 13 282 )
Hamming numbers without timing out.

# Solution

```python
def hamming(num):
    s = set(range(1, 6))
    res = [0, 1]
    for j in range(4999):
        n = min(s)
        if j == num - 1:
            return n
        s.remove(n)
        for i in range(2, 6):
            s.add(n * i)
```