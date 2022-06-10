# The Highest Building

Архитектор собирается спроектировать новое самое высокое здание в городе.
Для этого ему сперва необходимо определить, какое из существующих зданий является самым высоким.
Помогите архитектору найти самое высокое здание в городе.
example

**Входные данные:** Высота зданий как двумерный массив.

**Выходные данные:** Номер дома и его высота как список(list) целых чисел (Примечание: в этой задаче, как и в реальной
жизни, номера домов начинаются с "1", а не с "0")

**Пример:**

```python

highest_building([[0, 0, 1, 0],
                  [1, 0, 1, 1],
                  [1, 1, 1, 1],
                  [1, 1, 1, 1]]) == [3, 4]
# здание №3 самое высокое, его высота = 4

```

**Как это используется:** Работа с двумерными массивами - очень важный навык в жизни программиста.

**Предусловия :**

```
array width <= 10
array height <= 10
```

В каждом массиве будет только 1 самое высокое здание

# Solution

```python
def highest_building(buildings):
    result = list(zip(*buildings))
    highest = max(result, key=lambda x: sum(x))
    return [result.index(highest) + 1, sum(highest)]

if __name__ == '__main__':
    print("Example:")
    print(highest_building([
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert highest_building([
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]) == [3, 4], "Common"
    assert highest_building([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1]
    ]) == [4, 1], "Cabin in the wood"
    assert highest_building([
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1]
    ]) == [1, 5], "Triangle"
    assert highest_building([
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]) == [4, 6], "Pyramid"
    print("Coding complete? Click 'Check' to earn cool rewards!")

```