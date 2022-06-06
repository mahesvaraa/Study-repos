# Microwave ovens

У вас на работе есть место для обеда, где находятся 3 микроволновых печи (Мicrowave1, Мicrowave2, Мicrowave3), которые
являются субклассами класса MicrowaveBase. Каждая печь может принимать команды от пульта дистанционного управления -
RemoteControl. Используемые команды:

```set_time ("xx:xx")```, где "xx:xx" - время в минутах и секундах, которое показывает, сколько будет разогреваться еда.
Например: set_time("05:30")

```add_time ("Ns"), add_time ("Nm")```, где N - количество секунд или минут, которое нужно добавить к текущему времени.

```del_time ("Ns"), del_time ("Nm")```, где N - количество секунд или минут, которое нужно отнять от текущего времени.

```show_time()``` , показывает текущее время выставленное на определенной печи.

Время по умолчанию равно 00:00. Обратите внимание, что время не может быть меньше 00:00 и больше 90:00, даже если
add_time или del_time приводят к подобной ситуации.

Ваша задача - создать все необходимые классы (родительский класс MicrowaveBase, 3 класса для печей и RemoteControl) и
реализовать управление каждой микроволновкой с помощью общего пульта RemoteControl(microwave), где microwave - одна из 3
микроволновых печей, которой должен управлять пульт (например, microwave = Microwave1())

Также обратите внимание, что только одна печь нормально отображает время - Microwave3. Две остальные печи имеют
поврежденные дисплеи и на месте определенного символа отображают лишь "_". Для первой печи такой символ - первый, для
второй - последний. Давайте рассмотрим это на примерах:

```python
microwave_1 = Microwave1()
microwave_2 = Microwave2()
microwave_3 = Microwave3()

RemoteControl(microwave_1).show_time() == "_0:00"
RemoteControl(microwave_2).show_time() == "00:0_"
RemoteControl(microwave_3).show_time() == "00:00"
```

В этой миссии вам может помочь такой шаблон проектирования, как Bridge . Основная задача шаблона - отделить абстракцию
от её реализации так, чтобы то и другое можно было изменять независимо.

# Примеры

```python
microwave_1 = Microwave1()
microwave_2 = Microwave2()
microwave_3 = Microwave3()

remote_control_1 = RemoteControl(microwave_1)
remote_control_1.set_time("01:00")

remote_control_2 = RemoteControl(microwave_2)
remote_control_2.add_time("90s")

remote_control_3 = RemoteControl(microwave_3)
remote_control_3.del_time("300s")
remote_control_3.add_time("100s")

remote_control_1.show_time() == "_1:00"
remote_control_2.show_time() == "01:3_"
remote_control_3.show_time() == "01:40"
```

**Входные данные:** методы класса RemoteControl и время.

**Выходные данные:** время на экране определенной микроволновой печи.

**Как это используется:** Для работы со временем.

**Предусловие:** 00:00 <= время <= 90:00

```python
class MicrowaveBase:
    def __init__(self):
        self.time = 0
        self.table_time = '00:00'


class Microwave1(MicrowaveBase):
    def show_time(self):
        return '_' + self.table_time[1:]


class Microwave2(MicrowaveBase):
    def show_time(self):
        return self.table_time[:-1] + '_'


class Microwave3(MicrowaveBase):
    def show_time(self):
        return self.table_time


class RemoteControl:
    def __init__(self, Microwave_class):
        self.Microwave = Microwave_class

    def border_time(self):
        if self.Microwave.time > 5400:
            self.Microwave.time = 5400
        if self.Microwave.time < 0:
            self.Microwave.time = 0
        self.Microwave.table_time = '{:02}'.format(self.Microwave.time // 60) + ":" + '{:02}'.format(
            self.Microwave.time % 60)

    def set_time(self, str_time):
        minutes, seconds = int(str_time.split(':')[0]), int(str_time.split(':')[1])
        self.Microwave.time = minutes * 60 + seconds
        self.border_time()

    def add_time(self, str_time):
        if str_time[-1] == 's':
            self.Microwave.time += int(str_time[:-1])
        elif str_time[-1] == 'm':
            self.Microwave.time += int(str_time[:-1]) * 60
        self.border_time()

    def del_time(self, str_time):
        if str_time[-1] == 's':
            self.Microwave.time -= int(str_time[:-1])
        elif str_time[-1] == 'm':
            self.Microwave.time -= int(str_time[:-1]) * 60
        self.border_time()

    def show_time(self):
        return self.Microwave.show_time()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")

    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")
    print(remote_control_1.show_time())
    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")


```