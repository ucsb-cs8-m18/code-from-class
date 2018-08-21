# this module provides the f function

def f():
    return 42

print("Hi mom") # this will get printed when we run this file 
                # AND when we import it

print("My name is {}".format(__name__))


if __name__ == "__main__":
    # if this is true, I'm the main program running right now
    # i.e., I wasn't imported
    print("my_module.py is being run as the main program")
