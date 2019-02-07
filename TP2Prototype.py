import tkinter
from tkinter import filedialog
from turtle import *
import os
temp = ""
def dimension2 (x,y,pixel,segi) :
            showturtle()
            penup()
            goto(int(x),int(y))
            pendown()
            for i in range(segi) :
                forward(int(pixel))
                right((360/segi))
            penup()

def close() :
    root_window.destroy()
    exitonclick()

def check_error(lst,k) :
    
    try :
            d = int(d)
    except :
            l = True
    l =  False

    test1 = True
    p = 1
    n = k+1
    range = len(lst)
    while p < range  :
        if l :
            ##temp += ("Line {} {} {}\n").format(k,lst[k][0],lst[i][p])
            test1 = False  
            p += 1
    if test1 :
        return True
    else :
        return False

def check_number(d):
        try :
            d = int(d)
        except :
            return True
        return False 

root_window = tkinter.Tk()
button = tkinter.Button(text = "Quit", command=close)
button.pack()
nama_file = filedialog.askopenfilename()
file_read = open(nama_file,"r")
f_read = file_read.readlines()
Screen = getscreen()
Screen.colormode(255)
speed(10.5)
hideturtle()
color(0,0,0)
for i in range(len(f_read)) :
        if i == len(f_read)-1 :
            length = len(f_read[i])
        else :
            length = len(f_read[i]) - 1
        f_read[i] = f_read[i][0:length]
        f_read[i] = f_read[i].split()
        if i == 0 :
            for k in range(len(f_read[i])-1):
                temp += f_read[i][k] +" "
            title(temp + "| " + f_read[i][len(f_read[i])-1])
            temp = "" 
        elif f_read[i][0] == "color" :
                r = int(f_read[i][1])
                g = int(f_read[i][2])
                b = int(f_read[i][3])
                color(r,g,b)
        elif f_read[i][0] == "square" :
                dimension2(f_read[i][1],f_read[i][2],f_read[i][3],4)
        elif f_read[i][0] == "rectangle" :
                showturtle()
                penup()
                goto(int(f_read[i][1]),int(f_read[i][2]))
                pendown()
                for m in range(2) :
                    forward(int(f_read[i][3]))
                    right(90)
                    forward(int(f_read[i][4]))
                    right(90)
                penup()
                
        elif f_read[i][0] == "circle" :
                showturtle()
                penup()
                goto(int(f_read[i][1]),int(f_read[i][2]))
                pendown()
                circle(int(f_read[i][3]))
                penup()
        elif f_read[i][0] == "flower" :
                showturtle()
                penup()
                goto(int(f_read[i][1]),int(f_read[i][2]))
                pendown()
                setheading(360/int(f_read[i][3]))
                for x in range(1,int(f_read[i][3])+1) :
                    circle(int(f_read[i][4]),60)
                    right(-120)
                    circle(int(f_read[i][4]),60)
                    setheading(360/int(f_read[i][3])+(360/int(f_read[i][3])*x))
                penup()
        elif f_read[i][0] == "hexagon" :
                dimension2(f_read[i][1],f_read[i][2],f_read[i][3],6)
        elif f_read[i][0] == "pentagon" :
                dimension2(f_read[i][1],f_read[i][2],f_read[i][3],5)
hideturtle()
exitonclick()


