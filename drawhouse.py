#Draw_home_using_turtle_in_python🐢 
import turtle as t
import random
tim=t.Turtle()
t.colormode(255)
tim.pensize(5)
tim.speed(10)
tim.hideturtle()
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
def triangle():
   tim.color(random_color())
   tim.left(120)
   tim.forward(100)
   tim.right(240)
   tim.forward(100)
   tim.right(240)
   tim.forward(100)
   tim.left(120)
   tim.forward(100)
def rect():
    triangle()
    tim.color(random_color())
    tim.right(120)
    tim.forward(200)
    tim.right(90)
    tim.forward(85)
    tim.right(90)
    tim.forward(150)
    tim.penup()
    tim.forward(100)
def sqa():
    rect()
    tim.color(random_color())
    tim.pendown()
    tim.right(270)
    tim.forward(150)
    tim.left(90)
    tim.forward(250)
    tim.left(90)
    tim.forward(150)
    tim.left(90)
    tim.forward(150)
    tim.color(random_color())
    tim.left(90)
    tim.forward(150)
def door():
    sqa()
    tim.right(90)
    tim.penup()
    tim.color(random_color())
    tim.forward(30)
    tim.pendown()
    tim.right(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(30)
    tim.left(90)
    tim.forward(50)
    
door()

    
