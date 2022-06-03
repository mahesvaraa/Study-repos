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
