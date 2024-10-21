import turtle as t
import random

def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def rand_pos():
    x_cor = random.randint(-360,360)
    y_cor = random.randint(-360,360)
    return x_cor, y_cor
    
# 環境設定
t.setup(800,800)
t.bgcolor("skyblue")
t.up()
t.ht()

# 変数
player_speed = 5
score = 0
game_over = False

# 点数表現
t.goto(0, 350)
t.write(f"score : {score}",False,"center",("",20))


# player
player = t.Turtle()
player.shape("turtle")
player.shapesize(2)
player.up()
player.color("lavender")
player.speed(0)

# key event
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_right, "Right")
t.listen()

# feed
food = t.Turtle()
food.ht()
food.shape("triangle")
food.up()
food.color("darkgreen")
food.speed(0)
food.setheading(90)
food.goto(rand_pos())
food.st()

# poision
p_herb = t.Turtle()
p_herb.ht()
p_herb.shape("triangle")
p_herb.up()
p_herb.color("red")
p_herb.speed(0)
p_herb.setheading(90)
p_herb.goto(rand_pos())
p_herb.st()

while not game_over:
    player.forward(player_speed)

    if player.xcor() > 360 or player.xcor() < -360 or player.ycor() > 360 or player.ycor() < -360 :
        player.right(180)
    if player.distance(food) < 20:
        food.goto(rand_pos())
        p_herb.goto(rand_pos())
        score += 1
        player_speed += 1
        t.clear()
        t.write(f"score : {score}",False,"center",("",20))

    if player.distance(p_herb) < 20:
        game_over = True
    

t.goto(0,0)
t.write("Game Over",False,"center",("",50))
