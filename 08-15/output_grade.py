import pytest

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    else:
        if percentage >= 80:
            return "B"
        else:
            if percentage >= 70:
                return "C"
            else:
                if percentage >= 60:
                    return "D"
                else:
                    return "F"

grade = float(input("Enter the percentage: "))
result = calculate_grade(grade)
print(result)
