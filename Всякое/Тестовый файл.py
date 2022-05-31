class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50
        self.defense = 0
        self.is_alive = True
        self.vampirism = 0
        self.range_attack = False

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
                    print(unit_1[0], flag, unit_1[0].health, 'vs', unit_2[0].health, unit_2[0], '|  Damage', damage,
                          '| Healing',
                          -damage * unit_1[0].vampirism / 100)
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
                    print(unit_1[0], flag, unit_1[0].health, 'vs', unit_2[0].health, unit_2[0], '|  Damage', damage,
                          '| Healing',
                          -damage * unit_2[0].vampirism / 100)
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
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Lancer, 5)
    army_1.add_units(Vampire, 3)
    army_1.add_units(Warrior, 4)
    army_1.add_units(Defender, 2)
    army_2.add_units(Warrior, 4)
    army_2.add_units(Defender, 4)
    army_2.add_units(Vampire, 6)
    army_2.add_units(Lancer, 5)
    battle = Battle()
    print(battle.fight(army_1, army_2))
