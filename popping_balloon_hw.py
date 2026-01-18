import turtle
import random
import time

shield=False

#screen
screen=turtle.Screen()
screen.setup(800,600)
screen.bgcolor("light blue")
screen.tracer(0)


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
    global shield
    balloon=turtle.Turtle()
    balloon.shape("circle")
    balloon.color(random.choice(colors))
    x=random.randint(-350,350)
    y=random.randint(200,300)
    balloon.penup()
    balloon.goto(x,y)
    balloon.speed=random.uniform(1,3)
    if random.random() < 0.2: #20% chance to be a black balloon
        balloon.color("black")
        balloon.isBomb=True
    else:
        balloon.isBomb=False

    if random.random()<0.1: 
        balloon.color("blue")
        balloon.isShield=True
    else:
        balloon.isShield=False

    balloons.append(balloon)

def updateScore():
    global score
    score+=10
    pen1.clear()
    pen1.write(f"SCORE:{score}",font=("Arial",16,"bold"))
    pen1.hideturtle()

running=True

def gameOver():
    global running,score
    running=False
    pen2=turtle.Turtle()
    pen2.color("red")
    pen2.write(f"Game Over\nYour Score Was {score}",align="center",font=("Arial",35,"bold"))
    pen2.hideturtle()
    screen.update()
    time.sleep(3)
    screen.bye()

#game variables
gameSpeed=0.02
diffIncrease=0.001
spawnInterval=2
lastSpawnTime=time.time()

while running:
    screen.update()
    currentTime=time.time()
    #spawn balloons at intervals
    if currentTime-lastSpawnTime>spawnInterval:
        spawnBalloon()
        lastSpawnTime=currentTime
    
    #move the balloons
    for balloon in balloons:
        balloonY=balloon.ycor()
        balloonSpeed=balloon.speed
        balloon.sety(balloonY-balloonSpeed)
        if balloon.ycor()<=-300:
            balloons.remove(balloon)
            balloon.hideturtle()
        
        #check for collision with dart

        if dart.distance(balloon)<30:
            
            if balloon.isShield:
                shield=True
                balloons.remove(balloon)
                balloon.hideturtle()

            elif balloon.isBomb and shield==False:
                gameOver()

            elif balloon.isBomb and shield==True:
                balloons.remove(balloon)
                balloon.hideturtle()
                shield=False
                
            else:
                updateScore()
                balloons.remove(balloon)
                balloon.hideturtle()

    #prevent negative gamespeed
    gameSpeed=max(0.005,gameSpeed-diffIncrease)
    #prevent too frequent spawn of balloons
    spawnInterval=max(0.5,spawnInterval-0.0005)
    time.sleep(gameSpeed)






screen.mainloop()
