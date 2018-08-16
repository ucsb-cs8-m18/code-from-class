import turtle

bob = turtle.Turtle()
bob.shape("turtle")

'''
You can also do all this stuff with dots:

def drawDot(radius, color):
    bob.dot(radius*2, color)

def drawTargetLogoWithDots():
    drawDot(200, "red")
    drawDot(125, "white")
    drawDot(50, "red")

def drawConcentricDots():
    for i in range(20, 0, -1):
        if i % 2 == 0:
            drawDot(i*10, "white")
        else:
            drawDot(i*10, "black")
'''

def drawCircle(radius, line_color, fill_color):
    # move down by radius, so that the circle
    # gets drawn in the center of where bob is
    # currently
    bob.up()
    bob.setheading(270)
    bob.forward(radius)
    bob.setheading(0)
    bob.down()

    bob.color(line_color, fill_color)
    
    bob.begin_fill()
    bob.circle(radius)
    bob.end_fill()
    
    # move back up by radius to get back to where we were
    bob.up()
    bob.setheading(90)
    bob.forward(radius)
    bob.setheading(0)
    bob.down()

def drawTargetLogoWithCircles():
    drawCircle(200, "white", "red")
    drawCircle(125, "red", "white")
    drawCircle(50, "white", "red")

def drawConcentricCircles():
    for i in range(20, 0, -1):
        if i % 2 == 0: # if i is even
            drawCircle(i*10, "white", "black")
        else: # if i is odd
            drawCircle(i*10, "black", "white")

bob.speed(0)
# drawTargetLogoWithCircles()
drawConcentricCircles()
