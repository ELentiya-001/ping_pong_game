import turtle
import paddle
import ball
import scoreboard
import time

WIDTH = 800
HEIGHT = 600
WINNING_SCORE = 4
STARTING_POSITIONS = ((int((WIDTH / 2) - 30), 0), (-int((WIDTH / 2) - 30), 0))
# print(STARTING_POSITIONS)
game_is_on = True

# screen settings
screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title('PONG GAME')
screen.bgcolor('PeachPuff')
screen.tracer(0)

r_paddle = paddle.Paddle(STARTING_POSITIONS[0])
l_paddle = paddle.Paddle(STARTING_POSITIONS[1])

screen.listen()
screen.onkey(r_paddle.paddle_up, 'Up')
screen.onkey(r_paddle.paddle_down, 'Down')
screen.onkey(l_paddle.paddle_up, 'w')
screen.onkey(l_paddle.paddle_down, 's')

ball = ball.Pong((0, 0))
scoreboard = scoreboard.ScoreBoard()

while game_is_on:
    time.sleep(0.04)
    screen.update()
    ball.moving_pong()

    # DETECTING COLLISION WITH TOP AND BOTTOM WALLS
    if ball.ycor() >= int(HEIGHT / 2) - 10 or ball.ycor() <= -int(HEIGHT / 2) + 10:
        # COLLISION WITH TOP OR BOTTOM WALL
        ball.bounce_y()
        # print(f" TIME TO BOUNCE {ball.y_move}")

    # DETECT COLLISION WITH ANY OF THE TWO PADDLES
    if ball.xcor() >= int(WIDTH / 2) - 40 or ball.xcor() <= -int(WIDTH / 2) + 40:
        if ball.distance(r_paddle) <= 50 or ball.distance(l_paddle) <= 50:
            # THE BALL HAS COLLIDED WITH THE PADDLE
            ball.bounce_x()
            if ball.distance(r_paddle) <= 50:
                ball.setheading(225)
                ball.bounce_off_paddle()
            else:
                ball.setheading(45)
                ball.bounce_off_paddle()
            # print(f" TIME TO BOUNCE {ball.x_move}")
        elif ball.xcor() >= int(WIDTH / 2) - 20 or ball.xcor() <= -int(WIDTH / 2) + 20:
            # print("PADDLE MISSED THE BALL!")
            if ball.xcor() >= int(WIDTH / 2) - 20:
                scoreboard.l_score += 1
                scoreboard.update_score()
                ball.reset_position()
            else:
                scoreboard.r_score += 1
                scoreboard.update_score()
                ball.reset_position()


    if scoreboard.l_score == WINNING_SCORE or scoreboard.r_score == WINNING_SCORE:
        scoreboard.game_over()
        game_is_on = False
print(f"LEFT SCORE {scoreboard.l_score} RIGHT SCORE {scoreboard.r_score}\n")
screen.exitonclick()
