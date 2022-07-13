# Calculating with Functions

https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

```python
seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
```

**Requirements**:

* There must be a function for each number from 0 ("zero") to 9 ("nine")
* There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
* Each calculation consist of exactly one operation and two numbers
* The most outer function represents the left operand, the most inner function represents the right operand
* Division should be integer division. For example, this should return 2, not 2.666666...:

```
eight(divided_by(three()))
```

# Solution

```python
def zero(func=''): return eval('0' + func)
def one(func=''): return eval('1' + func)
def two(func=''): return eval('2' + func)
def three(func=''): return eval('3' + func)
def four(func=''): return eval('4' + func)
def five(func=''): return eval('5' + func)
def six(func=''): return eval('6' + func)
def seven(func=''): return eval('7' + func)
def eight(func=''): return eval('8' + func)
def nine(func=''): return eval('9' + func)
def plus(func=''): return f'+{func}'
def minus(func=''): return f'-{func}'
def times(func=''): return f'*{func}'
def divided_by(func=''): return f'//{func}'
```