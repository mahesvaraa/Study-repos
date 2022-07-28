# Write out numbers

https://www.codewars.com/kata/52724507b149fa120600031d

Create a function that transforms any positive number to a string representing the number in words. The function should
work for all numbers between 0 and 999999.

**Examples**

```python
number2words(0) == > "zero"
number2words(1) == > "one"
number2words(9) == > "nine"
number2words(10) == > "ten"
number2words(17) == > "seventeen"
number2words(20) == > "twenty"
number2words(21) == > "twenty-one"
number2words(45) == > "forty-five"
number2words(80) == > "eighty"
number2words(99) == > "ninety-nine"
number2words(100) == > "one hundred"
number2words(301) == > "three hundred one"
number2words(799) == > "seven hundred ninety-nine"
number2words(800) == > "eight hundred"
number2words(950) == > "nine hundred fifty"
number2words(1000) == > "one thousand"
number2words(1002) == > "one thousand two"
number2words(3051) == > "three thousand fifty-one"
number2words(7200) == > "seven thousand two hundred"
number2words(7219) == > "seven thousand two hundred nineteen"
number2words(8330) == > "eight thousand three hundred thirty"
number2words(99999) == > "ninety-nine thousand nine hundred ninety-nine"
number2words(888888) == > "eight hundred eighty-eight thousand eight hundred eighty-eight"
```

# Solution

```python
"""
Решение с интернета, но красивое
"""
ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}
illions = {
    1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
    6: 'quintillion', 7: 'sextillion', 8: 'septillion', 9: 'octillion',
    10: 'nonillion', 11: 'decillion'}

tire = {
    0: '',
    1: '-'
}


def number2words(i):
    """
    Convert an integer in to it's word representation.

    say_number(i: integer) -> string
    """
    if i < 0:
        return _join('negative', _say_number_pos(-i))
    if i == 0:
        return 'zero'
    return _say_number_pos(i)


def _say_number_pos(i):
    if i < 20:
        return ones[i]
    if i < 100:
        return _join(tens[i // 10] + tire[i % 10 != 0] + ones[i % 10])
    if i < 1000:
        return _divide(i, 100, 'hundred')
    for illions_number, illions_name in illions.items():
        if i < 1000**(illions_number + 1):
            break
    return _divide(i, 1000**illions_number, illions_name)


def _divide(dividend, divisor, magnitude):
    return _join(
        _say_number_pos(dividend // divisor),
        magnitude,
        _say_number_pos(dividend % divisor),
    )


def _join(*args):
    return ' '.join(filter(bool, args))
```