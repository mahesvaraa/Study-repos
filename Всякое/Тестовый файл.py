# arr = [input() for _ in range(int(input()))]
# search = [input() for _ in range(int(input()))]
#
# for string in arr:
#     res = [word.lower() in string.lower() for word in search]
#     if all(res):
#         print(string)

n = int(input())
arr = []
for i in range(n):
    arr.append(input())

m = int(input())
search = []
for i in range(m):
    search.append(input())


for string in arr:                         # для каждого поискового запроса (string)
    res = []                               # инициализируем пустой список
    for word in search:                    # для каждого слова (word) в запросе search
        if word.lower() in string.lower(): # если word в нижнем регистре есть в search в нижнем регистре
            res.append(True)               # пишем True
        else:                              # иначе
            res.append(False)              # пишем False

    if all(res):                           # если все значения в списке True
        print(string)                      # выводим строку
