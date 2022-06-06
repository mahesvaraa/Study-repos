# The weapons

В этой миссии вам необходимо будет добавить класс Weapon(health, attack, defense, vampirism, heal_power) чтобы создавать
оружие с заданными характеристиками и экипировать им солдат. При создании объекта оружия, ему будут переданы значения,
которые показывают, как изменятся соответствующие параметры воина, использующего данное оружие. Обратите внимание, что
если у солдата нет определенной характеристики (например, defense или vampirism), которая есть на оружии, то эта
характеристика не добавляется ему.

**Перечень** **характеристик**:

**health** - добавляет к максимальному и текущему запасу здоровья солдата указанное число

**attack** - добавляет к атаке солдата указанное число

**defense** - добавляет к защите солдата указанное число

**vampirism** - увеличивает вампиризм на указанное количество процентов

**heal_power** - увеличивает количество здоровья, которое восстанавливает лекарь при каждом исцелении на указанное число

Все указанные параметры оружия могут иметь как положительное, так и отрицательное значение. Таким образом, при
добавлении отрицательного модификатора, соответствующая характеристика становится меньше, но не может опуститься ниже 0.

Давайте рассмотрим пример вампира (базовые характеристики: health = 40, attack = 4, vampirism = 50%), надевшего
следующее оружие - Weapon(20, 5, 2, -60, -1). Так как у него есть health и attack, они будут изменены - health
увеличится до 60 (40 + 20), attack станет 9 (4 + 5). Параметров defense и heal_power у вампира нет, поэтому
соответствующие модификаторы на него никак не подействует. Также сработает изменение vampirism -60%, уменьшающее
стандартный параметр 50% до -10%. Но так как согласно условиям ни один параметр не может быть меньше 0, vampirism просто
будет равен 0% и перестанет работать.

Помимо оружия с задаваемыми характеристиками, вам также необходимо будет создать несколько классов-наследников Weapon с
заданными и неизменяемыми характеристиками. Вот их список:

**Sword** - health +5, attack +2

**Shield** - health +20, attack -1, defense +2

**GreatAxe** - health -15, attack +5, defense -2, vampirism +10%

**Katana** - health -20, attack +6, defense -5, vampirism +50%

**MagicWand** - health +30, attack +3, heal_power +3

И наконец, чтобы суметь надеть оружие, вам необходимо добавить в существующие классы солдат метод equip_weapon(
weapon_name).

Для того, чтобы экипировать солдат, входящих в состав армии, вам необходимо хранить их в списке units и обращаться по
индексу. Например:
my_army.units[0].equip_weapon(Sword()) - снаряжает первого воина мечом.

**Примечания**:

В процессе исцеления от лекаря или лечения вампиризмом, запас здоровья не может стать больше, чем максимальный запас (с
учетом всех модификаторов оружия).

Если лечение от вампиризма оказывается не целым числом, (например: 3.6, 1.1, 2.945), округляйте вниз в любом случае.
Таким образом, 3.6 = 3, 1.1 = 1, 2.945 = 2. Любой солдат может надеть любое количество оружия и получить все бонусы от
них, но если он наденет слишком много вещей с отрицательным модификатором health и опустит своё здоровье до 0, то умрет.

# Пример

```python
ogre = Warrior()
lancelot = Knight()
richard = Defender()
eric = Vampire()
freelancer = Lancer()
priest = Healer()

sword = Sword()
shield = Shield()
axe = GreatAxe()
katana = Katana()
wand = MagicWand()
super_weapon = Weapon(50, 10, 5, 150, 8)

ogre.equip_weapon(sword)
ogre.equip_weapon(shield)
ogre.equip_weapon(super_weapon)
lancelot.equip_weapon(super_weapon)
richard.equip_weapon(shield)
eric.equip_weapon(super_weapon)
freelancer.equip_weapon(axe)
freelancer.equip_weapon(katana)
priest.equip_weapon(wand)
priest.equip_weapon(shield)

ogre.health == 125
lancelot.attack == 17
richard.defense == 4
eric.vampirism == 200
freelancer.health == 15
priest.heal_power == 5

fight(ogre, eric) == False
fight(priest, richard) == False
fight(lancelot, freelancer) == True

my_army = Army()
my_army.add_units(Knight, 1)
my_army.add_units(Lancer, 1)

enemy_army = Army()
enemy_army.add_units(Vampire, 1)
enemy_army.add_units(Healer, 1)

my_army.units[0].equip_weapon(axe)
my_army.units[1].equip_weapon(super_weapon)

enemy_army.units[0].equip_weapon(katana)
enemy_army.units[1].equip_weapon(wand)

battle = Battle()

battle.fight(my_army, enemy_army) == True
```

**Входные данные:** воины, армии и оружие.

**Выходные данные:** результат сражения (True или False).

**Как это используется:** Для разработки компьютерных игр.

**Предусловие:** 5 типов солдат, 2 типа сражений

# Solution

```python
class Warrior:
    def __init__(self, attack=5, health=50, defense=0, vampirism=0, heal_power=0):
        self.attack = 5
        self.health = 50
        self.defense = 0
        self.vampirism = 0
        self.heal_power = 0

        self.is_alive = True
        self.range_attack = False
        self.do_heal = False
        self.has_vampirism = False
        self.has_defense = False

    def __str__(self):
        return f'Warrior {self.attack} {self.health} {self.defense} {self.vampirism} {self.heal_power}'

    def equip_weapon(self, weapon_name):
        self.health += weapon_name.health
        if self.health <= 0:
            self.health = 0
            self.is_alive = 0
        self.attack += weapon_name.attack
        if self.attack <= 0:
            self.attack = 0
        if self.has_defense:
            self.defense += weapon_name.defense
            if self.defense <= 0:
                self.defense = 0
        if self.has_vampirism:
            self.vampirism += weapon_name.vampirism
            if self.vampirism <= 0:
                self.vampirism = 0
        if self.do_heal:
            self.heal_power += weapon_name.heal_power
            if self.heal_power <= 0:
                self.heal_power = 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7

    def __str__(self):
        return f'Knight {self.attack} {self.health} {self.defense} {self.vampirism} {self.heal_power}'


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.defense = 2
        self.attack = 3
        self.has_defense = True

    def __str__(self):
        return f'Defender {self.attack} {self.health} {self.defense} {self.vampirism} {self.heal_power}'


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.vampirism = 50
        self.health = 40
        self.attack = 4
        self.has_vampirism = True

    def __str__(self):
        return f'Vampire {self.attack} {self.health} {self.defense} {self.vampirism} {self.heal_power}'


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
        self.range_attack = True

    def __str__(self):
        return f'Lancer {self.attack} {self.health} {self.defense} {self.vampirism} {self.heal_power}'


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 0
        self.health = 60
        self.heal_power = 2
        self.do_heal = True

    def heal(self, unit):
        unit.health += self.heal_power

    def __str__(self):
        return f'Healer {self.attack} {self.health} {self.defense} {self.vampirism} {self.heal_power}'


class Weapon:
    def __init__(self, health=0, attack=0, defense=0, vampirism=0, heal_power=0):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power


class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.health = 5
        self.attack = 2


class Shield(Weapon):
    def __init__(self):
        super().__init__()
        self.health = 20
        self.attack = -1
        self.defense = 2


class GreatAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.health = -15
        self.attack = 5
        self.defense = -2
        self.vampirism = 10


class Katana(Weapon):
    def __init__(self):
        super().__init__()
        self.health = -20
        self.attack = 6
        self.defense = -5
        self.vampirism = 50


class MagicWand(Weapon):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.attack = 3
        self.heal_power = 3


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
        self.units = self

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
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
	ogre = Warrior()
	lancelot = Knight()
	richard = Defender()
	eric = Vampire()
	freelancer = Lancer()
	priest = Healer()

	sword = Sword()
	shield = Shield()
	axe = GreatAxe()
	katana = Katana()
	wand = MagicWand()
	super_weapon = Weapon(50, 10, 5, 150, 8)

	ogre.equip_weapon(sword)
	ogre.equip_weapon(shield)
	ogre.equip_weapon(super_weapon)
	lancelot.equip_weapon(super_weapon)
	richard.equip_weapon(shield)
	eric.equip_weapon(super_weapon)
	freelancer.equip_weapon(axe)
	freelancer.equip_weapon(katana)
	priest.equip_weapon(wand)
	priest.equip_weapon(shield)

	ogre.health == 125
	lancelot.attack == 17
	richard.defense == 4
	eric.vampirism == 200
	freelancer.health == 15
	priest.heal_power == 5

	fight(ogre, eric) == False
	fight(priest, richard) == False
	fight(lancelot, freelancer) == True

	my_army = Army()
	my_army.add_units(Knight, 1)
	my_army.add_units(Lancer, 1)

	enemy_army = Army()
	enemy_army.add_units(Vampire, 1)
	enemy_army.add_units(Healer, 1)

	my_army.units[0].equip_weapon(axe)
	my_army.units[1].equip_weapon(super_weapon)

	enemy_army.units[0].equip_weapon(katana)
	enemy_army.units[1].equip_weapon(wand)

	battle = Battle()

	battle.fight(my_army, enemy_army) == False
    print("Coding complete? Let's try tests!")
```