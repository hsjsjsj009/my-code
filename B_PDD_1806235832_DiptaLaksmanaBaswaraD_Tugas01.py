from turtle import *
from random import *
from math import *

screen= getscreen() #Untuk menampilkan layar
screen.colormode(255) #untuk mensetting colormode menjadi RGB
speed(10.5) #untuk mengatur kecepatan 
title("                                                                                     Colorful Chessboard and Flowers") #untuk title screen
screensize(canvwidth=7000, canvheight=7000, bg=None) #untuk mengatur ukuran canvas
hideturtle() #untuk menyembunyikan turtle
rows = int(screen.numinput("Colorful Chessboard and Flowers","Enter the number of rows",None,minval=2, maxval=25)) #numinput di gunakan untuk input menggunakan dialog box
pixel = int(screen.numinput("Colorful Chessboard and Flowers","Enter the number of square size",None,minval=2, maxval=None)) 
petals = int(screen.numinput("Colorful Chessboard and Flowers","Enter the number petals",None,minval=1, maxval=360))
showturtle() #untuk menunjukkan turtle
penup()
goto (0,250)
pendown()
setheading(360/petals) #untuk mengarahkan turtle sesuai dengan sudut yang diberikan, sudut itu dihitung dari x-axis positif
pensize(3) #untuk mengatur ketebalan garis cetakan turtle
for i in range(1,petals+1) :
        r = (randint(0,255))
        g = (randint(0,255))
        b = (randint(0,255))
        color((r,g,b),(r,g,b))
        pendown()
        circle(100,60) #untuk membuat tali busur
        right(-120)
        circle(100,60)
        setheading(360/petals+(360/petals)*i)
penup()
if rows % 2 == 0 : #untuk mengecek barisnya genap atau ganjil
        x = -((rows)/2)*pixel 
        y = 120-pixel
        goto (x,y) #untuk menempatkan turtle
else :
        x = -((rows+1)/2)*pixel + (pixel//2)
        y = 120-pixel
        goto (x,y)
setheading(90)
pensize(0)
for numb in range(rows) : # loop untuk kolom
    for k in range(1,rows+1) : # lopp untuk baris
        r = (randint(0,255)) #untuk memberi nilai random pada variable
        g = (randint(0,255))
        b = (randint(0,255))
        color((r,g,b),(r,g,b)) #untuk mengaplikasikan nilai nilai rgb menjadi suatu warna isian dan garis
        pendown() #untuk membuat turtle mencetak garis
        begin_fill() # untuk memberi tanda awal permulaan pewarnaan
        for j in range(4) : #loop untuk membuat persegi
            forward(pixel) #untuk membuat turtle bergerak maju
            right(90) #untuk membuat turtle belok sebesar 90 derajat
        end_fill() #untuk memberi tanda akhir pewarnaan
        penup()
        goto(x+(pixel*k),y)
    y = y - pixel
    goto(x,y)
text = "Colorful Chessboard of " + str(rows**2) + " Squares and Flower of " + str(petals) + " Petals"
goto(0,(-pixel*rows)+50)
color("blue")
write(text,align='center',font=('Arial',16,'normal')) #untuk menulis text di canvas
hideturtle()
exitonclick() #untuk memerintahkan agar exit pada saat canvas di klik

    


    
