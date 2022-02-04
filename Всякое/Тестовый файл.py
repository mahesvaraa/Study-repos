with open(input(), 'r', encoding='utf-8') as file, open('random.txt', 'w', encoding='utf-8') as output:
    f, l = [], []
    for line in file:
        f.append(line.strip().replace(',', "").split())
count_def = 0
count_comment = 0
for i in range(len(f)):
    if 'def' in f[i]:
        if f[i - 1] == [] or f[i - 1][0] != "#":
            print(f[i][1].split("(")[0])
            count_comment += 1
        count_def += 1
if count_def - count_comment == count_def:
    print("Best Programming Team")
