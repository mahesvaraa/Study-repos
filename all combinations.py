from itertools import chain, combinations
# функция проверяющая вообще все комбинации

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)  # allows duplicate elements
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


stuff = [1, 2, 3, 4, 5]
var, result = [], []
for i, combo in enumerate(powerset(stuff), 0):
    if combo != ():
        print('combo #{}: {}'.format(i, list(combo)))

"""
RESULT:

combo #1: [1]
combo #2: [2]
combo #3: [3]
combo #4: [4]
combo #5: [5]
combo #6: [1, 2]
combo #7: [1, 3]
combo #8: [1, 4]
combo #9: [1, 5]
combo #10: [2, 3]
combo #11: [2, 4]
combo #12: [2, 5]
combo #13: [3, 4]
combo #14: [3, 5]
combo #15: [4, 5]
combo #16: [1, 2, 3]
combo #17: [1, 2, 4]
combo #18: [1, 2, 5]
combo #19: [1, 3, 4]
combo #20: [1, 3, 5]
combo #21: [1, 4, 5]
combo #22: [2, 3, 4]
combo #23: [2, 3, 5]
combo #24: [2, 4, 5]
combo #25: [3, 4, 5]
combo #26: [1, 2, 3, 4]
combo #27: [1, 2, 3, 5]
combo #28: [1, 2, 4, 5]
combo #29: [1, 3, 4, 5]
combo #30: [2, 3, 4, 5]
combo #31: [1, 2, 3, 4, 5]
"""