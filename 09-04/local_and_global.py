global_var = 5

def f(y):
    # if there were a global variable called x,
    x = y * 7
    # the above line would make a local variable called x,
    # and NOT update the global x

    # global_var = 7 makes a new variable called global_var
    global_var = 7

def g(y):
    x = y + 2

def update_global_var():
    # you can always access a global variable,
    # but you need to say "global varname"
    # if you want to update it
    global global_var
    # now I'm able to update the global variable,
    # and a local var of that same name will NOT
    # get created
    global_var = 6
    x = 42

f(8)

print(global_var) # shouldn't change

g(9)

update_global_var()

print(global_var) # should change