globvar = 0 # globals exist in the "outermost scope", outside of anything

def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1

def try_to_globvar_to_two():
    globvar = 2

def print_globvar():
    print(globvar)     # No need for global declaration to read value of globvar

set_globvar_to_one()
print_globvar()
try_to_globvar_to_two()
print_globvar()
