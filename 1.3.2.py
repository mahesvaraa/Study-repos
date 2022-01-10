word = input().lower()
print(('no', 'yes')[word == word[::-1]])
