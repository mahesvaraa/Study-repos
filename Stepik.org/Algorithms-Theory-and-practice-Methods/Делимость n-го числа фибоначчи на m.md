# Числа Фибоначчи

Задача на программирование повышенной сложности: огромное число Фибоначчи по модулю

Даны целые числа 1 ≤ n ≤10 ^ 18 и 2 ≤ m ≤ 10 ^ 5, необходимо найти остаток от деления n-го числа Фибоначчи на m.

**Sample Input:**

```
10 2
```

**Sample Output:**

```
1
```

# Solution

```python
def fib_mod(n, m):
    a, b, res = 0, 1, []
    while True:
        res.append(a)
        a, b = b, (a + b) % m
        if a == 0 and b == 1: break
    return res[n % len(res)]

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
```