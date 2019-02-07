from tkinter import *
from calendar import monthrange

def cal(tahun,bulan):
	month = {1:"Januari", 2:"Februari", 3:"Maret", 4:"April" , 5:"Mei", 6:"Juni",7:"July",8:"Agustus",9:"September",10:"Oktober",11:"November",12:"December"}
	temp_cal=monthrange(tahun,bulan)
	root = Tk()
	root.title("{} {}".format(month[bulan],tahun))
	days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
	for i in range(7):
		label = Label(root,padx=10,text=days[i])
		label.grid(row=0,column=i)
	rows = 1
	colums = temp_cal[0]
	for i in range(temp_cal[1]):
		if colums == 6:
			label = Label(root,padx=10,text=i+1)
			label.grid(row=rows,column=colums)
			rows += 1
			colums = 0
		else :
			label = Label(root,padx=10,text=i+1)
			label.grid(row=rows,column=colums)
			colums += 1

cal(2017,2)
