import turtle

MOVE = 40

class Pong(turtle.Turtle):
    def __init__(self, pos):
        super().__init__()
        self.create_ball(pos)
        self.x_move = 10
        self.y_move = 10

    def create_ball(self, position):
        self.shape('circle')
        # self.setheading(45)
        self.resizemode('user')
        self.turtlesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.color('gray0')
        self.goto(position)

    def bounce_y(self):
        self.y_move *= -1  # reverse the ball's y direction

    def bounce_x(self):
        self.x_move *= -1  # reverse the ball's y direction

    def moving_pong(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # self.forward(35)

    def bounce_off_paddle(self):
        self.forward(50)

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()