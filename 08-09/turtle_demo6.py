import turtle

steve = turtle.Turtle()
steve.shape("turtle")
steve.color("green")

def draw_pentagon(length):
    steve.forward(length)
    steve.left(360/5)
    steve.forward(length)
    steve.left(360/5)
    steve.forward(length)
    steve.left(360/5)
    steve.forward(length)
    steve.left(360/5)
    steve.forward(length)

# draw_pentagon(50)

def draw_hexagon(length):
    steve.forward(length)
    steve.left(360/6)
    steve.forward(length)
    steve.left(360/6)
    steve.forward(length)
    steve.left(360/6)
    steve.forward(length)
    steve.left(360/6)
    steve.forward(length)
    steve.left(360/6)
    steve.forward(length)

# draw_hexagon(50)

def draw_polygon(n, length):
    '''
    This function draws an n-gon with length "length"
    '''
    assert(n >= 3) # apparently this works just fine for triangles, too!

    for i in range(n):
        # stuff in here gets run n times
        print("I am drawing the", i, "th side")
        steve.forward(length)
        steve.left(360/n)

#draw_polygon(8, 50)

steve.speed(0) # make steve run really fast
draw_polygon(100, 1)
