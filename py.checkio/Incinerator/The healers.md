# The healers

Битва продолжается и каждая армия теряет множество хороших воинов. Давайте постараемся исправить это и добавим новый тип
юнитов - Healer. Healer не будет сражаться лично (его атака равна 0 и он не сможет нанести урон), но его задача не менее
полезна - каждый раз, когда союзный солдат бьет врага, Healer, стоящий позади союзника лечит его на +2 единицы здоровья
с помощью метода heal() . При этом исцеление не может поднять здоровье выше максимального уровня. То есть, если Healer
лечит Warrior, у которого 49 единиц здоровья, то после лечения Warrior будет иметь 50 единиц здоровья, так как это - его
максимальный уровень.

Базовые параметры класса Healer:

health = 60

attack = 0

![](https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/2f54230f16174967998f764bb54b9b89/healing_process.png)

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

battle = Battle()

battle.fight(my_army, enemy_army) == False
battle.fight(army_3, army_4) == True
```

Входные данные: воины и армии.

Выходные данные: результат сражения (True или False).

Как это используется: Для разработки компьютерных игр.

Предусловие: 6 типов солдат

# Solution

```python
class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50
        self.defense = 0
        self.is_alive = True
        self.vampirism = 0
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

    def heal(self, warrior):
        warrior.health += 2


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
    print(unit_1, 'HP:', unit_1.health, 'ATK:', unit_1.attack, 'VAMP:', unit_1.vampirism, 'DEF:', unit_1.defense)
    print(unit_2, 'HP:', unit_2.health, 'ATK:', unit_2.attack, 'VAMP:', unit_2.vampirism, 'DEF:', unit_2.defense)
    print('================')
    while unit_1.health > 0 and unit_2.health > 0:
        if flag == 'First':
            damage = unit_2.defense - unit_1.attack
            if damage < 0:
                unit_2.health = unit_2.health + damage
                unit_1.health -= damage * unit_1.vampirism / 100
            print(unit_1, flag, unit_1.health, 'vs', unit_2.health, unit_2, '|  Damage', damage, '| Healing',
                  -damage * unit_1.vampirism / 100)
            flag = 'Second'

        else:
            damage = unit_1.defense - unit_2.attack
            if damage < 0:
                unit_1.health = unit_1.health + damage
                unit_2.health -= damage * unit_2.vampirism / 100
            print(unit_1, flag, unit_1.health, 'vs', unit_2.health, unit_2, '|  Damage', damage, '| Healing',
                  -damage * unit_2.vampirism / 100)
            flag = 'First'

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

                        # Heal
                        if len(unit_1.all()) > 1 and unit_1[1].do_heal:
                            unit_1[1].heal(unit_1[0])

                    print(unit_1[0], flag, unit_1[0].health, 'vs', unit_2[0].health, unit_2[0], '|  Damage', damage,
                          '| Healing',
                          -damage * unit_1[0].vampirism / 100)

                    # Lancer attack
                    if unit_1[0].range_attack and len(unit_2.all()) > 1:
                        damage_to_behind = (unit_2[1].defense - unit_1[0].attack) * 0.5
                        if damage_to_behind < 0:
                            unit_2[1].health = unit_2[1].health + damage_to_behind
                            unit_1[0].health -= damage_to_behind * unit_1[0].vampirism / 100
                        print(unit_1[0], flag, unit_1[0].health, 'vs', unit_2[1].health, unit_2[1], '|  Damage',
                              damage_to_behind,
                              '| Healing',
                              -damage_to_behind * unit_1[0].vampirism / 100)

                    flag = 'Second'

                else:
                    damage = unit_1[0].defense - unit_2[0].attack
                    if damage < 0:
                        unit_1[0].health = unit_1[0].health + damage
                        unit_2[0].health -= damage * unit_2[0].vampirism / 100
                        # Heal
                        if len(unit_2.all()) > 1 and unit_2[1].do_heal:
                            unit_2[1].heal(unit_2[0])

                    print(unit_1[0], flag, unit_1[0].health, 'vs', unit_2[0].health, unit_2[0], '|  Damage', damage,
                          '| Healing',
                          -damage * unit_2[0].vampirism / 100)

                    # Lancer attack
                    if unit_2[0].range_attack and len(unit_1.all()) > 1:
                        damage_to_behind = (unit_1[1].defense - unit_2[0].attack) * 0.5
                        if damage_to_behind < 0:
                            unit_1[1].health = unit_1[1].health + damage_to_behind
                            unit_2[0].health -= damage_to_behind * unit_2[0].vampirism / 100
                        print(unit_2[0], flag, unit_2[0].health, 'vs', unit_1[1].health, unit_1[1], '|  Damage',
                              damage_to_behind,
                              '| Healing',
                              -damage_to_behind * unit_2[0].vampirism / 100)
                    flag = 'First'

                if unit_1[0].health <= 0:

                    unit_1.pop(0)
                    try:
                        print('================')
                        print(unit_1[0], 'HP:', unit_1[0].health, 'ATK:', unit_1[0].attack, 'VAMP:',
                              unit_1[0].vampirism,
                              'DEF:',
                              unit_1[0].defense)
                        print(unit_2[0], 'HP:', unit_2[0].health, 'ATK:', unit_2[0].attack, 'VAMP:',
                              unit_2[0].vampirism,
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
                        print(unit_1[0], 'HP:', unit_1[0].health, 'ATK:', unit_1[0].attack, 'VAMP:',
                              unit_1[0].vampirism,
                              'DEF:',
                              unit_1[0].defense)
                        print(unit_2[0], 'HP:', unit_2[0].health, 'ATK:', unit_2[0].attack, 'VAMP:',
                              unit_2[0].vampirism,
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

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
```