def calculate_grade(percentage):
    if percentage >= 60:
        print("pass")
    else:
        print("fail")

grade = float(input("Enter the percentage: "))
calculate_grade(grade)
