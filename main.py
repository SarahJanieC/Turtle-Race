import random
from turtle import Turtle, Screen
# A turtle race betting game written in Python using the Turtle module.

is_race_on = False
screen = Screen()
screen.title("Turtle Race Game")
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue","purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0,6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230,y=y_pos[i])
    all_turtles.append(t)

user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the color: ")

if(user_bet):
    is_race_on = True

while is_race_on:

    for racer in all_turtles:
        if(racer.xcor() > 225):
            is_race_on = False
            winning_color = racer.pencolor()
            if(winning_color == user_bet):
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")
        randDistance = random.randint(0,10)
        racer.forward(randDistance)

screen.exitonclick()







