# Simple Areas

Стефан постоянно работает с простыми фигурами, когда строит что либо. И ему не помешал бы специальный калькулятор для
расчетов расхода материалов. Давайте вспомним знания полученные на школьной скамье и достанем оттуда геометрию.

Вам нужно написать функцию для подсчета площади простых фигур: круга, прямоугольника и треугольника. Дано различное
число аргументов и в зависимости от их числа, ваша функция должна считать площадь различных фигур.
![](https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/c36e8316cdb34871897265aedca7f4d2/simple-areas.png)
Один аргумент -- диаметр круга и нужно рассчитать площадь круга.
Два аргумента -- стороны прямоугольника и нужна площадь этого прямоугольника.
Три аргумента -- длины сторон треугольника и нужно рассчитать площадь треугольника.

Результат должен быть с точностью до ±0.01.

**Примечания:** Думаю вы знаете, как работать с переменным числом аргументов .

**Входные данные**: Один, два или три аргумента, как числа (int, float).

**Выходные данные:** Площадь фигуры, как число (float, int).

Примеры:

```python
simple_areas(3) == 7.07
simple_areas(2, 2) == 4
simple_areas(2, 3) == 6
simple_areas(3, 5, 4) == 6
simple_areas(1.5, 2.5, 2) == 1.5
```

**Зачем это нужно**: Python может служить полезным инструментом для математиков и ученных. Вы легко можете реализовать
любую формулу или математические процедуры без использования сложных математических пакетов.

**Предусловия**:
0 < len(args) ≤ 3
all(0 < x ≤ 1000 for x in args)
Для случая с треугольником, любые две стороны в сумме больше третей.

# Solution

```python
def simple_areas(*args):
    if len(args) == 1:
        return args[0] * __import__('math').pi * args[0] / 4
    elif len(args) == 2:
        return args[0] * args[1]
    else:
        p = sum(args) / 2
        return (p * (p- args[0]) * (p - args[1]) * (p - args[2])) ** 0.5

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"

```