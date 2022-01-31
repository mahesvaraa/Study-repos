import random

arr = [random.randint(-100, 100) for i in range(100)]
arr2 = arr

import time


def selectionsort(arr):
    for i in range(len(arr)):
        k = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]
    return arr


def heapsort(arr):
    h = arr.copy()
    for i in range(len(arr)):
        arr[i] = min(h)
        h.remove(min(h))
    return arr


def countsort(arr):
    from collections import Counter
    res = []
    c = list(Counter(arr).items())
    # print(c)
    for i, n in c:
        res += [i] * n
    return res


def numericsort(arr=[267, 507, 912, 215, 109, 213, 199, 216, 257]):
    arr = list(map(str, arr))
    for i in reversed(range(len(str(arr[0])))):
        arr.sort(key=lambda x: x[i])
    return arr


print(numericsort())


# print(selectionsort(arr2))
# print(heapsort(arr2))


def timed(f, *args, n_iter=100):
    acc = float('inf')
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


print(timed(heapsort, arr))
print(timed(selectionsort, arr))
print(timed(countsort, arr))


def countsort(arr):
    from collections import Counter
    res = []
    c = Counter(arr)

    for j in range(11):
        if c.get(j):
            res += [j] * c.get(j)

    return res


n = input()
arr = list(map(int, input().split()))
print(*countsort(arr))
