from functools import lru_cache
from math import factorial


@lru_cache()
def fac(n):
    return factorial(n)


def going(n):
    res = [1]
    for i in range(1, n + 1):
        res.append(res[i - 1] * i)
    summ = sum(res) - 1
    return float(str(summ / fac(n))[:8])
