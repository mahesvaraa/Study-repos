# Army units

Вы - разработчик новой игры-стратегии и вам необходимо добавить в игру процесс создания солдат. В первой версии игры
будет 2 типа солдат - азиатские (AsianArmy) и европейские (EuropeanArmy), в будущем будут добавляться и другие типы.
Каждый из типов должен являться наследником базового класса Army, в котором описаны методы создания различных видов
солдат. Каждый солдат будет экземпляром одного из 3 классов: Swordsman (мечник), Lancer (копейщик) или Archer (лучник).
У каждого типа армии есть свои названия для различных видов солдат. У европейской армии это Knight (для Swordsman),
Raubritter (для Lancer) и Ranger (для Archer). У азиатской: Samurai (для Swordsman), Ronin (для Lancer) и Shinobi (для
Archer). Методы для создания солдат следующие:

**train_swordsman (name)** - создает экземпляр класса Swordsman.

**train_lancer (name)** - создает экземпляр класса Lancer.

**train_archer (name)** - создает экземпляр класса Archer.

Все 3 класса специализаций (Swordsman, Lancer и Archer) должны обладать методом introduce() , который возвращает строку,
описывающую солдата в формате:
"'тип' 'имя', 'тип армии' 'специализация'", например:

"Raubritter Harold, European lancer"

"Shinobi Kirigae, Asian archer"

В этой миссии вам необходимо использовать паттерн проектирования - Abstract Factory .

# Пример

```python
my_army = EuropeanArmy()
enemy_army = AsianArmy()

soldier_1 = my_army.train_swordsman("Jaks")
soldier_2 = my_army.train_lancer("Harold")
soldier_3 = my_army.train_archer("Robin")

soldier_4 = enemy_army.train_swordsman("Kishimoto")
soldier_5 = enemy_army.train_lancer("Ayabusa")
soldier_6 = enemy_army.train_archer("Kirigae")

soldier_1.introduce() == "Knight Jaks, European swordsman"
soldier_2.introduce() == "Raubritter Harold, European lancer"
soldier_3.introduce() == "Ranger Robin, European archer"

soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
soldier_6.introduce() == "Shinobi Kirigae, Asian archer"
```

**Входные данные**: имена солдат и методы классов.

**Выходные данные:** Описание солдат.

**Как это используется:** Для разработки игр.

**Предусловия:** 2 типа армий. 3 типа солдат.

# Solution

```python
class Army(list):
    def __init__(self):
        super().__init__()
        self.class_names = {}

    def train_swordsman(self, name):
        return Swordsman(self.class_names, name=name, army=self.__str__)

    def train_lancer(self, name):
        return Lancer(self.class_names, name=name, army=self.__str__)

    def train_archer(self, name):
        return Archer(self.class_names, name=name, army=self.__str__)


class Soldier:
    def __init__(self, classnames, army, name):
        self.class_names = classnames
        self.name = name
        self.army = army()

    def introduce(self):
        return f'{self.class_names[type(self).__name__]} {self.name}, {self.army} {type(self).__name__.lower()}'


class Swordsman(Soldier):
    def __init__(self, class_names, army, name):
        super().__init__(class_names, army, name)


class Lancer(Soldier):
    def __init__(self, class_names, army, name):
        super().__init__(class_names, army, name)


class Archer(Soldier):
    def __init__(self, class_names, army, name):
        super().__init__(class_names, army, name)


class AsianArmy(Army):
    def __init__(self):
        super().__init__()
        self.class_names = {'Swordsman': 'Samurai', 'Lancer': 'Ronin', 'Archer': 'Shinobi'}

    def __str__(self):
        return 'Asian'


class EuropeanArmy(Army):
    def __init__(self):
        super().__init__()
        self.class_names = {'Swordsman': 'Knight', 'Lancer': 'Raubritter', 'Archer': 'Ranger'}

    def __str__(self):
        return 'European'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")
    print(soldier_1.introduce())
    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"

    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"

    print("Coding complete? Let's try tests!")

```