import turtle as t
import os


player_a_score = 0
player_b_score = 0

win = t.Screen()   
win.title("Ping-Pong Game") 
win.bgcolor('black')   
win.setup(width=800,height=600) 
win.tracer(0)   



paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('red')
paddle_left.shapesize(stretch_wid=5,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)



paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
paddle_right.color('red')
paddle_right.penup()
paddle_right.goto(350,0)



ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0,0)
ball_dx = 1.5   
ball_dy = 1.5



pen = t.Turtle()
pen.speed(0)
pen.color('skyblue')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0            Player B: 0 ",align="center",font=('Monaco',24,"normal"))




def paddle_left_up():
    y = paddle_left.ycor()
    y = y + 15
    paddle_left.sety(y)


def paddle_left_down():
    y = paddle_left.ycor()
    y = y - 15
    paddle_left.sety(y)



def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 15
    paddle_right.sety(y)



def paddle_right_down():
    y = paddle_right.ycor()
    y = y - 15
    paddle_right.sety(y)



win.listen()
win.onkeypress(paddle_left_up,"u")
win.onkeypress(paddle_left_down,"e")
win.onkeypress(paddle_right_up,"Up")
win.onkeypress(paddle_right_down,"Down")






while True:

   
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

   

    if ball.ycor() > 290:  
        ball.sety(290)
        ball_dy = ball_dy * -1
        
    
    if ball.ycor() < -290: 
        ball.sety(-290)
        ball_dy = ball_dy * -1
        

    if ball.xcor() > 390:   
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")



    if(ball.xcor()) < -390: 
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score,player_b_score),align="center",font=('Monaco',24,"normal"))
        os.system("afplay wallhit.wav&")


    

    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
        ball.setx(-340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")
