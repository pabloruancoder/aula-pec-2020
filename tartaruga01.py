from turtle import *

def drawqua():
    pendown()
    begin_fill()
    for side in range(3):
        left(45)
        forward(45)
        left(45)
    end_fill()
    penup()

color("WhiteSmoke")
bgcolor("MidnightBlue")

drawqua()
forward(100)
drawtqua()
left(120)
forwqua(150)
drawtri()

hideturtle()
done()
            
