def checkio(n, arr):
    # a = set()
    cnt, a = 1, []
    for i in arr:
        a.append(i)
        b = []
        for begin, end in sorted(a):
            if b and b[-1][1] >= begin - 1:
                b[-1][1] = max(b[-1][1], end)
            else:
                b.append([begin, end])
        if sum(map(lambda x: x[1] - x[0] + 1, b)) >= n:
            return cnt
        cnt += 1
        print(b, sum(map(lambda x: x[1] - x[0] + 1, b)))
    else:
        return -1


print(checkio(20, [[1, 2], [20, 30], [25, 28], [5, 10], [4, 21], [1, 6]]))
# assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
# assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
# assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
# assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
# assert checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
# assert checkio(1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"
