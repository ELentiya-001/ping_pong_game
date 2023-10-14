import turtle

MOVE = 40
class Paddle(turtle.Turtle):
    def __init__(self, pos):
        super().__init__()
        self.create_paddle(pos)

    def create_paddle(self, position):
        self.shape('square')
        self.setheading(90)
        self.resizemode('user')
        self.turtlesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.color('gray0')
        self.goto(position)

    def paddle_up(self):
        self.forward(MOVE)

    def paddle_down(self):
        self.backward(MOVE)
