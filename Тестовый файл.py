def number_to_words(num):
    decimal = ["ноль", 'десять', "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
               "девяносто"]
    simple = ["ноль", 'один', "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    ten_to_twenty = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",
                     "семнадцать", "восемнадцать", "девятнадцать"]
    if num % 10 == 0:
        return decimal[num // 10]
    elif num < 10:
        return simple[num]
    elif 10 < num < 20:
        return ten_to_twenty[num % 10]
    elif num >= 20:
        return decimal[num // 10] + " " + simple[num % 10]
# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
print(number_to_words(7))
print(number_to_words(85))

