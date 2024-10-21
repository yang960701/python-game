import turtle

#triangle, square, arrow, circle
turtle.shape("turtle")
#背景色の指定
turtle.bgcolor("pink")

#線の指定
turtle.color("hotpink")
for i in range(4) :
    #位置の変更 前に100
    turtle.forward(100)
    #回転　左に90
    turtle.left(90)

turtle.color("black")
for i in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.color("white")
for i in range(5):
    turtle.forward(100)
    turtle.left(360/5)
