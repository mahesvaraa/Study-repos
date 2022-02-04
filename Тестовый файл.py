from fractions import Fraction as F

n = int(input())
x = sorted(list({F(i, j) for i in range(1, n + 1) for j in range(1, n + 1)}))
[print(i) for i in x if i < 1]
