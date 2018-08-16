a = 5
b = a
b = 4

print("a is", a, "and b is", b)

l1 = [1,2,3]
l2 = l1
l2[0] = 2

print("l1 is", l1, "and l2 is", l2)

def f(x):
    x = x + 1
    print("inside of f, x is", x)

x = 2
f(x)
print("x is", x)

def g(l):
    l[0] = 2
    print("inside of g, l is", l)

tiny_list = [1,2,3]
g(tiny_list)
print("tiny_list is", tiny_list)
