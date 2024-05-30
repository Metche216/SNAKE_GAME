from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier',15,"bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.speed('fastest')
        self.goto(x=0, y=250)
        self.color('white')
        self.hideturtle()   
        self.penup()
        self.update_score()
        
        
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()
        
    
    def add_point(self):
        self.score += 1
        self.update_score()