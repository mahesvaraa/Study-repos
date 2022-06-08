# Most Wanted Letter

Дан текст, который содержит различные английские буквы и знаки препинания. Вам необходимо найти самую частую букву в
тексте. Результатом должна быть буква в нижнем регистре.
При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте, что "A" == "a". Убедитесь, что
вы не считайте знаки препинания, цифры и пробелы, а только буквы.

Если в тексте две и больше буквы с одинаковой частотой , верните список со всеми этими буквами. Для примера, в тексте "
Hello, Evan" буквы "e" и "l" встречаются по 2 раза, так что ответом будет ["e", "l"].

**Вх. данные**: Текст для анализа, как строка.

**Вых. данные**: Список наиболее частых букв.

Примеры:

```
most_wanted("Hello World!") == ["l"]
most_wanted("How do you do?") == ["o"]
most_wanted("One") == ["o", "n", "e"]
most_wanted("Oops!") == ["o"]
most_wanted("AAaooo!!!!") == ["a", "o"]
most_wanted("abe") == ["a", "b", "e"]
```

**Как это используется:** Для большинства задач по дешифрованию необходимо знать частоту появления различных букв в
подобном тексте. Для примера, мы легко можем взломать одноалфавитный шифр подстановки, если мы знаем вероятность
появления букв. Это также может быть полезной информацией для лингвистов.

# Solution

```python
import string
from collections import Counter


def most_wanted(text: str):
    text = ''.join([i for i in text.lower() if i in string.ascii_letters])
    dict_counter = Counter(text)
    maximum = max(dict_counter, key=lambda x: dict_counter[x])
    res = []
    for i in text.lower():
        if dict_counter[i] == dict_counter[maximum] and i not in res:
            res.append(i)
    print(res)
    return sorted(res)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    most_wanted('Hello')
    assert sorted(most_wanted("Hello World!")) == ["l"], "Hello test"
    assert sorted(most_wanted("How do you do?")) == ["o"], "O is most wanted"
    assert sorted(most_wanted("One")) == ["e", "n", "o"], "All letter only once."
    assert sorted(most_wanted("Oops!")) == ["o"], "Don't forget about lower case."
    assert sorted(most_wanted("AAaooo!!!!")) == ["a", "o"], "Only letters."
    assert sorted(most_wanted("abe")) == ["a", "b", "e"], "The First."
    print("Start the long test")
    assert sorted(most_wanted("a" * 9000 + "b" * 1000)) == ["a"], "Long."
    print("The local tests are done.")

```