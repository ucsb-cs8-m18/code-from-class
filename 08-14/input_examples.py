# input function are a way of asking the user to input some text
name = input("What is your name? ") # it returns a string that is the response
# the string you give to the input function becomes the "prompt"

print("You said your name was", name)

number_as_a_string = input("What is your favorite number? ") # n is currently a string
number_as_an_int = float(number_as_a_string)

print(type(number_as_a_string))
print(type(number_as_an_int))
print(number_as_an_int + 1)
