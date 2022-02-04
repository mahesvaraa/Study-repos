from functools import reduce

coefficients, x = input().split(), int(input())


def evaluate(coefficients, x):
    arr = [x for i in range(len(coefficients))]
    step = [i for i in range(len(coefficients) - 1, -1, -1)]
    print(reduce(lambda x, y: x + y, map(lambda x, y, n: int(x) * y ** n, coefficients, arr, step)))


evaluate(coefficients, x)
