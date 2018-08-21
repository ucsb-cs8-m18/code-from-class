#!/usr/bin/env python3

# the above line is called a "shebang", and it tells the shell
# which program I want to use to run this file

# chmod u+x command_line_args.py
# makes this file executable to the user who owns it

# the above only will work in Linux/Unix/Macs
# instead of running the program as "python3 command_line_args.py 42",
# you can run it as "./command_line_args.py 42"

import sys
import math

'''
Let's write a program that takes 1 command
line argument and outputs the square root
of that argument.
'''

def main():
    number = sys.argv[1]
    number = float(number)
    print(math.sqrt(number))

# name is set to "__main__" when we are running the program,
# and otherwise it's the name of the file
if __name__ == "__main__":
    print(sys.argv)
    main()
