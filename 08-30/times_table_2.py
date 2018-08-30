def print_times_table_1_to_5():
    for i in range(1, 6):
        # this loops deals with rows
        for j in range(1, 6):
            # this loop worries about columns
            print("{:2}".format(i * j), end=" ")
        print()

def print_times_table(size):
    largest_number = size ** 2
    width_of_largest_number = len(str(largest_number))

    for i in range(1, size + 1):
        # this loops deals with rows
        for j in range(1, size + 1):
            # this loop worries about columns
            print(("{:" + str(width_of_largest_number) + "}").format(i * j), end=" ")
        print()


if __name__ == '__main__':
    width = int(input("How large do you want your times table? "))
    print_times_table(width)