# a function that prints the numbers from 1 to N, recursively
def print_1_to_N(N):
    # assume I'm never given a number <= 0

    if N == 1:
        # base case: N==1
        print(1)
    else:
        # recursive case
        # the smaller subproblem is printing 1 to N-1
        print_1_to_N(N-1)
        print(N)

print_1_to_N(5)

# the magic of recursion is that when you make the recursive 
# call in the recursive case, you get to ASSUME that it does
# the right thing, and it WILL as long as you build up the
# bigger solution correctly

# a function that prints the numbers from N to 1, recursively
def print_N_to_1(N):
    # assume I'm never given a number <= 0

    if N == 1:
        # base case, immediately print 1
        print(1)
    else:
        # recursive case
        # smaller subproblem is printing N-1 to 1
        print(N)
        print_N_to_1(N-1)

print_N_to_1(5)

# does an element exist in a list?
# for example, 5 is in [1,5,4,3]
def isIn(elem, l):
    # returns True if elem is in l, false otherwise

    # base case, l is empty--immediately the answer is False
    if len(l) == 0:
        return False
    else:
        # recursive case--the problem is smaller when the
        # list is smaller
        one_smaller_list = l[1:] # if l was [1,2,3], this is [2,3]
        first_element = l[0]

        if first_element == elem:
            return True
        else:
            # if elem is there, it better be in the smaller list
            # recursive call asks if the element 
            # is in the smaller list
            return isIn(elem, one_smaller_list)

print(isIn(5, [1,5,4,3]))
print(isIn(6, [1,5,4,3]))