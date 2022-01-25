n, *first = map(int, input().split())
k, *second = map(int, input().split())

def check(arr, k, r):
    l = 0
    while l <= r:
        try:
            m = (l + r) // 2
            if arr[m] == k:
                return m + 1
            elif arr[m] > k:
                r = m - 1
            elif arr[m] < k:
                l = m + 1
        except IndexError:
            return -1
    return -1


for i in second:
    print(check(first, i, n), end=' ')