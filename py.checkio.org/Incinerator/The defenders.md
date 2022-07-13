# The defenders

В предыдущей миссии - Army battles вы научились устраивать сражения между двумя армиями. Но пока что у нас был всего 2
типа солдат - Warriors и Knights. Давайте добавим еще один тип - Defender. Он должен быть наследником класса Warrior и
иметь дополнительный параметр - defense (защита), который помогает ему выживать дольше. Когда другой солдат бьет
defender, то defender теряет здоровье в количестве: атака соперника - защита defender (если атака соперника больше, чем
защита defender). В ином случае defender не теряет здоровья. Базовые параметры класса Defender:
health = 60 attack = 3 defense = 2

![](https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/105a2136dc67401c809d4a5d266ddf3e/warrior_vs_defender.png)

# пример

```python
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
bob = Defender()
mike = Knight()
rog = Warrior()
lancelot = Defender()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
fight(carl, mark) == False
carl.is_alive == False
fight(bob, mike) == False
fight(lancelot, rog) == True

my_army = Army()
my_army.add_units(Defender, 1)

enemy_army = Army()
enemy_army.add_units(Warrior, 2)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Defender, 1)

army_4 = Army()
army_4.add_units(Warrior, 2)

battle = Battle()

battle.fight(my_army, enemy_army) == False
battle.fight(army_3, army_4) == True
```

**Входные данные:** воины и армии.

**Выходные данные:** результат сражения (True или False).

**Как это используется**: Для разработки компьютерных игр.

**Предусловие**: 3 типа солдат

# Solution

```python
class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50
        self.defense = 0
        self.is_alive = True

    def __str__(self):
        return 'Warrior'


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

    def __str__(self):
        return 'Knight'


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.defense = 2
        self.attack = 3

    def __str__(self):
        return 'Defender'


class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1


class Army:
    def __init__(self):
        self.army = []

    def __getitem__(self, item):
        return self.army[item]

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
            damage = unit_2.defense - unit_1.attack
            if damage < 0:
                unit_2.health = unit_2.health + damage
            flag = 'Second'

        else:
            damage = unit_1.defense - unit_2.attack
            if damage < 0:
                unit_1.health = unit_1.health + damage
            flag = 'First'
        print(unit_1, flag, unit_1.health, 'vs', unit_2.health, unit_2)
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
                    damage = unit_2[0].defense - unit_1[0].attack
                    if damage < 0:
                        unit_2[0].health = unit_2[0].health + damage
                    flag = 'Second'

                else:
                    damage = unit_1[0].defense - unit_2[0].attack
                    if damage < 0:
                        unit_1[0].health = unit_1[0].health + damage
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
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")

```