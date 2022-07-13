# Сортировка вставками

import random

arr = [random.randint(-1000, 1000) for i in range(100)]
print(arr)


def insertsort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1
    print(arr)


# Сортировка выбором
def selectionsort(arr):
    for i in range(len(arr)):
        k = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]
    return arr


# Сортировка кучей
def heapsort(arr):
    h = arr.copy()
    for i in range(len(arr)):
        arr[i] = min(h)
        h.remove(min(h))
    return arr


# Быстрая сортировка
def quicksort(arr):
    if not arr:
        return arr
    pivot = arr.pop(len(arr) // 2)
    larr = list(filter(lambda x: x <= pivot, arr))
    rarr = list(filter(lambda x: x > pivot, arr))
    return quicksort(larr) + [pivot] + quicksort(rarr)
