# Числа Фибоначчи

Дано целое число 1 ≤ n ≤40, необходимо вычислить n-е число Фибоначчи

**Sample Input:**

```
3
```

**Sample Output:**

```
2
```

# Solution

```python
def fib(n):
    result = [0, 1]

    limit = n + 1

    while len(result) < limit:
        new = sum(result[-2:])
        result.append(new)
    
    return (result[-1], 0)[limit == 1]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
```