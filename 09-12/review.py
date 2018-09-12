# F₀ = 2, F₁ = 3, Fₙ = F_(n-1) * F_(n-2) (if n > 1)
# so, the sequence is 2, 3, 6, 18, ...
def fancy_fib(N):
    # this function returns the Nth element of the seq.
    # base cases are N == 0 and N == 1
    if N == 0:
        # print("fancy_fib({}) = 2".format(N))
        return 2
    elif N == 1:
        # print("fancy_fib({}) = 3".format(N))
        return 3
    else:
        # recursive case
        res = fancy_fib(N-1) * fancy_fib(N-2)
        # print("fancy_fib({}) = {}".format(N, res))
        return res

for i in range(10):
    print(fancy_fib(i))

# checking for a list with things of one type
def checkIfListOfInts(l):
    # return True if this is a list full of ints,
    # False otherwise
    if type(l) != list:
        return False

    # if we got this far, we haven't returned False,
    # which means we at least have a list to work with
    for elem in l:
        if type(elem) != int:
            return False

    # if we got this far, the loop has finished going
    # through the list and making sure everything there
    # is an int. If one element was not an int, we would
    # have returned False
    return True

print(checkIfListOfInts([1,2,3]))
print(checkIfListOfInts([1,2,3, "asdf"]))
print(checkIfListOfInts("asdf"))

# checking for a list with things of one type
def checkIfListOfInts2(l):
    # return True if this is a list full of ints,
    # False otherwise
    if type(l) == list:
        # this is good, keep going

        # we have a list, let's iterate through it
        for elem in l:
            if type(elem) == int:
                # this also good
                pass
                # using continue here instead would stop any further
                # execution of the loop body
            else:
                # this is bad
                return False

        # we got this far, so everything was good
        return True
    else:
        # we didn't have a list
        return False

print(checkIfListOfInts2([1,2,3]))
print(checkIfListOfInts2([1,2,3, "asdf"]))
print(checkIfListOfInts2("asdf"))

# python variable names can be made up of a-z, A-Z, _, and 0-9, 
# but can't start with a digit

