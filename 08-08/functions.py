def square(x):
    '''
    This is called a docstring! (doc is for documentation)
    It's supposed to tell people who use your function
    what it does.
    '''
    # return gives back the final answer
    return x ** 2 # (or x * x)

def derivative(f, x):
    '''
    Derivative of function f at x
    '''
    h = 0.00000001
    return (f(x + h) - f(x)) / h
    
x = 4
y = 5
print(square(y + 2))

print(derivative(square, 1))
print(derivative(square, 2))
