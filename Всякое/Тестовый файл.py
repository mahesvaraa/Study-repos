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
