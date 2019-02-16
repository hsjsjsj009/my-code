from time import *
from tkinter import *
def clock():
    root = Tk()
    days = 0
    hour = 0
    minute = 0
    second = 0
    form = "{}:{}:{}:{}".format(days,hour,minute,second)
    label = Label(root, text=form)
    label.pack(side=TOP)
    while True:
        form = "{}:{}:{}:{}".format(days,hour,minute,second)
        label.config(text=form)
        sleep(1)
        label.update()
        second += 1
        if second == 60 :
            minute += 1
            second = 0
        if minute == 60 :
            hour += 1
            minute = 0
        if hour == 24:
            days += 1
            hour =0
            
        
        
    
        
