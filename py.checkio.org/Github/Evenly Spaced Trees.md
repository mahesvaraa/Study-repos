# Evenly Spaced Trees
Вам нужно добавить несколько деревьев и расположить их на одинаковом расстоянии.

Вам дан список целых чисел (ints) в качестве входного значения. Это расположение существующего дерева. Вы должны вернуть минимальное количество дополнительных деревьев необходимых для их равномерного распределения.

Позиции существующих деревьев уже отсортированы.
Все позиции деревьев целые числа (ints).
![](https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/55be50e475a64ec9b5043d8e3d4052fe/example_01.png)
Пример:
```python
evenly_spaced_trees([0, 2, 6]) == 1 # add to 4.
evenly_spaced_trees([1, 3, 6]) == 3 # add to 2, 4 and 5.
evenly_spaced_trees([0, 2, 4]) == 0 # no need to add.
```
**Входные данные**: Расположение существующего дерева (a list of ints).

**Выходные данные**: Минимальное количество дополнительных деревьев (int).

**Как это используется:**
Ландшафтный дизайн.

**Предварительное условие**:
0 ≤ Расположение дерева ≤ 100
3 ≤ Существующие деревья

# Solution
```python
from typing import List


def evenly_spaced_trees(trees: List[int]) -> int:
    res = []
    for i in range(1, trees[-1] + 1):
        arr = list(range(trees[0], trees[-1] + 1, i))
        if all(map(lambda x: x in arr, trees)) and arr[-1] == trees[-1]:
            res.append(len(arr))
    print(res)
    return min(res) - len(trees)



if __name__ == '__main__':
    print("Example:")
    print(evenly_spaced_trees([0, 2, 6]))
    assert evenly_spaced_trees([0, 2, 6]) == 1, 'add 1'
    assert evenly_spaced_trees([1, 3, 6]) == 3, 'add 3'
    assert evenly_spaced_trees([0, 2, 4]) == 0, 'no add'
    print("Coding complete? Click 'Check' to earn cool rewards!")
```