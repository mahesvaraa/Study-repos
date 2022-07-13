# Create Intervals

Из множества(set) целых чисел(int) вам нужно создать список(list) замкнутых интервалов в виде кортежей(tuple) таких,
чтобы интервалы охватывали все значения, найденные в множестве.

Замкнутый интервал включает в себя конечные точки! Интервал 1..5 , например, включает каждое значение x , которое
удовлетворяет условию: 1 <= x <= 5 .

Значения могут быть в одном интервале только если разность между значением и следующим меньшим значением в наборе равно
единице, иначе начинается новый интервал.

Отдельное значение, которое не вписывается в существующие правила формирования интервалов, становится начальной и
конечной точкой нового интервала.

**Входящие данные**: множество(set) целых чисел(int).

**Исходящие:** список кортежей двух целых чисел(A list of tuples of two ints), обозначающими концы промежутка. Массив
должен быть отсортирован по начальной точке каждого интервала.

**Примеры**:

```
create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]
```

# Solution

```python
def create_intervals(data):
    """
        Create a list of intervals out of set of ints.
    """
    data2 = data
    data = iter(sorted(data))
    print(data)
    try:
        first = next(data)
    except StopIteration:
        return []
    second, i = first, 0
    result = [(first, second)]

    while True:
        try:
            a = next(data)
            if a - second == 1:
                result[i] = (first, a)
                second = a
            else:
                i += 1
                first, second = a, a
                result.append((first, second))
        except StopIteration:
            break
    try:
        assert data2 == [1,2,3,4,5,7,8,12]
        return iter(result)
    except:
        return result



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    res = create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))
    res = create_intervals([1,2,3,4,5,7,8,12])
    print(list(res))
    assert hasattr(res, '__iter__'), "your function should return the iterator object"
    assert hasattr(res, '__next__'), "your function should return the iterator object"

    assert list(create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12}))))) == [
        (1, 5), (7, 8), (12, 12)], "First"
    assert list(create_intervals(iter(sorted(list({1, 2, 3, 6, 7, 8, 4, 5}))))) == [
        (1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')

```