# from turtle import Turtle, Screen
import turtle
import random

screen = turtle.Screen()
screen.setup(width=800, height=400)

FONT = ("Courier", 20, "bold")
def track():
    road = turtle.Turtle()
    road.shape('square')
    road.color('green', 'grey')
    road.shapesize(4, 40, 5)
    road.penup()
    road.goto(0, 50)
    road.stamp()
    road.goto(0, -50)
    road.stamp()
    road.goto(0, -150)
    road.stamp()

    road.color('orange')
    road.shapesize(3, 10)
    road.penup()
    road.goto(0, 165)
    road.stamp()
    road.goto(-95, 150)
    road.color('black')
    road.hideturtle()
    road.write('начать гонки', font=FONT)

def race(x, y):    
    
    tina.hideturtle()
    tina.goto(-380, -50)
    
    tom.hideturtle()
    tom.goto(-380, 50)
    
    tim.hideturtle()
    tim.goto(-380, -150)
    tina.showturtle()
    tim.showturtle()
    tom.showturtle()
    turtle.reset()
    is_on = True
    winner = 0

    while is_on:
        if tina.xcor() > 350:
            is_on = False
            winner = 2
        if tom.xcor() > 350:
            is_on = False
            winner = 1
        if tim.xcor() > 350:
            is_on = False
            winner = 3
        random_tina = random.randint(0, 7)
        tina.forward(random_tina)
        random_tom = random.randint(0, 7)
        tom.forward(random_tom)
        random_tim = random.randint(0, 7)
        tim.forward(random_tim)
    turtle.write(f'win {winner} track', font=FONT)

    

track()
tina = turtle.Turtle()
tina.shape('turtle')
tina.color('green')
tina.shapesize(2)
tina.penup()
tina.goto(-380, -50)

tom = turtle.Turtle()
tom.shape('turtle')
tom.color('purple')
tom.shapesize(2)
tom.penup()
tom.goto(-380, 50)

tim = turtle.Turtle()
tim.shape('turtle')
tim.color('#ff72aa')
tim.shapesize(2)
tim.penup()
tim.goto(-380, -150)

screen.onscreenclick(race)
