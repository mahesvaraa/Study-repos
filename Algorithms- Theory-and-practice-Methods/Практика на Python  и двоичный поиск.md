```python
# наивный алгоритм
import sys

def find_pos(xs, query):
    try:
        return (xs.index(query) + 1)
    except ValueError:
        return (-1)

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *xs = next(reader)
    k, *queries = next(reader)
    for query in queries:
        print(find_pos(xs, query), end=" ")

if __name__ == '__main__':
    main()
```

```python
import sys

def find_pos(xs, query):
    #Invariant: lo <= pos <= hi
    lo, hi = 0, len(xs) - 1
    while lo <= hi:
        mid = (lo+hi) // 2
        if query < xs[mid]:
            hi = mid - 1    #[lo, mid - 1]
        elif query >xs[mid]:
            lo = mid + 1    #[mid + 1, hi]
        else:
            return mid + 1  #1-based
    return -1

def test():
    assert find_pos([], 42) == -1
    assert find_pos([42], 42) == 1
    assert find_pos([42], 24) == -1
    
def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *xs = next(reader)
    k, *queries = next(reader)
    for query in queries:
        print(find_pos(xs, query), end=" ")

if __name__ == '__main__':
    main()
```

```python
# c библиотекой
import sys
from bisect import bisect_left

def find_pos(xs, query):
    lo = bisect_left(xs, query)
    # i < lo : xs[i] < query
    # i > lo : xs[i] >=query
    if lo< len(xs) and xs[lo] == query:
        return lo + 1   #1-based
    else:
        return -1
    
def test():
    assert find_pos([], 42) == -1
    assert find_pos([42], 42) == 1
    assert find_pos([42], 24) == -1

def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *xs = next(reader)
    k, *queries = next(reader)
    for query in queries:
        print(find_pos(xs, query), end=" ")

if __name__ == '__main__':
    main()
```