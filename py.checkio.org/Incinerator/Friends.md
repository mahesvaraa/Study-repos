В задании "Как найти друзей" ("How to find friends") , было бы удобно работать, используя специальную структуру данных.
В этом задании мы разработаем структуру данных, которую будем применять для хранения и обработки социальной сети.

Класс "Friends" должен содержать данные о людях (их имена) и о связях между ними. Имена представлены в виде текстовых
строк, чувствительных к регистру. Связи не имеют направлений, то есть, если существует связь "sofia" с "nikola", это
справедливо и в обратную сторону.

**class Friends (connections)**

Возвращает новый объект, экземпляр класса Friends. Параметр "connections" имеет тип "итерируемый объект", содержащий
множества (set) с двумя элементами в каждом. Каждая связь содержит два имени в виде текстовых строк. Связи могут
повторяться в параметре инициализации, но в объекте хранятся только уникальные пары. Каждая связь имеет только два
состояния - присутствует или не присутствует.

```python
>> > Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"})
             >> > Friends([{"1", "2"}, {"3", "1"}])
```

Добавляет связь в объект. Параметр "connection" является множеством (set) из двух имен (строк). Возвращает True, если
заданная связь новая и не присутствует в объекте. Возвращает False, если заданная связь уже существует в объекте.

```python
>> > f = Friends([{"1", "2"}, {"3", "1"}])
>> > f.add({"1", "3"})
False
>> > f.add({"4", "5"})
True
```

**remove (connection)**

Удаляет связь из объекта. Параметр "connection" является множеством (set) из двух имен (строк). Возвращает True, если
заданная связь существует в объекте. Возвращает False, если заданная связь не присутствует в объекте.

```python
>> > f = Friends([{"1", "2"}, {"3", "1"}])
>> > f.remove({"1", "3"})
True
>> > f.remove({"4", "5"})
False
```

**names ()**

Возвращает множество (set) имён. Множество содержит имена, которые имеют хотя бы одну связь.

```python
>> > f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"})
                 >> > f.names()
{"a", "b", "c", "d"}
>> > f.remove({"d", "c"})
True
>> > f.names()
{"a", "b", "c"}
```

**connected (name)**

Возвращает множество (set) имён, которые связаны с именем, заданным параметром "name" . Если "name" не присутствует в
объекте, возвращается пустое множество (set).

```python
>> > f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"})
                 >> > f.connected("a")
{"b", "c"}
>> > f.connected("d")
set()
>> > f.remove({"c", "a"})
True
>> > f.connected("c")
set()
```

В этом задании все входные данные корректны, и выполнять их проверку не обязательно.

**Входные данные:** Операторы и выражения с классом Friends.

**Выходные данные:** Поведение объекта, как описано выше.

**Как это используется:** Здесь вы реализуете класс с изменяемым состоянием. Это не простая структура данных с
несколькими методами, а реализация более сложного объекта.

**Предусловие**: Все данные корректны.

# Solution

```python
class Friends:

    def __init__(self, iter_object):
        self.friend_list = list(iter_object)

    def add(self, set_object):
        if set_object not in self.friend_list:
            self.friend_list.append(set_object)
            return True
        else:
            return False

    def remove(self, set_object):

        if set_object in self.friend_list:
            self.friend_list.remove(set_object)
            return True
        else:
            return False

    def names(self):
        result = set()
        for friend_set in self.friend_list:
            for i in friend_set:
                result.add(i)
        return result

    def connected(self, friend):
        result = set()
        res = [i - set(friend) for i in self.friend_list if friend in i]
        for i in res:
            result = result.union(i)
        return result




if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    f1 = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    f2 = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))

    f = Friends([{"1", "2"}, {"3", "1"}])
    assert f.add({"1", "3"}) is False
    assert f.add({"4", "5"}) is True

    f3 = Friends([{"1", "2"}, {"3", "1"}])
    assert f3.remove({"1", "3"}) is True
    assert f3.remove({"4", "5"}) is False

    f4 = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"}))
    assert f4.names() == {"a", "b", "c", "d"}
    assert f4.remove({"d", "c"}) is True
    assert f4.names() == {"a", "b", "c"}

    f5 = f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
    assert f.connected("a") == {"b", "c"}
    assert f.connected("d") == set()
    assert f.remove({"c", "a"}) is True
    assert f.connected("c") == {'b'}

```