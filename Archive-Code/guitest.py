from tkinter import *
root = Tk()
photo = PhotoImage(file='wind.png')
photoLabel = Label(root,image=photo)
photoLabel.pack(side=LEFT)

text1 = Label(root,text="angin",foreground="white",background = "green",pady=100,padx=100,font=("Calibri",50))
text1.pack(side=TOP)

text2 = Label(root,text="angin",foreground="white",background = "blue",pady=100,padx=100,font=("Calibri",50))
text2.pack(side=BOTTOM)

root.mainloop()
