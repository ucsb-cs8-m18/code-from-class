import time

# let's write to a file called file2.txt *inside* inner_folder
in_file = open("inner_folder/file2.txt", "a")

text = in_file.write("\n" + str(time.time()) + "\n")

in_file.close()
