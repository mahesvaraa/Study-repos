# Long Repeat Inside

Существует четыре миссии связанные с анализом частей строк. Все они были созданы за один день и не требуют более одного
дня для своего решения. Эти миссии можно с легкостью преодолеть посредством простого перебора символов. Но, возможно,
есть вариант получше? (У Вас может еще не быть доступа ко всем этим миссиям, но по мере открытия островов на карте он
будет предоставлен)

Это четвертая и последняя миссия серии. Если в первой миссии Вам нужно было найти повторяющиеся буквы, то здесь Вам
необходимо разыскать повторяющуюся последовательность в подстроке. У меня есть небольшой пример: в строке "abababc" - "
ab" является последовательностью, которая повторяется более одного раза, поэтому ответом будет "ababab".

**Входные данные:** Строка.

**Выходные данные:** Строка.

**Пример**:

```python

repeat_inside('aaaaa') == 'aaaaa'
repeat_inside('aabbff') == 'aa'
repeat_inside('aababcc') == 'abab'
repeat_inside('abc') == ''
repeat_inside('abcabcabab') == 'abcabc'
```

# Solution

```python
import re

def repeat_inside(text):
    match = re.findall(r'(?=((.+?)\2+))', text)
    return max((x[0] for x in match), key=len, default='')



if __name__ == '__main__':
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
```