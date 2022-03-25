a = '12345'
from string import ascii_lowercase

alphabet = {i: v for i, v in enumerate(ascii_lowercase, 1)}
print(alphabet)
cnt = 0
for i, v in enumerate(a):
    if v:
        cnt += 1
    try:
        if int(a[i] + a[i + 1]) < 27:
            cnt += 1

    except IndexError:
        pass
print(cnt)
