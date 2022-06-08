# Building base

Сингулярность всё-таки наступила, и мы обязаны построить идеальный робо-город для наших повелителей. В этом сияющем
робополисе все здания будут прямоугольными, а все улицы идти в направлениях "север-юг" и "восток-запад", образуя
восхитительную решётку. Прежде чем начать строительство, мы должны создать класс, представляющий совершенное здание.

Так как все здания в городе прямоугольные, и их стены параллельны улицам, мы можем определить любое здание, используя
только пару координат юго-западного угла, длину стен, идущих с запада на восток, длину стен, идущих с севера на юг, а
также высоту здания. Эти значения выражены как положительные числа в обычных единицах измерения. Начало координат
расположено в юго-западном углу города , следовательно, северные стороны зданий имеют значения координат больше, чем
южные. Для решения этой задачи нам потребуется разработать несколько методов. Описание класса смотрите далее.

```
class Building (south, west, width_WE, width_NS, height=10)
```

Возвращает новый экземпляр класса Building (класса здания) с юго-западным углом расположенным в точке с
координатами [ south , west ], длиной стен, идущих по направлению "восток-запад" - width_WE , длиной стен, идущих по
направлению "север-юг" - width_NS , и высотой height. Параметр height является положительным числом со значением по
умолчанию равным 10.

```
Building(10, 10, 1, 2, 2)
Building(10, 10, 1, 2, 2)
Building(0, 0, 10.5, 2.546)
Building(0, 0, 10.5, 2.546, 10)
```

**corners ()**

Возвращает словарь (dictionary) с координатами углов здания. Словарь имеет следующие ключи: "north-west", "north-east"
, "south-west", "south-east". Значениями являются списки (list) или кортежи (tuples) с двумя числовыми значениями.

```python
>> > Building(1, 2, 2, 2).corners()
{"north-west": [3, 2], "north-east": [3, 4], "south-west": [1, 2], "south-east": [1, 4]}
```

**area ()**

Возвращает площадь основания здания.

```python
>> > Building(1, 2.5, 4.2, 1.25).area()
5.25
```

**volume ()**

Возвращает объем здания.

```python
>> > Building(1, 2.5, 4.2, 1.25, 101).volume()
530.25
```

**__repr__ ()**

Это представление объекта Building в виде текстовой строки. Метод используется в функциях print или str (преобразование
в строку). Возвращает строку следующего вида:
"Building({south}, {west}, {width_we}, {width_ns}, {height})"

```python
>> > str(Building(0, 0, 10.5, 2.546))
"Building(0, 0, 10.5, 2.546, 10)"
```

В этом задании все входные данные коректны, и проверку значений можно не выполнять.

**Входные данные:** операторы и выражения, использующие класс Building.

**Выходные данные:** поведение экземпляра как описано выше.

**Как это используется**: Здесь вы изучите как создать простой класс с минимальной функциональностью к вящей славе
Робонии.

**Предусловие:** Все данные корректны.

# Solution

```python
class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        print(south, west, width_WE, width_NS)
        self.a = width_NS
        self.b = width_WE
        self.h = height
        self.north_west = [south + width_NS, west]
        self.north_east = [south + width_NS, west + width_WE]
        self.south_west = [south, west]
        self.south_east = [south, west + width_WE]

    def corners(self):
        d = {
            "north-west": self.north_west,
            "north-east": self.north_east,
            "south-west": self.south_west,
            "south-east": self.south_east
        }
        print(d)
        return d

    def area(self):
        return self.a * self.b

    def volume(self):
        return self.area() * self.h

    def __repr__(self):
        return f"Building({self.south_west[0]}, {self.south_west[1]}, {self.b}, {self.a}, {self.h})"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())


    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"

```