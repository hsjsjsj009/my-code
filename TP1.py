from turtle import *
import random

screen= getscreen()
screen.colormode(255)
speed("fast")
screensize(canvwidth=3000, canvheight=3000, bg=None)
hideturtle()
rows = int(screen.numinput("Colorful Chessboard","Enter the number of rows",None,minval=2, maxval=25))
pixel = int(screen.numinput("Colorful Chessboard","Enter the number of square size",None,minval=2, maxval=100))
petals = int(screen.numinput("Colorful Chessboard","Enter the number petals",None,minval=2, maxval=20))
showturtle()
if rows % 2 == 0 :
        x = -((rows)/2)*pixel
        y = ((rows-2)/2)*pixel
        penup()
        goto (x,y)
else :
        x = -((rows+1)/2)*pixel
        y = (((rows+1)-2)/2)*pixel
        penup()
        goto (x,y)
    
for numb in range(rows) :
    for k in range(1,rows+1) :
        r = (random.randint(1,255))
        g = (random.randint(1,255))
        b = (random.randint(1,255))
        color((r,g,b),(r,g,b))
        pendown()
        begin_fill()
        for j in range(4) :
            forward(pixel)
            right(90)
        end_fill()
        penup()
        goto(x+(pixel*k),y)
    y = y - pixel
    goto(x,y)
    
if pixel > 50 :
        goto(0,pixel*0.75*rows)
else :
        goto(0,pixel*rows)
        
setheading(360/petals)
pensize(3)
for i in range(1,petals+1) :
    r = (random.randint(1,255))
    g = (random.randint(1,255))
    b = (random.randint(1,255))
    color((r,g,b),(r,g,b))
    pendown()
    for k in range(20) :
        forward(5)
        right(3)
    right(120)
    for k in range(20) :
        forward(5)
        right(3)
    setheading(360/petals+(360/petals)*i)

penup()
text = "Colorful Chessboard of " + str(rows**2) + " Squares and Flower of " + str(petals) + " Petals"
goto(0,-pixel*(rows))
color("blue")
write(text,align='center',font=('Arial',16,'normal'))
hideturtle()

    


    
