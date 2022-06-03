# Every person is unique

С каждым годом количество ваших знакомых все увеличивается и следить за информацией об их жизнях становится всё сложнее.
Давайте упростим и немного автоматизируем этот процесс. В конце концов, именно облегчение рутинных процессов - одна из
ключевых задач программирования.

Вам необходимо создать класс Person, а также несколько методов для работы с его экземплярами. Описание класса смотрите
далее.

class Person (first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown')

Возвращает новый экземпляр класса Person c именем и фамилией [ first_name , last_name ], датой рождения - birth_date (в
формате 'dd.mm.yyyy'), текущим местом работы - job , количеством проработанных лет - working_years , средней зарплатой
за весь период работы - salary (сумма в месяц), страной и городом проживания - [ country , city ] и полом - gender .
Параметр gender может принимать значения 'male' или 'female'. Если этот параметр не задан, то значение по умолчанию - '
unknown'.

```python
Person(‘John’, ‘Smith’, ‘19.09
.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’) ==
Person(‘John’, ‘Smith’, ‘19.09
.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’)

Person(‘Hanna
Rose’, ‘May’, ‘05.12
.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’) ==
Person(‘Hanna
Rose’, ‘May’, ‘05.12
.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’, ‘unknown’)
```

**name ()**

Возвращает полное имя (имя и фамилию, разделенные пробелом).

```python
Person(‘John’, ‘Smith’, ‘19.09
.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’).name() == ‘John
Smith’
```

**age ()**

Возвращает возраст человека - количество полных прожитых лет. (Считайте текущим днем 01.01.2018)

```python
Person(‘John’, ‘Smith’, ‘19.09
.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’).age() == 38
```

**work ()**

Возвращает род занятий человека в предложении вида: ‘He is a ...’ (если male) ‘She is a ...’ (female) ‘Is a ...’ (
unknown) В зависимости того, какой пол человека задан (м/ж) или, если пол неопределен - возвращает без указания пола.

```python
Person(‘Hanna
Rose’, ‘May’, ‘05.12
.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’).work() == ‘Is
a
designer’
```

**money ()**

Возвращает количество денег, заработанное за весь период работы. Сумму следует выводить в формате xx xxx … - разбивая
каждых 3 разряда пробелами. Например: ‘10 568’ ‘1 051 422’

```python
Person(‘John’, ‘Smith’, ‘19.09
.1979’, ‘welder’, 15, 3600, ‘Canada’, ‘Vancouver’, ‘male’).money() == ‘648
000’
```

**home ()**

Возвращает страну и город проживания в формате: ‘Lives in city, country’

```python
Person(‘Hanna
Rose’, ‘May’, ‘05.12
.1995’, ‘designer’, 2.2, 2150, ‘Austria’, ‘Vienna’).home() == ‘Lives in Vienna, Austria’
```

В этом задании все входные данные коректны, и проверку значений можно не выполнять.

**Входные данные:** операторы и выражения, использующие класс Person.

**Выходные данные:** поведение экземпляра как описано выше.

**Как это используется:** Работа с классами и объектно-ориентированным программированием - более высокий уровень
мастерства, которым следует овладеть, чтобы иметь возможность использовать Python в полной мере.

**Предусловие:** Все данные корректны.

# Solution

```python
class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.job = job
        self.working_years = working_years
        self.country = country
        self.salary = salary
        self.city = city
        self.gender = gender

    def name(self):
        return f'{self.first_name} {self.last_name}'

    def age(self):
        return 2017 - int(str(self.birth_date)[-4:])

    def work(self):
        if self.gender == 'male':
            return f'He is a {self.job}'
        elif self.gender == 'female':
            return f'She is a {self.job}'
        else:
            return f'Is a {self.job}'

    def money(self):
        return '{0:,}'.format(self.salary * self.working_years * 12).replace(',', ' ')

    def home(self):
        return f'Lives in {self.city}, {self.country}'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    print("Coding complete? Let's try tests!")

```