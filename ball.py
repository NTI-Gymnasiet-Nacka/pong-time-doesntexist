from turtle import Turtle

class Ball(Turtle):   
    def __init__(self, positon):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.visible = True

    def moveball(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
        pass
        


