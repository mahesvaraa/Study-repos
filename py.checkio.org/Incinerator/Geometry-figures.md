# Geometry figures

Вам часто приходится работать с различными геометрическими фигурами и узнавать их параметры - периметр, площадь, объем.
Устав делать это вручную, вы решили автоматизировать процесс. Для этого вам необходимо создать класс Parameters и классы
геометрических фигур: круга, правильного треугольника, квадрата, правильного пятиугольника, правильного шестиугольника и
куба. Для всех фигур должны быть доступны методы:

perimeter() - возвращает периметр фигуры

area() - возвращает площадь фигуры

volume() - возвращает объем фигуры

Также вам необходимо реализовать метод choose_figure() для класса Parameters, с помощью которого можно будет выбирать,
по формулам какой геометрической фигуры следует считать параметры.

Так как все фигуры, кроме куба, не имеют объема, вам нужно будет вернуть 0, если метод volume() будет применен к любой
фигуре, кроме куба. Если результат получается без дробной части - верните его как int(), в ином случае - округлите до 2
знаков после запятой.

В этой миссии вам необходимо использовать такой шаблон проектирования, как Strategy .

# Примеры

```python
figure = Parameters(10)

figure.choose_figure(Circle())
figure.area() == 314.16

figure.choose_figure(Triangle())
figure.perimeter() == 30

figure.choose_figure(Square())
figure.area() == 100

figure.choose_figure(Pentagon())
figure.perimeter() == 50

figure.choose_figure(Hexagon())
figure.perimeter() == 60

figure.choose_figure(Cube())
figure.volume() == 1000
```

**Входные данные:** операторы и выражения, использующие класс Parameters и классы фигур.

**Выходные данные:** периметр, площадь или объем (число).

**Как это используется:** Для анализа геометрических объектов.

**Предусловие:** Все данные корректны.

# Solution

```python
class Parameters:
    def __init__(self, arg):
        pi = __import__('math').pi
        self.figure = None
        self.side = arg
        self.formula_area = {
            'Circle': pi * self.side ** 2,
            'Triangle': 3 ** 0.5 * self.side ** 2 / 4,
            'Square': self.side ** 2,
            'Pentagon': self.side ** 2 * (25 + 10 * 5 ** 0.5) ** 0.5 / 4,
            'Hexagon': 3 * 3 ** 0.5 * self.side ** 2 / 2,
            'Cube': 6 * self.side ** 2
        }
        self.formula_perimeter = {
            'Circle': pi * self.side * 2,
            'Triangle': 3 * self.side,
            'Square': self.side * 4,
            'Pentagon': self.side * 5,
            'Hexagon': self.side * 6,
            'Cube': self.side * 12
        }

    def choose_figure(self, Cls):
        self.figure = type(Cls).__name__

    def perimeter(self):
        return round(self.formula_perimeter[self.figure], 2)

    def area(self):
        return round(self.formula_area[self.figure], 2)

    def volume(self):
        if self.figure == 'Cube':
            return self.side ** 3
        else:
            return 0



class Circle:
    pass


class Triangle:
    pass


class Square:
    pass


class Pentagon:
    pass


class Hexagon:
    pass


class Cube:
    pass



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    figure = Parameters(10)

    figure.choose_figure(Circle())
    assert figure.area() == 314.16

    figure.choose_figure(Triangle())
    assert figure.perimeter() == 30

    figure.choose_figure(Square())
    assert figure.area() == 100

    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50

    figure.choose_figure(Hexagon())
    assert figure.perimeter() == 60

    figure.choose_figure(Cube())
    assert figure.volume() == 1000

    print("Coding complete? Let's try tests!")
```