import shutil

# this function will tell me how wide and tall my terminal is
width, height = shutil.get_terminal_size()

# let's write a program that has a "*" that bounces from left to right

import time

sleep_time = 0.01

while True: # forever,
    # go from left to right
    for i in range(width):
        print("\r" + " " * i + "*" + " " * (width - i - 1), end="")
        time.sleep(sleep_time)
    # go from right to left
    for i in range(width-1, -1, -1):
        print("\r" + " " * i + "*" + " " * (width - i - 1), end="")
        time.sleep(sleep_time)
