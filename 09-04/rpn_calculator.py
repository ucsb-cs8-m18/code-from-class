# make a reverse polish notation calculator
# read a string and then do the operations

stack = []

if __name__ == '__main__':
    # read in a string from the user, 
    # and then separate it into commands
    # for the calculator
    s = input("Enter your expression: ")
    s = s.split()

    # iterate through our list of commands
    # and perform each operation
    for command in s:
        if command == "+":
            # pop twice, do the operation, and then push result
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operand1 + operand2
            stack.append(result)
        elif command == "-":
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operand1 - operand2
            stack.append(result)
        elif command == "/":
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operand1 / operand2
            stack.append(result)
        elif command == "*":
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operand1 * operand2
            stack.append(result)
        else: # command should be a number in this case
            stack.append(int(command))

    print(stack)