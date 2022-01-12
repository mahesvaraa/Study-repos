from itertools import chain, combinations
# функция проверяющая вообще все комбинации

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)  # allows duplicate elements
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var, result = [], []
for i, combo in enumerate(powerset(stuff), 1):
    if combo != ():
        print('combo #{}: {}'.format(i, combo))
