Вы с друзьями собираетесь каждую неделю, чтобы вместе провести время. Обычно это или посиделки в баре в пятницу вечером,
или выезд на природу за город в субботу или коллективные настольные игры в воскресенье. Чтобы каждый раз не приглашать
каждого человека по отдельности и случайно никого не забыть, вы решили написать программу, которая бы автоматически
рассылала вашим друзьям сообщения о дне, времени и месте следующей встречи.

Чтобы было проще взаимодействовать с друзьями, вам необходимо создать класс Friend, а каждый друг будет экземпляром
этого класса. Также вам необходимо создать класс Party(place) который будет отвечать за отправление приглашений.

Периодически круг друзей меняется - иногда появляются новые, иногда исчезают старые (например, переезжают в другой
город). Чтобы наладить взаимодействие с ними, вам необходимо создать класс Party со следующими методами:

add_friend (Friend(name)) - добавляет друга 'name' в список 'наблюдателей' (людей, которые оповещаются каждый раз, когда
назначается новая встреча).

del_friend (friend) - удаляет друга friend из списка 'наблюдателей'.

send_invites() - рассылает приглашения всем друзьям из списка 'наблюдателей'.

Класс Friend должен иметь метод show_invite() , который возвращает текст последнего приглашения, полученного человеком с
указанием места, дня и времени. Место будет указано при создании экземпляра Party. Если человек не получил приглашения,
то этот метод должен вернуть - "No party..."

В этой миссии вам может помочь такой шаблон проектирования, как Observer .

# Примеры

```python
party = Party("Midnight Pub")
nick = Friend("Nick")
john = Friend("John")
lucy = Friend("Lucy")
chuck = Friend("Chuck")

party.add_friend(nick)
party.add_friend(john)
party.add_friend(lucy)
party.send_invites("Friday, 9:00 PM")
party.del_friend(nick)
party.send_invites("Saturday, 10:00 AM")
party.add_friend(chuck)

john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
chuck.show_invite() == "No party..."
```

**Входные данные:** методы класса Party и друзья.

**Выходные данные:** текст приглашения, полученного человеком.

**Как это используется:** Для автоматической рассылки оповещений об изменении информации всем наблюдателям.

**Предусловие:** Все имена друзей будут различными.

# Solution

```python
class Friend:
    def __init__(self, name):
        self.name = name
        self.date = 'No party...'

    def update(self, date: str) -> None:
        self.date = date

    def show_invite(self):
        return self.date

class Party:
    def __init__(self, name_of_party):
        self.name_of_party = name_of_party
        self.observers = []

    def add_friend(self, name: Friend):
        self.observers.append(name)

    def send_invites(self, party_date: str):
        for friend in self.observers:
            friend.update(self.name_of_party + ': ' + party_date)

    def del_friend(self, name: Friend):
        self.observers.remove(name)



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
    print("Coding complete? Let's try tests!")

```