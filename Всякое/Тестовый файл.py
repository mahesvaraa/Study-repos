def checkio(cakes):
    res = list()

    for c in cakes:
        for a in cakes:
            for b in cakes:
                if c != a and c != b and a != b:
                    if (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1]) == 0:
                        if sorted((a, b, c)) not in res:
                            res.append(sorted((a, b, c)))

    res3 = res.copy()
    for i in res3:
        for j in res3:
            k = i
            i = sorted(i)
            j = sorted(j)
            if (i != j and i[0] == j[0] and i[1] == j[1] and i[2] < j[2]) or (
                    i != j and i[0] < j[0] and i[1] == j[1] and i[2] == j[2]) or (
                    i != j and i[0] == j[0] and i[1] < j[1] and i[2] == j[2]):
                try:
                    res.remove(k)
                except:
                    pass
    return len(res)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
