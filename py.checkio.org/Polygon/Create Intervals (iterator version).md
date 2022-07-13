# Create Intervals (iterator version)

Из множества целых чисел(int) (которые будут представлены как итератор отсортированного списка) вам нужно создать
список(list) замкнутых интервалов в виде кортежей(tuple) таких, чтобы интервалы охватывали все значения, найденные в
множестве. После чего ваша функция должна вернуть объект-итератор, ссылающийся на полученный список.

Замкнутый интервал включает в себя конечные точки! Интервал 1..5 , например, включает каждое значение x , которое
удовлетворяет условию: 1 <= x <= 5 .

Значения могут быть в одном интервале только если разность между значением и следующим меньшим значением в наборе равно
единице, иначе начинается новый интервал. Отдельное значение, которое не вписывается в существующие правила формирования
интервалов, становится начальной и конечной точкой нового интервала.

Входные данные: итератор отсортированного списка целых чисел(int).

Выходные данные: объект-итератор, ссылающийся на список кортежей.

# Примеры

```python
list(create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))) == [
    (1, 5), (7, 8), (12, 12)]
list(create_intervals(iter(sorted(list({1, 2, 3, 6, 7, 8, 4, 5}))))) == [
    (1, 8)]
```

# Solution

```python
def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    try:
        res = [i for i in data]
        arr = [[res[0]]]
        j = 0
        for i in range(1, len(res)):
            if res[i] - res[i - 1] == 1:
                arr[j].append(res[i])
            else:
                j += 1
                arr.extend([[res[i]]])
        for i in range(len(arr)):
            arr[i] = (arr[i][0], arr[i][-1])

        return iter(arr)
    except:
        return iter([])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    res = create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))
    assert hasattr(res, '__iter__'), "your function should return the iterator object"
    assert hasattr(res, '__next__'), "your function should return the iterator object"

    assert list(create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))) == [
        (1, 5), (7, 8), (12, 12)], "First"
    assert list(create_intervals(iter(sorted(list({1, 2, 3, 6, 7, 8, 4, 5}))))) == [
        (1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
    print(create_intervals([]))

```

```python
def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """


    try:
        j = 0
        result = [[]]
        while True:
            try:
                next_item = next(data)
                if not result[j]:
                    result[j] = [next_item, next_item]
                else:
                    if result[j][1] + 1 == next_item:
                        result[j][1] = next_item

                    else:
                        j += 1
                        result.append([next_item, next_item])
            except StopIteration:
                break
        if result == [[]]:
            raise data
        return iter(result)
    except TypeError:
        return iter([])

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12})))))
    print(list(create_intervals([])))
```