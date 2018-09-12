# for loops iterate through things (lists, range(_) statements)
for i in [1,2,3]:
    # and the variable i becomes the current element each time the
    # body gets executed
    print(i*2)


# assignment statements evaluate the right hand side first,
# because Python needs to get the value before it can store
# that value as the variable mentioned on the left hand side
x = 2 + 2

try:
    # try to execute all the code in this indented try block
    x = 2 / 0
except ZeroDivisionError:
    # BUT, if a ZeroDivisionError is raised, 
    # then immediately jump here and DON'T
    # continue executing the rest of the try block
    print("uh oh")
