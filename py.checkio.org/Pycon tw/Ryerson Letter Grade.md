Given the grade percentage for the course, calculate and return the letter grade that would appear in the Ryerson’s
grade transcript, as defined on the page Ryerson Grade Scales . The letter grade should be returned as a string that
consists of the uppercase letter followed by the possible modifier "+" or "-" .

|Letter|    Percentage|
| ------------- | ------------- |
|A+    |90-100    |
|A    |85-89    |
|A-    |80-84    |
|B+    |77-79    |
|B    |73-76    |
|B-    |70-72    |
|C+    |67-69    |
|C    |63-66    |
|C-    |60-62    |
|D+    |57-59    |
|D    |53-56    |
|D-    |50-52    |
|F    |0-49    |

**Input**: Int. Grade percentage.

**Output**: Str. The letter grade.

**Example**:

The initial code contains grade table as raw string. Feel free to change it in any way.

```python

ryerson_letter_grade(45) == "F"
ryerson_letter_grade(62) == "C-"
```

**Precondition**: argument can be from 0 to 150

The mission was taken from Python CCPS 109 Fall 2018. It is taught for Ryerson Chang School of Continuing Education by
Ilkka Kokkarinen

# Solution

```python
def ryerson_letter_grade(i: int) -> str:
    if i in range(0, 50):
        return 'F'
    elif i in range(50, 53):
        return 'D-'
    elif i in range(53, 57):
        return 'D'
    elif i in range(57, 60):
        return 'D+'
    elif i in range(60, 63):
        return 'C-'
    elif i in range(63, 67):
        return 'C'
    elif i in range(67, 70):
        return 'C+'
    elif i in range(70, 73):
        return 'B-'
    elif i in range(73, 77):
        return 'B'
    elif i in range(77, 80):
        return 'B+'
    elif i in range(80, 85):
        return 'A-'
    elif i in range(85, 90):
        return 'A'
    elif i >= 90:
        return 'A+'


if __name__ == '__main__':
    print("Example:")
    print(ryerson_letter_grade(45))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert ryerson_letter_grade(45) == "F"
    assert ryerson_letter_grade(62) == "C-"
    print("Coding complete? Click 'Check' to earn cool rewards!")

```