from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier',15,"bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed('fastest')
        self.goto(x=0, y=250)
        self.color('white')
        self.hideturtle()   
        self.penup()
        self.update_score()
        
        
    
    def update_score(self):
        self.write(f"Score: {self.score} ", False, align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.color('red')
        self.write("GAME OVER", align=ALIGNMENT, font=FONT )
        
    
    def add_point(self):
        self.score += 1
        self.clear()
        self.update_score()