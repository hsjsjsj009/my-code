from tkinter import *

class App(Frame):
    line_color = "black"
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.tempat_canvas = Frame(self)
        self.tempat_canvas.pack(side=BOTTOM)
        self.tempat_warna = Frame(self)
        self.tempat_warna.pack(side=LEFT)
        self.tempat_tombol= Frame(self)
        self.tempat_tombol.pack(side=RIGHT)
        Save = Button(self.tempat_tombol,text="Save",width=5)
        Save.grid(column=0,row=0,sticky=E)
        Red = Button(self.tempat_warna,bg="red",command=self.red,width=2)
        Red.grid(column=0,row=0)
        Green = Button(self.tempat_warna,bg="Green",command=self.green,width=2)
        Green.grid(column=1,row=0)
        Blue = Button(self.tempat_warna,bg="Blue",command=self.blue,width=2)
        Blue.grid(column=2,row=0)
        Black = Button(self.tempat_warna,bg="Black",command=self.black,width=2)
        Black.grid(column=3,row=0)
        Clear= Button(self.tempat_tombol,text="Clear",command=self.clear)
        Clear.grid(column=0,row=1,sticky=E)
        self.place = Canvas(master=self.tempat_canvas,width=200,height=200,bg="white")
        self.place.pack()
        self.place.bind("<Button-1>", self.begin)
        self.place.bind("<Button1-Motion>", self.draw)
    
    def black(self):
        App.line_color="black"
    
    def red(self):
        App.line_color="red"
    
    def green(self):
        App.line_color="green"
    
    def blue(self):
        App.line_color="blue"

    def begin(self,event):
        self.ord_x=event.x
        self.ord_y=event.y

    def draw(self,event):
        new_x=event.x
        new_y=event.y
        self.place.create_line(self.ord_x,self.ord_y,new_x,new_y,fill=App.line_color)
        self.ord_x = new_x
        self.ord_y = new_y

    def clear(self):
        self.place.delete("all")

    def save(self):
        

        



if __name__ == "__main__":
    main = Tk()
    app = App(main)
    main.mainloop()
    
    
            