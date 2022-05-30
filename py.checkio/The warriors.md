# Воины

Наверняка многие из вас имеют опыт прохождения компьютерных игр. Возникало ли у вас в процессе игры желание изменить
что-нибудь и сделать так, чтобы персонажи или игровой мир больше соответствовали вашему представлению о хорошей игре?
Скорее всего да. В этой миссии (и в нескольких последующих, связанных с ней) вам предоставится возможность «посидеть в
кресле разработчика» и создать логику простой игры о сражениях. Давайте начнем с малого — сражения 1×1. В этой миссии
вам необходимо будет создать класс **Warrior** , у экземпляров которого будет 2 параметра — **health** (здоровье, равное
50) и
**attack** (атака, равная 5), а также свойство **is_alive** , которое может быть **True** (если здоровье воина > 0)
или **False** (в ином случае). Кроме этого вам необходимо создать класс для второго типа солдат — **Knight** , который
будет наследником
**Warrior** , но с увеличенной атакой — 7. Также вам необходимо будет создать функцию **fight**() , которая будет
проводить дуэли между 2 воинами и определять сильнейшего из них. Бои происходят по следующему принципу:

* каждый ход первый воин наносит второму урон в размере своей атаки, вследствие чего здоровье второго воина уменьшается
* аналогично и второй воин, если он еще жив, поступает по отношению к первому.

Битва заканчивается смертью одного из них. Если первый воин все еще жив (а второй, соответственно, уже нет), функция
возвращает True , или в ином случае False .

![](https://d17mnqrx9pmt3e.cloudfront.net/media/missions/media/4e0dd625813446a595c6f45e5033d355/warrior.png)

# Пример

```python
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
```

**Входные данные:** воины.

**Выходные данные:** результат поединка (True или False).

**Как это используется:** Для разработки компьютерных игр.

**Предусловие:** 2 типа солдат

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

```