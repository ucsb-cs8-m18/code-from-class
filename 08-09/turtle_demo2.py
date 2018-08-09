import turtle

steve = turtle.Turtle()
steve.shape("turtle")
steve.color("green")

def draw_box(size):
    steve.forward(size) # steve, go forward size units
    steve.left(90) # steve, turn left 90 degrees
    steve.forward(size)
    steve.left(90)
    steve.forward(size)
    steve.left(90)
    steve.forward(size)

draw_box(50)
draw_box(100)
draw_box(200)
