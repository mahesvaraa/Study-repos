import colorama
from colorama import Fore, Back, Style  # цветная консоль
from matplotlib import pyplot as plt
import time
from functools import lru_cache

colorama.init()


def timed(f, *args, n_iter=100):
    acc = float('inf')
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


print(Fore.RED + '# fib1 #' + Style.RESET_ALL)


def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)


print(fib1(8), '# time =', timed(fib1, 8))
# print(fib1(80)) # долго
cache = {}
print(Fore.RED + '# fib 2 # ' + Style.RESET_ALL)


def fib2(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n - 1) + fib2(n - 2)
    return cache[n]


print(fib2(8), '# time =', timed(fib2, 8))
print(fib2(80), '# time =', timed(fib2, 80))  # быстро


def memo(f):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return inner


print(Fore.RED + '# memo fib1 #' + Style.RESET_ALL)


@memo
def fib1(x):
    assert x >= 0
    return x if x <= 1 else fib1(x - 1) + fib1(x - 2)


print(fib1(8), '# time =', timed(fib1, 8))
print(fib1(80), '# time =', timed(fib1, 80))
print(Fore.RED + '# lru_cache fib1 #' + Style.RESET_ALL)


@lru_cache(maxsize=None)
def fib1(x):
    assert x >= 0
    return x if x <= 1 else fib1(x - 1) + fib1(x - 2)


print(fib1(8), '# time =', timed(fib1, 8))
print(fib1(80), '# time =', timed(fib1, 80))
print(Fore.RED + '# fib3 #' + Style.RESET_ALL)


def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


print(fib3(8), '# time =', timed(fib3, 8))
print(fib3(80), '# time =', timed(fib3, 80))


def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
    plt.show()
    plt.legend()
    plt.grid(True)


compare([fib3], list(range(200)))
