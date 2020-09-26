from turtle import*

def drawPlanet(circuloSize, circuloColor):
    color(circuloColor)
    pendown()
    begin_fill()
    for side in range(8):
        left(45)
        forward(circuloSize)
    end_fill()
    penup()


bgcolor("MidnightBlue")
drawPlanet(50, "Red")
forward(100)
drawPlanet(30, "White")
left(120)
forward(150)
drawPlanet(70, "Green")

hideturtle()
done()
