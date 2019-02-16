from tkinter import *
from calendar import *
def cal(tahun,bulan):    
    temp_cal=monthrange(tahun,bulan)
    root = Tk()
    days= ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i in range(7):
        label = Label(root,padx=15,text=days[i])
        label.grid(row=0,column=i)
    rows = 1
    colums = temp_cal[0]
    for i in range(temp_cal[1]):
        if columns == 6:
            label = Label(root,padx=15,text=i+1)
            label.grid(row=rows,columns=columns)
            columns = 0
            rows += 1
        else :
            label = Label(root,padx=15,text=i+1)
            label.grid(row=rows,columns=columns)
            columns += 1

cal(2017,2)
