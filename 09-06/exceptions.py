import pytest

# let's write a function that splits a string into words,
# and then returns the first word
def first_word(s):
    # make sure s is a string
    if type(s) != str:
        raise ValueError
    elif len(s) == 0:
        raise ValueError

    # need to make sure s had at least one word in it!
    # could either check for len(s) > 0
    # or len(s.split()) > 0

    words_of_s = s.split()
    return words_of_s[0]

# now, let's make test cases for this function

def test_first_word_1():
    assert(first_word("The quick brown fox...") == "The")

def test_first_word_2(): 
    try:
        res = first_word(42)
        # if we got here, no exception was raised
        assert(False)
    except ValueError:
        # if we got here, it raised an exception!
        # and that's what we wanted
        assert(True)

def test_first_word_3():
    # this is a slightly shorter way of making sure
    # your function raised the correct exception
    with pytest.raises(ValueError):
        res = first_word("")