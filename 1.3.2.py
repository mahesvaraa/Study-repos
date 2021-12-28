p, dollars, cents = [int(input()) for i in range(3)]
p = p / 100

summ = dollars * 100 + cents
print(int((summ * p + summ) // 100))
print(int((summ * p + summ) % 100))
