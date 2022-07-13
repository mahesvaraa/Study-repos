unit = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teen = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
ten = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

x = '41'

res = [
    unit[int(x[-7])] + ' million ' if len(x) >= 7 else '',
    unit[int(x[-6])] + ' hundred ' if len(x) >= 6 else '',
    (ten[int(x[-5])], teen[int(x[-5]) + 1])[x[-2] == '1'] + ['', '-'][x[-3] != '0'] if len(x) >= 5 else '',
    unit[int(x[-4])] + ' thousand ' if len(x) >= 4 else '',
    unit[int(x[-3])] + ' hundred ' if len(x) >= 3 else '',
    (ten[int(x[-2])], teen[int(x[-2]) + 1])[x[-2] == '1'] + ['', '-'][x[-1] != '0'] if len(x) >= 2 else '',
    unit[int(x[-1])] if len(x) >= 1 and x[-2] != '1' else '',
]
print(''.join(res))
