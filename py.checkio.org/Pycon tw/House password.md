# House Password

We have prepared a set of Editor's Choice Solutions. You will see them first after you solve the mission. In order to
see all other solutions you should change the filter.

Стефан и София забывают о безопасности и используют простые пароли для всего. Помогите Николе разработать модуль для
проверки паролей на безопасность. Пароль считается достаточно стойким, если его длина больше или равна 10 символам, он
содержит, как минимум одну цифру, одну букву в верхнем и одну в нижнем регистре. Пароль может содержать только латинские
буквы и/или цифры.

**Вх. данные**: Пароль как строка.

**Вых. данные:** Безопасность пароля в виде булевого значения (bool) или любого типа данных, который может быть
сконвертирован и представлен как булево значение (True или False)

**Пример:**

```python
checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True
```

**Как это используется**: Если вы беспокоитесь о безопасности вашего приложения или сервиса, вы можете проверять пароли
ваших пользователей на "сложность". Также вы можете использовать свои навыки и усложнить требования к паролям.

**Предусловия :**
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64

# Solution

```python
import re
from string import ascii_lowercase, ascii_uppercase


def checkio(data: str) -> bool:
    return len(data) >= 10 and any(re.findall(f'[{ascii_lowercase}]', data)) and any(
        re.findall(f'[{ascii_uppercase}]', data)) and any(re.findall(r'[0-9]', data))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

```