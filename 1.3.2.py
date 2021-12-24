text = input()

temp = {}  # сколько раз встречается "тот или иной" символ
for char in text:
    if not char in temp:
        temp.update({char: 1})
    else:
        temp[char] += 1

# подсчет длины самого длинного палиндрома
result = 0
for key in temp:
    result += 2 * (temp[key] // 2)
if len(text) - result > 0:
    result += 1

print(result)
