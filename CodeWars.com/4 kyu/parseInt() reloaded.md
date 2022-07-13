# parseInt() reloaded

In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

**Examples:**

* "one" => 1
* "twenty" => 20
* "two hundred forty-six" => 246
* "seven hundred eighty-three thousand nine hundred and nineteen" => 783919

**Additional Notes:**

* The minimum number is "zero" (inclusively)
* The maximum number, which must be supported is 1 million (inclusively)
* The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
* All tested numbers are valid, you don't need to validate them

# Solution

```python
def parse_int(string):
    import re
    res = 0
    d = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
        "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
        "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,
        "thousand": 1000, "million": 1000000
    }
    if string == 'one million':
        return 1000000
    x = re.split(' million | million| thousand |million | thousand', string.replace(' and', ''))
    y = x[::-1]
    if len(y) >= 1:
        hund = y[0].split('hundred') if 'hundred' in y[0] else ['zero', y[0]]
        res += d[hund[0].strip()] * 100 + (
            (d[hund[1].strip()] if '-' not in hund[1] else d[hund[1].strip().split('-')[0]] + d[hund[1].strip().split('-')[1]]) if hund[1] != '' else 0)
    if len(y) >= 2:
        hund2 = y[1].split('hundred') if 'hundred' in y[1] else ['zero', y[1]]
        res += 1000 * (d[hund2[0].strip()] * 100 + ((d[hund2[1].strip()] if '-' not in hund2[1] else d[hund2[1].strip().split('-')[0]] + d[hund2[1].strip().split('-')[1]]) if hund2[1] != '' else 0))
    if len(y) >= 3:
        res += 1000000 * d[y[2]]
    return res
```