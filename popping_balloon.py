import turtle
import random
import time


#screen
screen=turtle.Screen()
screen.setup(800,600)
screen.bgcolor("light blue")
#screen.tracer(0)


#dart
dart=turtle.Turtle()
dart.color("blue")
dart.shape("triangle")
dart.setheading(90)
dart.penup()
dart.goto(0,-250)


#score display
score=0
pen1=turtle.Turtle()
pen1.color("black")
pen1.penup()
pen1.goto(-380,250)
pen1.write(f"SCORE:{score}",font=("Arial",16,"bold"))
pen1.hideturtle()

#add movement to the dart
def moveLeft():
    x=dart.xcor()
    dart.setx(x-20)

def moveRight():
    x=dart.xcor()
    dart.setx(x+20) 

screen.listen()
screen.onkey(moveLeft,"a")
screen.onkey(moveRight,"d")                                              

#balloons setup
balloons=[]
colors=["yellow","red","green","purple"]

def spawnBalloon():
    balloon=turtle.Turtle()
    balloon.shape("circle")
    balloon.color(random.choice(colors))

screen.mainloop()
