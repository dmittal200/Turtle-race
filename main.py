import random
from turtle import Turtle, Screen

screen = Screen()
race_on = False
screen.setup(width=500, height=400)
color = ['red','orange','black', 'purple', 'yellow']
user_bet = screen.textinput(title="Make your bet", prompt=f"Choose any color {color}")
all_turtle = []
yaxis = -150
for x in range(len(color)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[x])
    yaxis = yaxis+50
    new_turtle.goto(x=-230, y=yaxis)
    all_turtle.append(new_turtle)

if user_bet:
    race_on = True

while race_on:

    for turtle in all_turtle:
        if turtle.xcor()>230:
            race_on=False
            win_color = turtle.pencolor()
            if win_color==user_bet:
                print(f"You have won! {win_color} is the winning turtle")
                break
            else:
                print(f"You have lost! {win_color} is the winning turtle")
                break

        random_dis = random.randint(0,10)
        turtle.forward(random_dis)


screen.exitonclick()
