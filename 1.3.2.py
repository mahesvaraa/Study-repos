dollar, cent, pirog = [int(input()) for i in range(3)]
itog_cent = (dollar * 100 + cent)
ostatok = itog_cent * pirog
print(ostatok // 100, ostatok % 100)
