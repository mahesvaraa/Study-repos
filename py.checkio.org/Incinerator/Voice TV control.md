Технологии развиваются стремительно - всего полвека назад обычный черно-белый телевизор был роскошью, затем - телевизор
с пультом дистанционного управления. И вот пришло время, когда уже и этого кажется мало. Ну что же, давайте сделаем
технологический шаг вперед и реализуем голосовое управление телевизора (для начала - прототип написанный на Python).
Команды, которые будут использоваться:

**first_channel()** - переключается на первый канал из списка.
**last_channel()** - переключается на последний канал из списка.
**turn_channel(N)** - переключается на канал номер N. Обратите внимание, что нумерация каналов начинается с 1, а не с 0.
**next_channel()** - переключается на следующий канал. Если текущий канал - последний, то эта команда переключает на
первый канал.
**previous_channel()** - переключается на предыдущий канал. Если текущий канал - первый, то эта команда переключает на
последний канал.
**current_channel()** - возвращает название текущего канала.
**is_exist(N/'name')** - принимает 1 аргумент - число N или строку 'name' и возвращает "Yes", если канал с номером N или
названием 'name' существует в списке и "No" в ином случае.

По умолчанию до начала работы всех команд включен канал №1. Ваша задача - создать класс VoiceCommand и методы, описанные
ранее. В этой миссии вам может помочь такой шаблон проектирования, как Iterator .

# Примеры

```python
CHANNELS = ["BBC", "Discovery", "TV1000"]

controller = VoiceCommand(CHANNELS)

controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
controller.is_exist(4) == "No"
controller.is_exist("BBC") == "Yes"
```

**Входные данные:** голосовые команды.

**Выходные данные:** название канала или проверка существования его в списке.

**Как это используется:** Для работы с итерируемыми объектами.

**Предусловие**: Все команды и названия каналов корректны.

# Solution

```python
class VoiceCommand:
    def __init__(self, arr: list, cursor=0):
        self._collection = arr
        self._cursor = cursor

    def current_channel(self):
        if self._cursor < len(self._collection):
            return self._collection[self._cursor]

    def first_channel(self):
        self._cursor = 0
        return self._collection[0]

    def last_channel(self):
        self._cursor = len(self._collection) - 1
        return self._collection[-1]

    def has_next(self):
        return len(self._collection) >= self._cursor + 1

    def next_channel(self):
        if len(self._collection) > self._cursor + 1:
            self._cursor += 1
            return self._collection[self._cursor]
        else:
            self._cursor = 0
            return self._collection[0]

    def turn_channel(self, cursor):
        cursor -= 1
        if cursor < len(self._collection):
            self._cursor = cursor
            return self._collection[cursor]

    def previous_channel(self):
        self._cursor -= 1
        return self._collection[self._cursor]

    def is_exist(self, arg):
        if isinstance(arg, str):
            return ['No', 'Yes'][arg in self._collection]
        else:
            return ['No', 'Yes'][len(self._collection) > arg]

    def name_channel(self):
        print(self._collection[self._cursor], self._cursor)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")

```