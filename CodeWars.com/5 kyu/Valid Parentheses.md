# Valid Parentheses

https://www.codewars.com/kata/52774a314c2333f0a7000688

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The
function should return true if the string is valid, and false if it's invalid.

**Examples**

```python
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
```

**Constraints**
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input
string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (
e.g. [], {}, <>).

# Solution

```python
def valid_parentheses(text):
    text = ''.join(i for i in text if i in ')(')
    while "()" in text:
        text = text.replace("()", "")
    return not text
```