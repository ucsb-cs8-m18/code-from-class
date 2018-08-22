def read_the_file_and_print_lines():
    infile = open("sample_file.txt")

    # entire_text_of_file = infile.read()
    lines_of_file = infile.readlines()

    infile.close() # I'm done working with the file now

    print(lines_of_file)

def write_to_the_file():
    file = open("sample_file.txt", "w")
    file.write("hi\n")
    file.close()

def read_and_write_to_the_file():
    # first, open the file and read all its lines
    file = open("sample_file.txt", "r")
    lines_of_file = file.readlines()
    print(lines_of_file) # print out all the lines
    file.close()

    # then, write a line to the end file
    file = open("sample_file.txt", "a") # "a" for "append"
    file.write("hi\n")
    file.close()

    # read the whole file again
    file = open("sample_file.txt", "r")
    lines_of_file = file.readlines()
    print(lines_of_file) # print out all the lines again
    file.close()

if __name__ == "__main__":
    read_and_write_to_the_file()
