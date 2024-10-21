import turtle as t
import random

def com_choice():
    random_choice = random.randint(0,2)
    com.shape(images[random_choice])
    return com_list[random_choice]

def result_print(user_c,com_c):
    global user_score, com_score
    
    t.clear()
    t.goto(0,-100)
    if user_c == com_c:
        t.write("draw",False,"center",("",50))
    elif winning_case[user_c] == com_c:
        t.write("win",False,"center",("",50))
        user_score += 1
        user_pen.clear()
        user_pen.write(user_score, False,"center", ("", 50))
    else:
         t.write("lose",False,"center",("",50))
         com_score += 1
         com_pen.clear()
         com_pen.write(com_score, False,"center", ("", 50))
         
def rock(x,y):
    user.shape(rock_gif)
    #パソコンの選択
    com = com_choice()
    result_print("rock",com)
    
def scissors(x,y):
    user.shape(scissors_gif)
    #パソコンの選択
    com = com_choice()
    result_print("scissors",com)

def paper(x,y):
    user.shape(paper_gif)
    #パソコンの選択
    com = com_choice()
    result_print("paper",com)
    
    
t.bgcolor("lavender")
t.title("rock_paper_scissors")
t.ht()
t.up()

rock_gif = "images/rock.gif"
scissors_gif = "images/scissors.gif"
paper_gif = "images/paper.gif"
t.addshape(rock_gif)
t.addshape(scissors_gif)
t.addshape(paper_gif)

t.shape(paper_gif)

images = [rock_gif,scissors_gif,paper_gif]
com_list = ["rock", "scissors", "paper"]
winning_case = {"rock":"scissors", "scissors":"paper", "paper":"rock"}

user_score = 0
com_score = 0

#自分
user = t.Turtle()
user.up()
user.speed(0)
user.goto(-200, 200)
user.write("自分の選択", False,"center", ("", 30))
user.goto(-200,-100)
user.shape(rock_gif)

#パソコン
com = t.Turtle()
com.up()
com.speed(0)
com.goto(200, 200)
com.write("パソコンの選択", False,"center", ("", 30))
com.goto(200,-100)
com.shape(rock_gif)

#user score
user_pen = t.Turtle()
user_pen.ht()
user_pen.up()
user_pen.goto(-200,100)
user_pen.write(user_score, False,"center", ("", 50))
#com score
com_pen = t.Turtle()
com_pen.ht()
com_pen.up()
com_pen.goto(200,100)
com_pen.write(user_score, False,"center", ("", 50))


t.onscreenclick(rock,1)
t.onscreenclick(scissors,2)
t.onscreenclick(paper,3)

