import turtle

steve = turtle.Turtle()
steve.shape("turtle")
steve.color("green")

def draw_star(length):
    steve.right(90)
    steve.right(36/2)
    steve.forward(length)
    steve.left(180-36)
    steve.forward(length)
    steve.left(180-36)
    steve.forward(length)
    steve.left(180-36)
    steve.forward(length)
    steve.left(180-36)
    steve.forward(length)

draw_star(50)
draw_star(100)
draw_star(200)
