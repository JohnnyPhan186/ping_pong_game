import turtle
import winsound
wn = turtle.Screen()
pen = turtle.Turtle()


# Display on screen
wn.bgcolor("Pink")
pen.write("PRESS E TO START THE GAME \n OR PRESS ANY KEY TO EXIT or \n CLICK THE CANCEL BUTTON", align="center", font=("Courier", 24, "normal"))
user_input = turtle.textinput('Test to run the while Loop to start the game!','Press e to start the Game!')
pen.clear()
Condition = True

while (Condition):
    if (user_input.lower() == "e"):
        wn = turtle.Screen()  # Game Menu
        wn.title("Welcome to Pong! Modified by Johnny Phan")
        wn.setup(width=900, height=700)
        wn.bgcolor("black")

        pen.clear()
        Player_1_name = turtle.textinput(' ', 'Player 1! Enter your name!: ')
        Player_2_name = turtle.textinput(' ', 'Player 2! Enter your name!: ')
        score_limit = int(turtle.textinput(' ','Set a score limit!: '))





        # wn = turtle.Screen()
        wn.title("Pong MODIFIED by Johnny Phan")
        wn.bgcolor("black")
        wn.setup(width=800,height=600)
        wn.tracer(0)

        # Paddle A
        paddle_a = turtle.Turtle()
        paddle_a.speed(0)
        paddle_a.shape("square")
        paddle_a.color("white")
        paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        paddle_a.penup()
        paddle_a.goto(-350, 0)

        # Paddle B
        paddle_b = turtle.Turtle()
        paddle_b.speed(0)
        paddle_b.shape("square")
        paddle_b.color("white")
        paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        paddle_b.penup()
        paddle_b.goto(350,0)

        # Ball
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("red")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 0.07
        ball.dy = -0.07

        # Score
        score_a = 0
        score_b = 0

        # Pen
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write(Player_1_name + ": 0" + Player_2_name + ": 0", align="center", font=("Courier", 24, "normal"))



        # Function
        def paddle_a_up():
            y = paddle_a.ycor()
            y += 20
            paddle_a.sety(y)


        def paddle_a_down():
            y = paddle_a.ycor()
            y -= 20
            paddle_a.sety(y)


        def paddle_b_up():
            y = paddle_b.ycor()
            y += 20
            paddle_b.sety(y)


        def paddle_b_down():
            y = paddle_b.ycor()
            y -= 20
            paddle_b.sety(y)

        # Paddle
        # Keyboard binding
        wn.listen()
        wn.onkeypress(paddle_a_up, 'w')
        wn.onkeypress(paddle_a_down, 's')
        wn.onkeypress(paddle_b_up, 'Up')
        wn.onkeypress(paddle_b_down, "Down")

        #Paddle restriction

        if paddle_a.ycor() >= 100:
            paddle_a_down()
        if paddle_a.ycor() <= -100:
            paddle_a_up()
        if paddle_b.ycor() >= 100:
            paddle_b_down()
        if paddle_b.ycor() <= -100:
            paddle_b_up()


        #Main game loop
        while (Condition):
            wn.update()

            # Move the ball
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # Border Checking

            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1



            if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1


            if ball.xcor() > 390:
                ball.setx(390)
                ball.dx *= -1
                score_a += 1
                pen.clear()
                pen.write(Player_1_name + ":{}".format(score_a) + Player_2_name + ":{}".format(score_b), align="center",font=("Courier", 24, "normal"))

            if ball.xcor() < -390:
                ball.setx(-390)
                ball.dx *= -1
                score_b += 1
                pen.clear()


                pen.write(Player_1_name + ":{}".format(score_a) + Player_2_name + ":{}".format(score_b), align="center",
                          font=("Courier", 24, "normal"))


            # paddle and ball collisions
            def ball_collisions():


                if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
                    ball.setx(340)
                    ball.dx *= -1
                    winsound.PlaySound("C:\\Users\\DinkleFarts\\Downloads\\quick_fart_x.wav", winsound.SND_ASYNC)

                if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
                    ball.setx(-340)
                    ball.dx *= -1
                    winsound.PlaySound("C:\\Users\\DinkleFarts\\Downloads\\quick_fart_x.wav", winsound.SND_ASYNC)


            ball_collisions()

            #Score limit reacher

            if int(score_a == score_limit):
                pen.clear()
                pen.write("GAMEOVER! " + Player_1_name + " wins!", align="center", font=("Courier", 24, "normal"))
                winsound.PlaySound("C:\\Users\\DinkleFarts\\Downloads\\fanfare_x.wav", winsound.SND_ASYNC) #sound file
                play_again = turtle.textinput(' ', 'Play again? \n Type Yes or No')

                if (play_again.lower() == "yes"):
                    wn.clear()
                    break
                else:
                    Condition = False

            elif int(score_b == score_limit):
                pen.clear()
                pen.write("GAMEOVER! " + Player_2_name + " wins!", align="center", font=("Courier", 24, "normal"))
                winsound.PlaySound("C:\\Users\\DinkleFarts\\Downloads\\fanfare_x.wav",winsound.SND_ASYNC) #sound file
                play_again = turtle.textinput(' ','Play again? \n Type Yes or No')

                if (play_again.lower() == "yes"):
                    wn.clear()
                    break
                else:
                    Condition = False

    else:
        pen.write("Thanks for playing!", align="center", font=("Courier", 24, "normal"))
