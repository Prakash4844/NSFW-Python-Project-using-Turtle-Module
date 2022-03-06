import turtle
t = turtle.Turtle()

# full screen
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)

# do curve
def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

# first testicle
t.fillcolor("black")
t.begin_fill()
t.circle(50)
t.end_fill()

# move pen to the other side
t.penup()
t.setpos(100, 0)
t.pendown()

# second testicle
t.fillcolor("black")
t.begin_fill()
t.circle(50)
t.end_fill()

# first line of the shaft
t.left(90)
t.forward(250)

# glan of the penis
t.fillcolor("brown")
t.begin_fill()
t.circle(50)
t.end_fill()

# rectangular shaft
t.fillcolor("black")
t.begin_fill()
t.left(90)
t.forward(100)

t.left(90)
t.forward(200)

t.left(90)
t.forward(100)
t.end_fill()

# creating the Uretheral opening of the penis glan
t.backward(45)
t.left(90)
t.forward(250)

# color of urine and curve of urine stream
t.color("yellow")
t.pensize(5)
curve()

turtle.done()