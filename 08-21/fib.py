import sys

# let's print out the ith Fibonacci number

def fib(i):
    # if i is 1 or 2, we immediately know the answer
    if i == 1 or i == 2:
        return 1
    # otherwise, we need to loop
    first = 1
    second = 1
    count = 1
    while count <= i - 2:
        old_second = second
        second = first + second
        first = old_second
        count = count + 1
    return second

if __name__ == "__main__":
    if len(sys.argv) == 1: # argv is always at least of length 1
        # if we got no command line arguments, let's print out the
        # first 10 Fibonacci numbers in the sequence
        for i in range(1, 11):
            print(fib(i))
    else:
        i = int(sys.argv[1]) # the 1st command line argument will be the #
        print(fib(i))
