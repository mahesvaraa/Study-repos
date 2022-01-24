n, length = map(int, input().split())
dic, result, temp = {}, [], ''

for i in range(n):
    letter, stroka = input().split(': ')
    dic[letter] = stroka

word_decode = input()
arr = sorted(dic.items(), key=lambda x: x[1], reverse=True)
max_len = len(max(sorted(dic.values(), reverse=True), key=len))

for i in word_decode:
    temp += i
    for k, v in arr:
        if v == temp:
            result.append(k)
            temp = ''
            break

print(''.join(result))
