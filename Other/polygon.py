import turtle

sides = input("What's number of sides?:  ")
length = int(input("what's the length?: "))

t = turtle.Turtle()

t.pensize(3)
t.speed(0)

angle = 360 / int(sides)

for i in range(int(sides)):
    t.forward(length)
    t.left(angle)

turtle.done()
