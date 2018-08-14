def calculate_grade(percentage):
    if percentage >= 60:
        return "pass"
    else:
        return "fail"

grade = float(input("Enter the percentage: "))
pass_or_fail = calculate_grade(grade) # now returns a string, so let's use it

# now, pass_or_fail is a string, and calculate_grade doesn't print anything

print(pass_or_fail)
