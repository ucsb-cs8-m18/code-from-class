# let's print the numbers from 1 to 10 using for and while

for i in range(1, 11):
    print(i)

i = 1
while i <= 10:
    print(i)
    # i = i + 1
    i += 1 # same as above
    
v = 0
i = 1
while i <= 5:
    v = v + i
    i = i + 1
print(v)
