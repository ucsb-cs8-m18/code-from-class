month = 8
day = 16
year = 2018

# separate things between commas with the empty string
print(month, "/", day, "/", year, sep="")

print(str(month) + "/" + str(day) + "/" + str(year))

print(month, day, year, sep="/")

# "...{}..." is a format string

print("{0}/{1}/{2}".format(month, day, year))

print("{1}/{0}/{2}".format(month, day, year))

print("{2}/{0}/{1}".format(month, day, year))

# this is the same as print("{0}/{1}/{2}".format(month, day, year))
print("{}/{}/{}".format(month, day, year))

# let's make a times table now

# the :5 part sets the width of the thing you're printing
# to be 5 spaces wide
print("{0:5}".format(42))

for i in range(1, 6):
    print("{} {} {} {} {}".format(i*1, i*2, i*3, i*4, i*5))

for i in range(1, 6):
    print("{:2} {:2} {:2} {:2} {:2}".format(i*1, i*2, i*3, i*4, i*5))

# apparently the < left aligns things
for i in range(1, 6):
    print("{:<2} {:<2} {:<2} {:<2} {:<2}".format(i*1, i*2, i*3, i*4, i*5))

# end is usually set to "\n", which is a new line
print(42, end="")
print(" hi", end="")
