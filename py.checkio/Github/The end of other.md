# The end of other

Для практики в лингвистике Роботы хотят изучить суффиксы.

В этой задаче дан набор слов в нижнем регистре. Проверьте есть ли в этом наборе пара слов, такая что одно слово
заканчивается другим (суффикс или совпадение). Для примера: {"hi", "hello", "lo"} -- "lo" это окончание "hello", так что
результат True.

**Замечания**: Для этой задачи вы можете прочитать о типе данных set и строковых функциях .

**Вх. данные**: Слова как набор (set) строк (str).

**Вых. данные**: True или False, как булево выражение.

Примеры:

```python
checkio({"hello", "lo", "he"}) == True
checkio({"hello", "la", "hellow", "cow"}) == False
checkio({"walk", "duckwalk"}) == True
checkio({"one"}) == False
checkio({"helicopter", "li", "he"}) == False
```

**Как это используется**: В этой задаче вы познакомитесь с тем, как итерировать тип данных set и некоторыми полезными
функциями.

**Предусловия**: 2 ≤ len(words) < 30
all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)

# Solution

```python
def checkio(words_set):
    for i in words_set:
        for j in words_set:
            if i != j and list(i) == list(i)[:-len(j)] + list(j):
                return True
    else:
        return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio({"hello", "lo", "he"}))

    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
    print("Done! Time to check!")
```