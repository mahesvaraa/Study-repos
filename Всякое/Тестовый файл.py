s = input()
s = s.replace(' ', '').replace('+', ' ').replace('-',' -')
print(sum(map(int, s.split())))

