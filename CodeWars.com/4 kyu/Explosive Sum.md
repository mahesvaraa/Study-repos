# Explosive Sum

https://www.codewars.com/kata/52ec24228a515e620b0005ef

How many ways can you make the sum of a number?

In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of
writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the
same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct
ways:

```python
4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
```

**Examples**
**Basic**

```python
exp_sum(1)  # 1
exp_sum(2)  # 2  -> 1+1 , 2
exp_sum(3)  # 3 -> 1+1+1, 1+2, 3
exp_sum(4)  # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
exp_sum(5)  # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3
exp_sum(10)  # 42
```

**Explosive**

```python
exp_sum(50)  # 204226
exp_sum(80)  # 15796476
exp_sum(100)  # 190569292
```

See here for more examples.

# Solution

```python
def exp_sum(num):
    d = [[0] * (num + 1) for _ in range(num + 1)]

    def dec(n, k):
        if n >= 0 and k >= 0 and d[n][k] > 0:
            return d[n][k]
        if n < 0:
            return 0
        if n <= 1 or k == 1:
            return 1
        d[n][k] = dec(n, k - 1) + dec(n - k, k)
        return d[n][k]

    return dec(num, num)

```