
# the thing you use to look up is called a key,
# the thing you look up with your key is called a value
# key: value, key: value, ...
d = {"x": "y", "a": "b"} # called a dictionary
# because you can look things up

print(d["x"]) # should print "y"
print(d["a"]) # should print "b"

# keys can be any immutable thing, like numbers, tuples, etc.

nicknames = {"Lawt": "Lawton",
             "Bob": "Robert",
             "Bobby": "Robert", "Rob": "Robert",
             "Nick": "Nicolas",
             "Daddy": "Chancellor Yang"}

print(nicknames["Daddy"])
