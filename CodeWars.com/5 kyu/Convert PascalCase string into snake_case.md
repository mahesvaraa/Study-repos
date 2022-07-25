# Convert PascalCase string into snake_case

https://www.codewars.com/kata/529b418d533b76924600085d

Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation.
Lowercase characters can be numbers. If the method gets a number as input, it should return a string.

**Examples**

```python
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"
```

# Solution
```python
def to_underscore(string):
    string = str(string)
    for i, v in enumerate(string):
        if v.isupper():
            string = string.replace(v, '_' + v.lower())
    if string[0] == '_':
        string = string[1:]
    return string
```