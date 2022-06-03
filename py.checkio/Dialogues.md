# Dialogues

Современный мир наполнен средствами связи - социальные сети, мессенджеры, телефонные звонки и СМС. И всё же, при
огромном богатстве выбора, порой в любом из средств обнаруживается изъян и в такие моменты появляется мысль: "Пора
делать собственное средство связи. Уж оно-то точно будет лишено всех недостатков".

В этой миссии вам представится такая возможность.

Ваша задача - реализовать способ связи между человеком Human(name) и роботом Robot(serial_number) с последующим выводом
их переписки. Для этого вам необходимо создать класс для каждого из двоих собеседников и метод send() для отправки
сообщений в чат, а также класс Chat как средство связи. Chat должен обладать следующими методами:

connect_human() - подключает к чату человека.

connect_robot() - подключает к чату робота.

show_human_dialogue() - отображает диалог так, как его видит человек - обычным текстом.

show_robot_dialogue() - отображает диалог так, как его видит робот - в виде набора нулей и единиц. Для простоты будем
считать, что любая гласная буква ("aeiouAEIOU") в текстовом сообщении должна быть заменена на "0", а все остальные
символы (согласные буквы, пробелы и специальные знаки, как ",", "!" и т.п.) на "1".

Диалог для человека должен отображаться как многострочная строка вида:

(human name) said: текст сообщения

(robot serial number) said: текст сообщения

Для робота:

(human name) said: 11100100011

(robot serial number) said: 100011100101

В этой миссии вам может помочь такой шаблон проектирования, как Mediator .

# Примеры

```python
chat = Chat()
karl = Human("Karl")
bot = Robot("R2D2")
chat.connect_human(karl)
chat.connect_robot(bot)
karl.send("Hi! What's new?")
bot.send("Hello, human. Could we speak later about it?")
chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""
```

**Входные данные:** собеседники и текст сообщений.

**Выходные данные:** диалог (многострочная строка).

**Как это используется:** Для организации канала общения и передачи информации.

**Предусловие**: 2 собеседника.

# Solution

```python
VOWELS = "aeiou"


class Chat(object):
    """Mediator class."""

    def __init__(self):
        self.chat_history = []

    def send(self, user, message):
        message_to_robot = message
        for char in message_to_robot:
            if char.lower() in VOWELS:
                message_to_robot = message_to_robot.replace(char, '0')
            else:
                message_to_robot = message_to_robot.replace(char, '1')
        self.chat_history.append((user, message + '\n    ', message_to_robot + '\n    '))

    def show_human_dialogue(self):
        result = ''
        for i in self.chat_history:
            result += f"""{i[0]} said: {i[1]}"""
        return result.rstrip()

    def show_robot_dialogue(self):
        result = ''
        for i in self.chat_history:
            result += f"""{i[0]} said: {i[2]}"""
        return result.rstrip()

    def connect_human(self, Cls):
        Cls.chat = self

    def connect_robot(self, Cls):
        Cls.chat = self


class User(object):
    '''A class whose instances want to interact with each other.'''

    def __init__(self, name):
        self.name = name
        self.chat = None

    def send(self, message):
        self.chat.send(self, message)

    def __str__(self):
        return self.name


class Human(User):
    pass


class Robot(User):
    pass


"""main method"""

if __name__ == "__main__":
    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
    R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
    R2D2 said: 10110111010111100111101110011101011010011011"""

```