a = 5
b = 4

# I want a = 4, b = 5

'''
b = a # after this, b is 5 and a is 5
a = b # after this, a is 5 and b is 5
# so, this doesn't work
'''

temp = a # after this, temp = 5, a = 5, b = 4
a = b    # after this, temp = 5, a = 4, b = 4
b = temp # after this, temp = 5, a = 4, b = 5

# we did it!

# you can think of this as assigning tuples
(a, b) = (b, a) # this also works, and is quicker to type
a, b = b, a # this is exactly the same, just no ()s

print("a is {}, b is {}".format(a, b))
