from turtle import Turtle, Screen

s = Screen()
s.bgcolor('black')
s.title('Sun')

sketch_pen = Turtle()
sketch_pen.pencolor('orange')
sketch_pen.speed(0)
sketch_pen.pensize(1)

sketch_pen.speed(0)

length, angle = 0, 0

sketch_pen.penup()
sketch_pen.goto(0, 100)
sketch_pen.pendown()
while True:
    sketch_pen.forward(length)
    sketch_pen.right(angle)
    length += 1
    angle += 0.05
    if angle == 270:
        break
    sketch_pen.hideturtle()
s.exitonclick()