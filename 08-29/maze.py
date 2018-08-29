import random

import shutil

# this function will tell me how wide and tall my terminal is
width, height = shutil.get_terminal_size()

for i in range(width*height): 
    if random.randint(0, 1) == 0:
        print("╱", end="")
    else:
        print("╲", end="")
