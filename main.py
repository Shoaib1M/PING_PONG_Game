from turtle import Screen, Turtle
import time
screen=Screen()
screen.bgcolor('black')
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.tracer(0)

#paddle 1
paddle=Turtle()
paddle.shape("square")
paddle.penup()
paddle.color("white")
paddle.shapesize(5,1)
paddle.goto(350,0)

#paddle2
paddle2=Turtle()
paddle2.shape("square")
paddle2.penup()
paddle2.color("white")
paddle2.shapesize(5,1)
paddle2.goto(-350,0)

#ball
ball=Turtle()
ball.shape("circle")
ball.penup()
ball.shapesize(1,1)
ball.color("white")

#line
line=Turtle()
line.right(90)
line.color("white")
line.hideturtle()
for i in range(6):
    line.pendown()
    line.forward(40)
    line.penup()
    line.forward(10)
line.goto(0,0)
line.left(180)
for i in range(6):
    line.pendown()
    line.forward(40)
    line.penup()
    line.forward(10)


#points
score_paddle1=0
score_paddle2=0


# Score turtles (defined once, outside the game loop)
score1 = Turtle()
score1.color("white")
score1.hideturtle()
score1.penup()
score1.goto(30, 250)

score2 = Turtle()
score2.color("white")
score2.hideturtle()
score2.penup()
score2.goto(-50, 250)

def update_score():
    score1.clear()
    score1.write(score_paddle1, font=("Arial", 30, "bold"))
    score2.clear()
    score2.write(score_paddle2, font=("Arial", 30, "bold"))

# Call this once at start
update_score()


screen.listen()
x_up=10
y_up=10

def go_up():
    paddle.goto(350,paddle.ycor()+20)

def go_down():
    paddle.goto(350,paddle.ycor()-20)

def go_up2():
    paddle2.goto(-350,paddle2.ycor()+20)

def go_down2():
    paddle2.goto(-350,paddle2.ycor()-20)

def ball_direction():
    global x_up, y_up
    x = ball.xcor()
    y = ball.ycor()
    x += x_up
    y += y_up
    ball.goto(x, y)

def bounce_y():
    global y_up
    y_up*=-1

def bounce_x():
    global x_up
    x_up*=-1

screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")

screen.onkey(go_up2,"w")
screen.onkey(go_down2,"s")


game_status=True

# In game loop:
while game_status:
    time.sleep(0.05)
    screen.update()
    ball_direction()

    if ball.ycor() > 275 or ball.ycor() < -275:
        bounce_y()

    if (ball.xcor() > 320 and ball.distance(paddle) < 50) or (ball.xcor() < -320 and ball.distance(paddle2) < 50):
        bounce_x()

    # Right side missed (point to paddle2)
    if ball.xcor() > 380:
        score_paddle2 += 1
        update_score()
        ball.goto(0, 0)
        bounce_x()

    # Left side missed (point to paddle1)
    if ball.xcor() < -380:
        score_paddle1 += 1
        update_score()
        ball.goto(0, 0)
        bounce_x()

    if score_paddle1 >=10 or score_paddle2 >=10:
        game_status = False
        game_over = Turtle()
        game_over.color("white")
        game_over.penup()
        game_over.hideturtle()
        game_over.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
        game_over.goto(-130, -50)
        if score_paddle1 > score_paddle2:
            game_over.write("Player 1 WON", font=("Arial", 30, "bold"))
        if score_paddle2 > score_paddle1:
            game_over.write("Player 2 WON",font=("Arial", 30, "bold"))



screen.exitonclick()
