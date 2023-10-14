# CHOICES = (
#     (0.00, 300.00), (0.00, 280.00), (0.00, 260.00), (0.00, 240.00), (0.00, 220.00), (0.00, 200.00), (0.00, 180.00),
#     (0.00, 160.00), (0.00, 140.00), (0.00, 120.00), (0.00, 100.00), (0.00, 80.00), (0.00, 60.00), (0.00, 40.00),
#     (0.00, 20.00), (0.00, 0.00), (0.00, -20.00), (0.00, -40.00), (0.00, -60.00), (0.00, -80.00), (0.00, -100.00),
#     (0.00, -120.00), (0.00, -140.00), (0.00, -160.00), (0.00, -180.00), (0.00, -200.00), (0.00, -220.00),
#     (0.00, -240.00), (0.00, -260.00), (0.00, -280.00))

import turtle

class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('navy')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f'{self.l_score}', move=False, align='center', font=('Courier', 56, 'normal'))
        self.goto(100, 200)
        self.write(arg=f'{self.r_score}', move=False, align='center', font=('Courier', 56, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.color('gray0')
        self.write(arg=f'GAME OVER!', move=False, align='center', font=('Courier', 56, 'normal'))