"""
By Allister "Big G" Gulley

1. A list and description of all of the resources you used to help you make this project.  If you followed a tutorial, I want to know.  Your project can't be a carbon copy of the tutorial though.  Include links to resources you used to help you add other things to your project as well, not just the tutorial link.  IT SHOULD BE WELL DOCUMENTED!  Use docstrings and comments to make it easy for me to figure out what your program does without me needing to run it.

2. A seperate explanation of your project.  Explain why you chose this idea, what the program does, any challenges you had to overcome, anything you learned from the process of, etc.  Also, talk about the library you learned about and anything else it is capable of that you did not include in your program.

3. A link to your Replit

4. A link to your GitHub repo for the project

Used Turtle Graphics Functions:
goto() : sets turtle to go somewhere
setx() : sets x coordinate
sety() : sets y coordinate
xcor() : variable for x coord
ycor() : variable for y coord
penup() : stops turtle from drawing
color() : sets turtle color
shape() : creates turtle shape
bgcolor() : sets background color
position() : sets turtle position
hideturtle() : makes turtle invisible
onkeypress() : activates when a key is pressed

Resources Used:
https://www.cs.auckland.ac.nz/courses/compsci111ssc/lectures/LectureSlides/L25_Python3.pdf
https://docs.python.org/3/library/turtle.html
https://www.w3schools.com/python/ref_random_choices.asp
https://trinket.io/docs/colors
https://docs.python.org/3/library/random.html#random.choice
https://www.geeksforgeeks.org/create-pong-game-using-python-turtle/
https://stackoverflow.com/questions/42107249/how-to-add-exception-to-random-randint-in-python
https://stackoverflow.com/questions/71247245/how-do-you-use-dx

Repl:https://replit.com/@TheBambbozler/My-Pong-Game#main.py
Github: https://github.com/3GG5c3L3n7/Pong-Game
"""
import turtle
from random import choice
from random import randint

#creates screen
sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("black")
sc.colormode(255)
sc.setup(width=1080, height=720)

#creates "PONG"
menu = turtle.Turtle()
menu.speed(0)
menu.color("white")
menu.penup()
menu.hideturtle()
menu.goto(0, 275)
menu.write("PONG", align="center", font=("Times New Roman", 50, "normal"))

#creates list of usable colors
color_list=(['lime green','dark violet','red','orange','light blue','indigo'])
chosen_color=choice(color_list)
#chooses random numbers from list for ball start direction
numbers=[-5,-4,-3,-2,2,3,4,5]
number1=choice(numbers)
number2=choice(numbers)
#ball speed
speed=1

#creates pong ball
ball = turtle.Turtle()
ball.speed(speed)
ball.shape("circle")
ball.color("yellow") # color
ball.penup()
ball.goto(0, 0)
#ball start direction coordinates
ball.dx = number1# default 5
ball.dy = number2# default -5

#creates player scores
left_player=0
right_player=0
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 240)
sketch.write("Player1 : 0    Player2 : 0", align="center", font=("Comic Sans MS", 24, "normal"))

# functions to move the left or right paddle up/down during button press
#also checks if pad is going past y-coord border or not
def pad1_up():
    y=left_pad.ycor()
    if y < 175:
        y+=20
        left_pad.sety(y)
def pad1_down():
    y=left_pad.ycor()
    if y > -175:  
        y-=20
        left_pad.sety(y)
def pad2_up():
    y=right_pad.ycor()
    if y < 175:
        y+=20
        right_pad.sety(y)
def pad2_down():
    y=right_pad.ycor()
    if y > -175:
        y-=20
        right_pad.sety(y)

#Binds the keypresses to the pad movement functions
sc.listen()
sc.onkeypress(pad1_up, "q")
sc.onkeypress(pad1_down, "a")
sc.onkeypress(pad2_up, "Up")
sc.onkeypress(pad2_down, "Down")

#creates border
border = turtle.Turtle()
border.speed(0)
border.shape("square")
border.color("white")
border.fillcolor(chosen_color)
border.shapesize(stretch_wid=24, stretch_len=60)
border.penup()
border.goto(0,0)

#creates left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400,0)

#creates right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400,0)

#game loop
#ALSO, dx and dy are x and y velocities, so multiplying by a # will abruptly change direction FOR EXAMPLE, if x were 2 and y were 0, it would move left, if x were -2 and y was -8, it would move downward while moving left very little.
while True:
    sc.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)   
    
    # Checking borders
    if ball.ycor() > 230:#if ball hits top
        ball.sety(230)
        ball.dy *= -1
 
    if ball.ycor() < -230:#if ball hits bottom
        ball.sety(-230)
        ball.dy *= -1
 
    if ball.xcor() > 500:#if ball hits right border
        ball.goto(0, 0)
        ball.dy *= -1
        left_player += 1
        chosen_color=choice(color_list)
        sc.bgcolor(chosen_color)#random color after scoring
        sketch.clear()
        sketch.write("Player1 : {}    Player2 : {}".format(
                      left_player, right_player), align="center",
                      font=("Courier", 24, "normal"))
 
    if ball.xcor() < -500:#if ball hits left border
        ball.goto(0, 0)
        ball.dy *= -1
        right_player += 1
        chosen_color=choice(color_list)
        sc.bgcolor(chosen_color)#random color after scoring
        sketch.clear()
        sketch.write("Player1 : {}    Player2 : {}".format(left_player, right_player), align="center",font=("Courier", 24, "normal"))
 
    # Paddle ball collision
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < right_pad.ycor()+80 and ball.ycor() > right_pad.ycor()-80):
        ball.setx(360)
        ball.dx*=-1
        
    if (ball.xcor()<-360 and ball.xcor()>-370) and (ball.ycor()<left_pad.ycor()+80 and ball.ycor()>left_pad.ycor()-80):
        ball.setx(-360)
        ball.dx*=-1