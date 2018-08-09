import turtle

steve = turtle.Turtle()
steve.shape("turtle")
steve.color("green")

steve.forward(50)
steve.up() # stop drawing when moving
steve.forward(50) # this won't make any lines
steve.down()
steve.forward(50) # steve starts drawing another line now
