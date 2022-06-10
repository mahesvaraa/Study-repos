# The Cheapest Flight

«Нам нужно долететь домой как можно дешевле, чтобы больше денег осталось на подарки. Тётя Лида просила сыров разных, а
Вася хотел машинку новую. Я уже довольно долго смотрю на расписание, и мне начинает казаться, что некоторые самолёты
летают зря.»

На входе вы получаете расписание самолётов в виде массива, каждый элемент которого — это цена прямого воздушного
соединения двух городов (массив из 3 элементов: первые два — названия городов в виде строк, и третий — цена перелёта).

Самолёты летают в обе стороны и цена в обе стороны одинаковая. Есть вероятность, что соединения между городами может и
не быть.

Найдите цену самого дешёвого перелёта для городов, которые переданы 2-м и 3-м аргументами.

**Input:** 3 аргумента: расписание перелётов в виде массива массивов, город вылета, город назначения.

**Output**: Int. Лучшая цена.

**Example**:

```python
cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'A',
 'C') == 70
cheapest_flight([['A', 'C', 100],
  ['A', 'B', 20],
  ['B', 'C', 50]],
 'C',
 'A') == 70
 ```

**Как это используется**: Может быть использовано в повседневной жизни для нахождения оптимальной комбинации.

**Precondition**: Цена всегда int. В расписании рейсов есть хотя бы один элемент. Оба искомых города есть в расписании.

# Solution

```python
from typing import List


class Trip:
    def __init__(self, a, b):
        self.start = a
        self.finish = b
        self.variables = []

    def create(self, obj):
        self.variables.append(Flight(obj))

    def print(self):
        return list(self.variables)

    def min_price(self):
        return list(map(lambda x: x.min_price(self.start, self.finish), self.variables))


class Flight:
    def __init__(self, obj):
        self.arr = [obj]
        self.summ = obj[2]
        self.next = obj[1]

    def add(self, obj):
        self.arr.append(obj)
        self.next = obj[1]
        self.summ += obj[2]

    def min_price(self, a, b):
        if self.arr[0][0] == a and self.arr[-1][1] == b:
            return self.summ
        else:
            return 0

    def check(self, a, b):
        return self.arr[0][0] == a and self.arr[-1][1] == b

    def __repr__(self):
        return f'{self.__dict__}'


def cheapest_flight(costs: List, a: str, b: str) -> int:
    fly = Trip(a, b)
    massive = costs
    result = []

    for i in massive:
        if fly.start == i[0]:
            fly.create(i)
        elif fly.start == i[1]:
            fly.create([i[1], i[0], i[2]])
    for j in massive:
        for k in fly.variables:

            if k.check(a, b):
                continue

            if j[0] == k.arr[-1][1]:
                k.add(j)
                continue

            elif j[1] == k.arr[-1][1]:
                k.add([j[1], j[0], j[2]])
                continue

            if len(k.arr) > 1:
                if j[0] == k.arr[-2][1]:
                    fly.create(*k.arr[:-1])
                elif j[1] == k.arr[-2][1]:
                    fly.create(*k.arr[:-1])

        result = list(filter(lambda x: x != 0, fly.min_price()))

    return min(result) if result else 0


if __name__ == '__main__':
    print("Example:")
    print(cheapest_flight([['A', 'C', 40], ['A', 'B', 20], ['A', 'D', 20], ['B', 'C', 50], ['D', 'C', 70]], 'D','C'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert cheapest_flight([['A', 'C', 100], ['A', 'B', 20], ['B', 'C', 50]], 'A', 'C') == 70
    assert cheapest_flight([['A', 'C', 100], ['A', 'B', 20], ['B', 'C', 50]], 'C', 'A') == 70
    assert cheapest_flight([['A', 'C', 40], ['A', 'B', 20], ['A', 'D', 20], ['B', 'C', 50], ['D', 'C', 70]], 'D',
                           'C') == 60
    assert cheapest_flight([['A', 'C', 100], ['A', 'B', 20], ['D', 'F', 900]], 'A', 'F') == 0
    assert cheapest_flight([['A', 'B', 10], ['A', 'C', 15], ['B', 'D', 15], ['C', 'D', 10]], 'A', 'D') == 25
    print("Coding complete? Click 'Check' to earn cool rewards!")

```