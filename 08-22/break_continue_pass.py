'''
if 2 < 3:
    # you can't have an if/while/for/def statement without a body
'''

if 2 < 3:
    pass # the pass statement does absolutely nothing, and it's just filler
         # for when you need to type something to get the program to run

i = 1
while i <= 10:
    if i == 6: # ignore the i == 6 case
        i += 1
        continue # stop the loop body early
    elif i == 8:
        break # stop the loop
    print(i)
    i += 1
    
