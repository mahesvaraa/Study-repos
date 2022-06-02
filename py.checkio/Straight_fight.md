# Straight fight

В этой миссии не будет новых типов солдат, зато появится новая тактика - **straight_fight(army_1, army_2)**. Это должен
быть метод класса Battle и он должен работать следующим образом:
сперва устраиваются дуэли между каждой парой воинов из первой и второй армии (первый с первым, второй со вторым и так
далее). Затем из каждой армии убираются все погибшие воины и процесс повторяется до тех пор, пока в одной из армий не
останется ни одного воина. В начальном составе армий может быть не одинаковое количество воинов. Если для воинов не
находится соперника из вражеской армии - считается, что они автоматически выигрывают дуэль (например, 9-й и 10-й солдаты
из первой армии, если во второй всего 8 солдат).

![](https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/a8b34395d090457ea078c094eb3353e1/straight_fight.png)

# Пример

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
freelancer = Lancer()
vampire = Vampire()
priest = Healer()

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
fight(freelancer, vampire) == True
freelancer.is_alive == True
freelancer.health == 14
priest.heal(freelancer)
freelancer.health == 16

my_army = Army()
my_army.add_units(Defender, 2)
my_army.add_units(Healer, 1)
my_army.add_units(Vampire, 2)
my_army.add_units(Lancer, 2)
my_army.add_units(Healer, 1)
my_army.add_units(Warrior, 1)

enemy_army = Army()
enemy_army.add_units(Warrior, 2)
enemy_army.add_units(Lancer, 4)
enemy_army.add_units(Healer, 1)
enemy_army.add_units(Defender, 2)
enemy_army.add_units(Vampire, 3)
enemy_army.add_units(Healer, 1)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Lancer, 1)
army_3.add_units(Healer, 1)
army_3.add_units(Defender, 2)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 1)
army_4.add_units(Healer, 1)
army_4.add_units(Lancer, 2)

army_5 = Army()
army_5.add_units(Warrior, 10)

army_6 = Army()
army_6.add_units(Warrior, 6)
army_6.add_units(Lancer, 5)

battle = Battle()

battle.fight(my_army, enemy_army) == False
battle.fight(army_3, army_4) == True
battle.straight_fight(army_5, army_6) == False
```

**Входные данные:** воины и армии.

**Выходные данные:** результат сражения (True или False).

**Как это используется:** Для разработки компьютерных игр.

**Предусловие:** 5 типов солдат, 2 типа сражений

# Solution

```python
class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50
        self.defense = 0
        self.vampirism = 0

        self.is_alive = True
        self.range_attack = False
        self.do_heal = False

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


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
        self.range_attack = True

    def __str__(self):
        return 'Lancer'


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 0
        self.health = 60
        self.do_heal = True

    def heal(self, unit):
        unit.health += 2

    def __str__(self):
        return 'Healer'


def fight(unit_1, unit_2):
    flag = 'First'
    while unit_1.is_alive and unit_2.is_alive:
        if flag == 'First':
            damage = unit_2.defense - unit_1.attack
            if damage < 0:
                unit_2.health = unit_2.health + damage
                unit_1.health -= damage * unit_1.vampirism / 100
            flag = 'Second'

        else:
            damage = unit_1.defense - unit_2.attack
            if damage < 0:
                unit_1.health = unit_1.health + damage
                unit_2.health -= damage * unit_2.vampirism / 100
            flag = 'First'

        if unit_1.health <= 0:
            unit_1.is_alive = False
        if unit_2.health <= 0:
            unit_2.is_alive = False

    return unit_1.is_alive


class Army(list):

    def __init__(self):
        super().__init__()
        self.army = []

    def add_units(self, Warrior, count):
        for i in range(count):
            self.append(Warrior())


class Battle():

    def fight(self, unit_1, unit_2):
        while len(unit_1) and len(unit_2):
            flag = 'First'
            while unit_1 and unit_2:
                if flag == 'First':
                    damage = unit_2[0].defense - unit_1[0].attack
                    if damage < 0:
                        unit_2[0].health = unit_2[0].health + damage
                        unit_1[0].health -= damage * unit_1[0].vampirism / 100

                        # Heal
                        if len(unit_1) > 1 and unit_1[1].do_heal:
                            unit_1[1].heal(unit_1[0])

                    # Lancer attack
                    if unit_1[0].range_attack and len(unit_2) > 1:
                        damage_to_behind = (unit_2[1].defense - unit_1[0].attack) * 0.5
                        if damage_to_behind < 0:
                            unit_2[1].health = unit_2[1].health + damage_to_behind
                            unit_1[0].health -= damage_to_behind * unit_1[0].vampirism / 100

                    flag = 'Second'

                else:
                    damage = unit_1[0].defense - unit_2[0].attack
                    if damage < 0:
                        unit_1[0].health = unit_1[0].health + damage
                        unit_2[0].health -= damage * unit_2[0].vampirism / 100
                        # Heal
                        if len(unit_2) > 1 and unit_2[1].do_heal:
                            unit_2[1].heal(unit_2[0])

                    # Lancer attack
                    if unit_2[0].range_attack and len(unit_1) > 1:
                        damage_to_behind = (unit_1[1].defense - unit_2[0].attack) * 0.5
                        if damage_to_behind < 0:
                            unit_1[1].health = unit_1[1].health + damage_to_behind
                            unit_2[0].health -= damage_to_behind * unit_2[0].vampirism / 100

                    flag = 'First'

                if unit_1[0].health <= 0:
                    unit_1.pop(0)

                if unit_2[0].health <= 0:
                    unit_2.pop(0)
                    flag = 'First'

            return bool(unit_1)

    def straight_fight(self, unit_1, unit_2):
        while unit_1 and unit_2:
            biggest_army, mini_army = sorted([unit_1, unit_2], key=len, reverse=True)
            for i in range(len(mini_army)):
                fight(unit_1[i], unit_2[i])
            unit_1 = list(filter(lambda x: x.is_alive, unit_1))
            unit_2 = list(filter(lambda x: x.is_alive, unit_2))
        return bool(unit_1)


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
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

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
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    assert freelancer.health == 14
    priest.heal(freelancer)
    assert freelancer.health == 16

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    army_5 = Army()
    army_5.add_units(Warrior, 10)

    army_6 = Army()
    army_6.add_units(Warrior, 6)
    army_6.add_units(Lancer, 5)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    assert battle.straight_fight(army_5, army_6) == False
    print("Coding complete? Let's try tests!")

```