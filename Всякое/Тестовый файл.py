VOWELS = "aeiou"


class Chat:
    def __init__(self):
        self.chat_history = []

    def connect_human(self, user):
        self.chat_history[user] = {}

    def connect_robot(self, user):
        self.chat_history[user] = {}


class Human:
    def __init__(self, name):
        self.name = name


class Robot:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

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

    print("Coding complete? Let's try tests!")
