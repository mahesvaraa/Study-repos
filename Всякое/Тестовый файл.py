simbols = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"""
a = input()
c = a[::-1]
b = a
for i in simbols:
    a = a.replace(i, '')
if len(set(a)) == 1:
    print(True)
elif len(set(a[:len(a) // 2 + 1])) - len(set(a[len(a) // 2:])) not in [-1, 0, 1]:
    print(False)
else:
    for k, v in enumerate(a):
        if a[:k] + a[k + 1:] == (a[:k] + a[k + 1:])[::-1]:
            print(True)
            break
        if c[:k] + c[k + 1:] == (c[:k] + c[k + 1:])[::-1]:
            print(True)
            break
    else:
        print(False)
