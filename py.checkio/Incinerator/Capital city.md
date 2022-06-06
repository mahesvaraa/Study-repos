# Capital city

Вы - активный путешественник, который побывал уже не в одном десятке стран мира. Ваш богатый опыт натолкнул вас на
мысль, что самые интересные и передовые вещи в стране проще всего найти в ее столице. Ваша задача - реализовать класс
Capital(), для которого можно было бы создать только один объект с глобальным доступом к нему, а все последующие
создаваемые экземпляры этого класса не перезаписывали бы первый (и единственный) экземпляр. Также вам необходимо
реализовать метод name() который возвращает название столицы. В этой миссии вам может помочь такой шаблон
проектирования, как Singleton .

# Примеры

```python

russian_capital_1 = Capital("Moscow")
russian_capital_2 = Capital("London")
russian_capital_3 = Capital("Marocco")
russian_capital_2.name() == "Moscow"
russian_capital_3.name() == "Moscow"
```

**Входные данные:** класс Capital.

**Выходные данные:** название столицы.

**Как это используется:** Для создания уникального объекта в единственном экземпляре.

**Предусловие:** Все данные корректны.

# Solution

```python
def singleton(Cls):
    singletons = {}

    def getinstance(*args, **kwargs):
        if Cls not in singletons:
            singletons[Cls] = Cls(*args, **kwargs)
        return singletons[Cls]

    return getinstance


@singleton
class Capital(object):
    def __init__(self, names):
        self.names = names

    def name(self):
        return self.names

```