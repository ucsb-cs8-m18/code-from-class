'''
accumulator pattern: you have a variable that accumulates things
For example, you can add up the elements of a list, and accumulate their sum
in a variable
'''

# add up the numbers from 1 to 10
def sum_1_10():
    sum = 0 # sum is the accumulator
    for i in range(1, 11):
        sum = sum + i
    return sum

print(sum_1_10())

# multiply the numbers from 1 to 10, and return that

def ten_factorial():
    product = 1
    for i in range(1, 11):
        product = product * i
    return product

print(ten_factorial())

# sum of a list

def sum_list(l):
    sum = 0 # sum is the accumulator
    for i in l:
        sum = sum + i
    return sum

print(sum_list([4,5,6]))
