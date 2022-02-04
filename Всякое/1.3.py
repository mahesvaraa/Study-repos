from collections import Counter

word = input()
word_counter = list(map(list, Counter(word).most_common()[::-1]))
while len(word_counter) > 2:
    left, right = word_counter[0], word_counter[1]
    word_counter = word_counter[2::]
    word_counter.append([left[0:-1], right[0:-1], left[-1] + right[-1]])
    word_counter.sort(key=lambda x: x[-1])


def find_idx(input_list, elem):
    for i in range(len(input_list)):
        if isinstance(input_list[i], list):
            result = find_idx(input_list[i], elem)
            if result:
                return [i] + result
        elif input_list[i] == elem:
            return [i]

    return False


dic = {}
result = ''

for i in set(word):
    dic[i] = ''.join(list(map(str, find_idx(word_counter, i))))[:-1]

for i in word:
    result += str(dic[i])

print(len(set(word)), len(result))

for k, i in sorted(dic.items()):
    print(k, ': ', i, sep="")
print(result)