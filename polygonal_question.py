import turtle

turtle.shape("turtle")
turtle.bgcolor("lightblue")
turtle.pensize(10)

#turtle.textinput, turtle.numinput
polygon = int(turtle.numinput("多角","何角にしますか？"))

for i in range(polygon):
    turtle.forward(100)
    turtle.left(360 / polygon)
