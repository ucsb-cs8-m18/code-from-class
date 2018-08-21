# this is a stub! It's partially implemented.
def calculate_grade(percentage):
    return "A"

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
