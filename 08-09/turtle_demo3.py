import turtle

steve = turtle.Turtle()
steve.shape("turtle")
steve.color("green")

def draw_rectangle(width, height):
    steve.forward(width) # steve, go forward size units
    steve.left(90) # steve, turn left 90 degrees
    steve.forward(height)
    steve.left(90)
    steve.forward(width)
    steve.left(90)
    steve.forward(height)

draw_rectangle(50, 100)
#draw_rectangle(100, 50)
#draw_rectangle(50, 50)

# in lab01, you'll make, e.g., a function called drawL(width,height)
