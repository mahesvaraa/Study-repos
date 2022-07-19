def fib(n):
    summ, n1, n2 = 0, 0, 1
    for i in range(n + 1):
        summ += n2 * 4
        n1, n2 = n2, n1 + n2
    return summ


print(fib(7))
