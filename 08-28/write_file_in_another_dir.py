import time

# let's write to a file called file2.txt *inside* inner_folder
in_file = open("inner_folder/file2.txt", "w")

text = in_file.write(str(time.time()))

in_file.close()
