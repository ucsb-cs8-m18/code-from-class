def calculate_grade(percentage):
    # make sure we get either a float or an int
    if type(percentage) != int and type(percentage) != float:
        return "invalid"

    # now that we know we have a float or an int, make sure
    # the percentage is within a valid range
    if percentage < 0 or percentage > 100:
        return "invalid"

    # if we got this far, we are not "invalid"
    
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

def test_calculate_grade_1():
    assert(calculate_grade(95) == "A")

def test_calculate_grade_2():
    assert(calculate_grade(70) == "C")

def test_calculate_grade_3():
    assert(calculate_grade(55) == "F")

def test_calculate_grade_4():
    assert(calculate_grade(-5.5) == "invalid")

def test_calculate_grade_5():
    assert(calculate_grade("asdf") == "invalid")
