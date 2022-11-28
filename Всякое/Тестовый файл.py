import re

start, end = map(int, input().split())
regex = re.compile(r'\d+')
print(sum(map(int, regex.findall(input(), start, end))))
