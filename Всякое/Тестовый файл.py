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
