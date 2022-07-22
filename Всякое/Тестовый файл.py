from itertools import cycle


def josephus_survivor(n, k):
    x = list(range(1, n + 1))
    iterator = cycle(x.copy())
    n = 0
    for i in iterator:
        if i in x:
            n += 1
            if n % k == 0:
                x.remove(i)
        if len(x) == 1:
            return x[0]


k = 3

x = list(range(1, 8))
while x:
    kk = k - len(x) if k - len(x) > 0 else 0
    x = x + x[:kk]
    while len(x) < k:
        x += x
    x.pop(2)
    print(x[3:] + x[:3])
