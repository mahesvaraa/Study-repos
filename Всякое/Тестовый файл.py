class Registration:

    def __init__(self, log, passwd):
        self.__login = log  # передаем в сеттер login значение логин
        self.__password = passwd  # передаем в сеттер password значение пароль
        self.login = self.login  # сразу же проверяем логин
        self.password = self.password  # сразу же проверяем пароль

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, log):
        if log.count('@') != 1:
            raise ValueError("Login must include at least one ' @ '")
        elif log.count('.') != 1:
            raise ValueError("Login must include at least one ' . '")
        else:
            self.__login = log

    @staticmethod
    def is_include_digit(s):
        return any([i in '0123456789' for i in s])

    @staticmethod
    def is_include_all_register(s):
        return [i.isupper() for i in s].count(True) > 1

    @staticmethod
    def is_include_only_latin(s):
        from string import ascii_letters
        return all([i in ascii_letters + '0123456789' for i in s])

    @staticmethod
    def check_password_dictionary(s):
        easy_passwords = '123456 password 123456789 12345 12345678 qwerty 1234567 111111 1234567890 123123 abc123 ' \
                         '1234 password1 iloveyou 1q2w3e4r 000000 qwerty123 zaq12wsx dragon sunshine princess letmein ' \
                         '654321 monkey 27653 1qaz2wsx 123321 qwertyuiop superman asdfghjkl '
        return s in easy_passwords.split()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, passwd):
        if not isinstance(passwd, str):
            raise TypeError("Пароль должен быть строкой")
        if not 5 <= len(passwd) <= 11:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not self.is_include_digit(passwd):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not self.is_include_all_register(passwd):
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
        if not self.is_include_only_latin(passwd):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if self.check_password_dictionary(passwd):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        self.__password = passwd


x = Registration('1qaz@WS.X', '1qazWSX')
x.__login = '123'
print(x.__login)
