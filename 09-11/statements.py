# python statements

# normal statements get executed one after the other
print(1)
print(2)
print(3)

grade = 99
# if statements EITHER execute the True branch or the False branch

# the first that happens when Python executes this is to check
# grade >= 90
if grade >= 90:
    # if it's true, this executes, and NO OTHER BODY executes
    print("A") 
elif grade >= 80: # if the first condition isn't true, try this one next
    # if it's true, this executes, and NO OTHER BODY executes
    print("B")
else:
    # if none of the above conditions hold, then this 
    # body gets executed
    print("no")

print("done")


i = 9
while i > 0: # first, test the condition. if True, execute body
    print(i)
    i -= 1
    # once the body is done executing, always jump back to the 
    # condition once more, and try everything again
# once the condition of the while loop is False, the loop ends


