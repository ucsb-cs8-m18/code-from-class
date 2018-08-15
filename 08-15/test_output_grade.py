# test with "python3 -m pytest test_output_grade.py"

import pytest

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

# test cases start with test_ (or end with _test)
def test_calculate_grade_1():
    # this test case makes sure that calculate_grade returns
    # "A" when the percentage is 95
    assert(calculate_grade(95) == "A")

##def test_calculate_grade_bad():
##    # this test should fail
##    assert(calculate_grade(60) == "F")

def test_calculate_grade_2():
    # this test case makes sure that calculate_grade returns
    # "A" when the percentage is 95
    assert(calculate_grade(70) == "C")

def test_calculate_grade_3():
    # this test case makes sure that calculate_grade returns
    # "A" when the percentage is 95
    assert(calculate_grade(55) == "F")

def test_calculate_grade_4():
    # this test case makes sure that calculate_grade returns
    # "A" when the percentage is 95
    assert(calculate_grade(-5.5) == "invalid")

def test_calculate_grade_5():
    # this test case makes sure that calculate_grade returns
    # "A" when the percentage is 95
    assert(calculate_grade("asdf") == "invalid")
