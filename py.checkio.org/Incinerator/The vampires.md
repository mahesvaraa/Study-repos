# The vampires

Итак, у нас есть 3 типа солдат: Warrior, Knight и Defender. Давайте сделаем сражения армий еще более эпичными и добавим
новый тип юнитов - Vampire!

Vampire должен быть наследником класса Warrior и иметь дополнительный параметр - vampirism , который помогает ему
исцелять себя. Когда вампир наносит удар другому юниту, то восставнавливает себе здоровье в размере +50% от нанесенного
урона (защита соперника уменьшает наносимый вампиром урон и, соответственно, получаемое лечение).

Базовые параметры класса Vampire:
health = 40 attack = 4 vampirism = 50%

Вы должны хранить атрибут вампиризма как целое число (50 на 50%). Это необходимо для того, чтобы данное решение
развивалось в соответствии с одной из следующих задач этой саги.

![](https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/e698caf5f3e74bc499d4c1d8df4a7186/defender_vs_vampire.png)

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
eric = Vampire()
adam = Vampire()
richard = Defender()
ogre = Warrior()

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
fight(eric, richard) == False
fight(ogre, adam) == True

my_army = Army()
my_army.add_units(Defender, 2)
my_army.add_units(Vampire, 2)
my_army.add_units(Warrior, 1)

enemy_army = Army()
enemy_army.add_units(Warrior, 2)
enemy_army.add_units(Defender, 2)
enemy_army.add_units(Vampire, 3)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Defender, 4)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 2)

battle = Battle()

battle.fight(my_army, enemy_army) == False
battle.fight(army_3, army_4) == True
```

**Входные данные**: воины и армии.

**Выходные данные:** результат сражения (True или False).

**Как это используется:** Для разработки компьютерных игр.

**Предусловие:** 4 типа солдат

# Solution

```python
class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50
        self.defense = 0
        self.is_alive = True
        self.vampirism = 0

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

class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.vampirism = 50
        self.health = 40
        self.attack = 4

    def __str__(self):
        return 'Vampire'

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
    print('=' * 20)
    flag = 'First'
    print('================')
    print(unit_1, 'HP:', unit_1.health, 'ATK:', unit_1.attack, 'VAMP:',unit_1.vampirism, 'DEF:', unit_1.defense)
    print(unit_2, 'HP:', unit_2.health, 'ATK:', unit_2.attack, 'VAMP:',unit_2.vampirism, 'DEF:', unit_2.defense)
    print('================')
    while True:
        if flag == 'First':
            damage = unit_2.defense - unit_1.attack
            if damage < 0:
                unit_2.health = unit_2.health + damage
                unit_1.health -= damage * unit_1.vampirism / 100
            print(unit_1, flag, unit_1.health, 'vs', unit_2.health, unit_2, '|  Damage', damage, '| Healing', -damage * unit_1.vampirism / 100)
            flag = 'Second'

        else:
            damage = unit_1.defense - unit_2.attack
            if damage < 0:
                unit_1.health = unit_1.health + damage
                unit_2.health -= damage * unit_2.vampirism / 100
            print(unit_1, flag, unit_1.health, 'vs', unit_2.health, unit_2, '|  Damage', damage, '| Healing', -damage * unit_2.vampirism / 100)
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
        print('=== fight army ===')
        while True:

            flag = 'First'

            while True:

                if flag == 'First':
                    damage = unit_2[0].defense - unit_1[0].attack
                    if damage < 0:
                        unit_2[0].health = unit_2[0].health + damage
                        unit_1[0].health -= damage * unit_1[0].vampirism / 100
                    print(unit_1[0], flag, unit_1[0].health, 'vs', unit_2[0].health, unit_2[0], '|  Damage', damage, '| Healing',
                          -damage * unit_1[0].vampirism / 100)
                    flag = 'Second'

                else:
                    damage = unit_1[0].defense - unit_2[0].attack
                    if damage < 0:
                        unit_1[0].health = unit_1[0].health + damage
                        unit_2[0].health -= damage * unit_2[0].vampirism / 100
                    print(unit_1[0], flag, unit_1[0].health, 'vs', unit_2[0].health, unit_2[0], '|  Damage', damage, '| Healing',
                          -damage * unit_2[0].vampirism / 100)
                    flag = 'First'

                if unit_1[0].health <= 0:

                    unit_1.pop(0)
                    try:
                        print('================')
                        print(unit_1[0], 'HP:', unit_1[0].health, 'ATK:', unit_1[0].attack, 'VAMP:', unit_1[0].vampirism,
                              'DEF:',
                              unit_1[0].defense)
                        print(unit_2[0], 'HP:', unit_2[0].health, 'ATK:', unit_2[0].attack, 'VAMP:', unit_2[0].vampirism,
                              'DEF:',
                              unit_2[0].defense)
                        print('================')
                    except:
                        pass
                if unit_2[0].health <= 0:
                    unit_2.pop(0)
                    flag = 'First'
                    try:
                        print('================')
                        print(unit_1[0], 'HP:', unit_1[0].health, 'ATK:', unit_1[0].attack, 'VAMP:', unit_1[0].vampirism,
                              'DEF:',
                              unit_1[0].defense)
                        print(unit_2[0], 'HP:', unit_2[0].health, 'ATK:', unit_2[0].attack, 'VAMP:', unit_2[0].vampirism,
                              'DEF:',
                              unit_2[0].defense)
                        print('================')
                    except:
                        pass
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
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")

    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Defender, 5)
    army_1.add_units(Vampire, 6)
    army_1.add_units(Warrior, 7)
    army_2.add_units(Warrior, 6)
    army_2.add_units(Defender, 6)
    army_2.add_units(Vampire, 6)
    battle = Battle()
    assert battle.fight(army_1, army_2) == False
```