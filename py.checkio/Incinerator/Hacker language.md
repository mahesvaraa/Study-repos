Вы с друзьями решили почувствовать себя настоящими хакерами и для этого необходимо было выбрать специальный язык для
общения в сети, понятный только вам. После долгих размышлений, вы решили что в оригинале сообщения будут на английском
языке с возможностью написания времени в формате "hh:mm" и даты в формате "dd.mm.yyyy". Также (помимо "." и ":") могут
использоваться символы "!", "?", "$", "%", "@".

После того, как сообщение написано и готово к отправке - его необходимо зашифровать по следующему принципу:

- все буквы и пробелы сперва преобразовываются в соответствующие ASCII коды, а затем каждое полученное таким образом
  число преобразовывается в двоичное число, за исключением пробела - пробел должен быть отображен как "1000000", а не "
  100000".
- числа, даты, время и специальные символы, описанные выше, не изменяются. После этого сообщение будет готово к
  отправке.

Для реализации этой системы вам необходимо создать класс HackerLanguage с соответствующие методами для работы с текстом.
Команды, которые будут использоваться:

**write (text)** - дописывает к текущему тексту сообщения новый текст (text).

**delete (N)** - удаляет из текущего сообщения последние N символов.

**send() -** возвращает зашифрованное сообщение, которое будет отправлено.

**read (text)** - в качестве аргумента получает зашифрованное сообщение и возвращает его как обычный английский текст.

В этой миссии вам может помочь такой шаблон проектирования, как **Interpreter** .

# Пример

```python
message_1 = HackerLanguage()
message_1.write('Remember: 21.07.2018 at 11:11AM')
message_1.delete(2)
message_1.write('PM')
message_1.send() == '10100101100101110110111001011101101110001011001011110010:100000021.07.2018100000011000011110100100000011:1110100001001101'

message_2 = HackerLanguage()
message_2.read(
    '10011011111001100000011001011101101110000111010011101100100000011010011110011100000011011011110010.11100101101111110001011011111110100@11001111101101110000111010011101100.110001111011111101101') ==
'My email is mr.robot@gmail.com'
```

**Входные данные:** обычный или зашифрованный текст сообщения.

**Выходные данные:** зашифрованный или расшифрованный текст сообщения.

**Как это используется:** Для шифрования и дешифрования важной информации.

**Предусловие**: В тексте будут только: [a-z], [A-Z], [0-9], ".", ":", "!", "?", "$", "%", "@"

# Solution

```python
import string


class HackerLanguage:
    def __init__(self):
        self.text = ''

    def write(self, words):
        self.words = words
        for word in self.words:
            if word == ' ':
                self.words = self.words.replace(' ', '1000000')
            elif word in string.ascii_letters:
                b = bin(ord(word))[2:]
                self.words = self.words.replace(word, b)
        self.text += self.words

    def send(self):
        return self.text

    def delete(self, number):
        try:
            for i in range(number):
                if self.text[-1] in [".", ":", "!", "?", "$", "%", "@", ' ']:
                    self.text = self.text[:-1]
                else:
                    self.text = self.text[:-7]
        except IndexError:
            pass

    def read(self, message):
        res, i = '', 0
        while i != len(message):
            # print(message)
            if message[i] in [".", ":", "!", "?", "$", "%", "@"]:
                res += message[i]
                i += 1
                continue
            elif message[i:i + 7] != '1000000':
                res += chr(int('0' + f'{message[i:i + 7]}', 2))
            else:
                res += ' '
            i += 7
        return res


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")
    message_3 = HackerLanguage()
    print(message_3.read('1001001100000011000011101101100000011101001101001111001011001011100100...'))
    message = HackerLanguage()
    message.delete(10)
    message.write('I need more % and $ from this deal!')
    message.send()
```