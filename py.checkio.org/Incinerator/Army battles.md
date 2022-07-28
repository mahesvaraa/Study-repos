В прошлой миссии — Warriors — вы научились устраивать дуэли между 2 отдельными воинами. Отличная работа! Но давайте
перейдём к чему-то более эпичному — к армиям! В этой миссии ваша задача — добавить к уже существующим классам и функциям
новые.Одним из новых классов должен стать класс - Army , который будет обладать методом add_units() , позволяющим
добавлять выбранное количество воинов в армию. Первый добавленный юнит будет первым, кто вступит в бой, второй будет
вторым, и так далее. Также нужно создать класс Battle() с функцией fight() , которая будет устраивать сражения и
определять сильнейшую армию. Сражения между армиями происходят по следующему принципу:

* сперва проводится дуэль между первым воином первой армии и первым воином второй
* как только один из них погибает — в дуэль вступает следующий воин из той армии, которая потеряла бойца, а выживший
  воин со своим текущим здоровьем продолжает сражаться
* так продолжается до тех пор, пока все воины одной из армий не умрут. В этом случае функция battle() возвращает True ,
  если первая армия выиграла или False , если вторая оказалась сильнее.

Обратите внимание, что первая армия имеет преимущество, чтобы начать каждый бой!

![](https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/8f856023648b4e48837e1d2df1b434ff/battle.png)

# example

Пример :

```python

chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
fight(carl, mark) == False
carl.is_alive == False

my_army = Army()
my_army.add_units(Knight, 3)

enemy_army = Army()
enemy_army.add_units(Warrior, 3)

army_3 = Army()
army_3.add_units(Warrior, 20)
army_3.add_units(Knight, 5)

army_4 = Army()
army_4.add_units(Warrior, 30)

battle = Battle()

battle.fight(my_army, enemy_army) == True
battle.fight(army_3, army_4) == False

```

**Входные данные:** воины и армии.

**Выходные данные:** результат битвы (True или False).

**Как это используется:** Для разработки компьютерных игр.

**Предусловие:**

2 типа солдат

Во всех битвах каждая из участвующих армий очевидно не является изначально пустой.

# Solution

```python
class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack += 2


class Army:
    def __init__(self):
        self.army = []

    def __getitem__(self, item):
        return self.army[item]  # delegate to li.__getitem__

    def pop(self, item):
        self.army.pop(item)

    def len(self):
        return len(self.army)

    def all(self):
        return self.army

    def add_units(self, Warrior, count):
        for i in range(count):
            self.army.append(Warrior())


def fight(unit_1, unit_2):
    flag = 'First'
    while True:
        if flag == 'First':
            unit_2.health -= unit_1.attack
            flag = 'Second'
        else:
            unit_1.health -= unit_2.attack
            flag = 'First'
        if unit_1.health <= 0 or unit_2.health <= 0:
            break
    if unit_1.health <= 0:
        unit_1.is_alive = False
    if unit_2.health <= 0:
        unit_2.is_alive = False
    return unit_1.is_alive


class Battle:

    def fight(self, unit_1, unit_2):
        while True:
            flag = 'First'
            while True:
                if flag == 'First':
                    unit_2[0].health -= unit_1[0].attack
                    flag = 'Second'
                else:
                    unit_1[0].health -= unit_2[0].attack
                    flag = 'First'
                if unit_1[0].health <= 0:
                    unit_1.pop(0)
                if unit_2[0].health <= 0:
                    unit_2.pop(0)
                    flag = 'First'
                if unit_1.len() == 0 or unit_2.len() == 0:
                    break
            return bool(unit_1.all())


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")

```