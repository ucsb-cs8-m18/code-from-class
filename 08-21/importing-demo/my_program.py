import my_module

print("My name is {}".format(__name__))


if __name__ == "__main__":
    print("my_program.py is being run as the main program")
    print(my_module.f())
