class Warrior:
    def __init__(self):
        self.attack = 5
        self.health = 50
        self.is_alive = True


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack += 2


def fight(unit_1, unit_2):
    flag = 'First'
    while True:
        if flag == 'First':
            unit_2.health -= unit_1.attack
            flag = 'Second'
        else:
            unit_1.health -= unit_2.attack
            flag = 'First'
        print(flag, unit_1.health, unit_2.health)
        if unit_1.health <= 0 or unit_2.health <= 0:
            break
    if unit_1.health <= 0:
        unit_1.is_alive = False
    if unit_2.health <= 0:
        unit_2.is_alive = False
    return unit_1.is_alive
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

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

    print("Coding complete? Let's try tests!")
