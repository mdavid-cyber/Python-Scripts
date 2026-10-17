import turtle

seasons = [
    ("spring", 50, "pink"),
    ("summer", 60, "brown"),
    ("autumn", 70, "red"),
    ("winter", 80, "cyan")
]

width = 50
gap = 10

t = turtle.Turtle()
t.pensize(2)
t.speed(0)

t.penup()
t.goto(-200, -100)
t.pendown()
t.forward((width + gap) * len(seasons))

t.penup()
t.goto(-200, -100)
t.pendown()

for season, rainfall, color in seasons:
    t.pencolor("black")
    t.fillcolor(color)
    t.begin_fill()

    t.left(90)
    t.forward(rainfall)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(rainfall)
    t.left(90)

    t.end_fill()

    t.penup()
    t.forward(gap)
    t.pendown()

t.hideturtle()
turtle.done()

