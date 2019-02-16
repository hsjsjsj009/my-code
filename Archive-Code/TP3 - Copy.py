from tkinter import *

root = Tk()
condition = 0
class entry:
    global root
    global label_bot
    def __init__(self,width,font,side):
        self.entry = Entry(root,width=width,font=font,justify=side)
        self.entry.pack()
    def check(self):
        if len(self.data) == 12 :
            return True
        return False 
    def num(self):
        try:
            x = int(self.data)
        except :
            return False
        return True
    def getdata_input(self):
        global label_bot
        self.data = self.entry.get()
        if self.check() and self.num():
            label_bot.config(text="Code Accepted")
            label_bot.update()
            return True
        elif not self.check():
            label_bot.config(text="Not 12 digit")
            label_bot.update()
            return False
        elif not self.num():
            label_bot.config(text="Not numerik")
            label_bot.update()
            return False
    def getdata_output(self):
        if ".eps" not in self.entry.get():
            self.data = self.entry.get() + ".eps"
        else :
            self.data = self.entry.get()
        return self.data
    def __repr__(self):
        return self.data

class canvas:
    def create(self,root,width,height,background):
        self.canv = Canvas(root,width=width,height=height,background = background)
    def export(self,address,height,width):
        self.canv.postscript(file=address,colormode="color",height=height,width=width)
    
class Barcode(canvas):
    global condition
    g =("0100111","0110011","0011011","0100001","0011101","0111001","0000101","0010001","0001001","0010111")
    FirstGroup = ("LLLLLL","LLGLGG","LLGGLG","LLGGGL","LGLLGG","LGGLLG","LGGGLL","LGLGLG","LGLGGL","LGGLGL")
    def __init__(self,number,output):
        self.left_binary = str()
        self.right_binary = str()
        self.final_code = str()
        self.number = str(number)
        self.output = output

    def checksum(self):
        temp = list(self.number)
        a = [i for i in temp[1:13:2]]
        b = [i for i in temp[:13:2]]
        pass1 = int()
        pass2 = int()
        for i in a:
            pass1 += int(i)
        for i in b:
            pass2 += int(i)
        pass1 *= 3
        pass2 += pass1
        if pass2%10 == 0 :
            return str(0)
        else :
            return str((((pass2//10)+1)*10)-pass2)

    def start(self):
        leftcode = Barcode.FirstGroup[int(self.number[0])]
        rightcode = "RRRRRR"
        self.barcode = self.number + self.checksum()
        counter = 1
        for i in leftcode:
            if i == "L":
                self.left_binary += self.L(int(self.barcode[counter]))
                counter += 1
            elif i == "G":
                self.left_binary += self.G(int(self.barcode[counter]))
                counter += 1
        for i in rightcode:
            self.right_binary += self.R(int(self.barcode[counter]))
            counter += 1
        self.final_code = "323"+self.left_binary+"23232"+self.right_binary+"323"
    
    def create_new(self,barcode,address):
        self.left_binary = str()
        self.right_binary = str()
        self.final_code = str()
        self.number = str(barcode)
        self.output = address

    def draw(self):
        self.start()
        counter = 0
        if condition == 0:
            self.canv.create_text(205,20,fill="black",font="Calibri 14 bold",text="EAN-13 Barcode :")
            for i in self.final_code:
                if i == "3":
                    self.canv.create_rectangle(65+counter,50,68+counter,150,fill="blue",outline="")
                    counter += 3
                elif i == "2":
                    self.canv.create_rectangle(65+counter,50,68+counter,150,fill="white",outline="")
                    counter += 3
                elif i == "1":
                    self.canv.create_rectangle(65+counter,50,68+counter,130,fill="black",outline="")
                    counter += 3
                elif i == "0":
                    self.canv.create_rectangle(65+counter,50,68+counter,130,fill="white",outline="")
                    counter += 3
            self.canv.create_text(58,140,fill="black",font="Calibri 14 bold",text=str(self.barcode[0]))
            counter = 0
            for i in range(1,len(self.barcode)):
                if i >= 7:
                    self.canv.create_text(90+counter,140,fill="black",font="Calibri 14 bold",text=str(self.barcode[i]))
                    counter += 22
                else :
                    self.canv.create_text(83+counter,140,fill="black",font="Calibri 14 bold",text=str(self.barcode[i]))
                    counter += 22
            self.canv.create_text(205,180,fill="blue",font="Calibri 14 bold",text="Check Digit : {}".format(self.barcode[-1]))
            self.canv.pack()
        else :
            self.canv.delete("all")
            self.canv.create_text(205,20,fill="black",font="Calibri 14 bold",text="EAN-13 Barcode :")
            self.canv.update()
            for i in self.final_code:
                if i == "3":
                    self.canv.create_rectangle(65+counter,50,68+counter,150,fill="blue",outline="")
                    self.canv.update()
                    counter += 3
                elif i == "2":
                    self.canv.create_rectangle(65+counter,50,68+counter,150,fill="white",outline="")
                    self.canv.update()
                    counter += 3
                elif i == "1":
                    self.canv.create_rectangle(65+counter,50,68+counter,130,fill="black",outline="")
                    self.canv.update()
                    counter += 3
                elif i == "0":
                    self.canv.create_rectangle(65+counter,50,68+counter,130,fill="white",outline="")
                    self.canv.update()
                    counter += 3
            self.canv.create_text(58,140,fill="black",font="Calibri 14 bold",text=str(self.barcode[0]))
            self.canv.update()
            counter = 0
            for i in range(1,len(self.barcode)):
                if i >= 7:
                    self.canv.create_text(90+counter,140,fill="black",font="Calibri 14 bold",text=str(self.barcode[i]))
                    self.canv.update()
                    counter += 22
                else :
                    self.canv.create_text(83+counter,140,fill="black",font="Calibri 14 bold",text=str(self.barcode[i]))
                    self.canv.update()
                    counter += 22
            self.canv.create_text(205,180,fill="blue",font="Calibri 14 bold",text="Check Digit : {}".format(self.barcode[-1]))
            self.canv.update()

    def L(self,number):
        temp = list(Barcode.g[number])
        temp.reverse()
        for i in range(len(temp)):
            if int(temp[i]):
                temp[i] = "0"
            else :
                temp[i] = "1"
        return "".join(temp)

    def G(self,number):
        return Barcode.g[number]

    def R(self,number):
        return Barcode.g[number][::-1]

def process(event):
    global condition,root,a
    if condition == 0:
        if input_code.getdata_input() :
            address_file = output_file.getdata_output()
            barcode = input_code
            a = Barcode(barcode,address_file)
            a.create(root,400,210,"white")
            a.draw()
            a.export(a.output,width=400,height=210)
            condition = 1
    else :
        if input_code.getdata_input() :
            address_file = output_file.getdata_output()
            barcode = input_code
            a.create_new(barcode,address_file)
            a.draw()
            a.export(a.output,width=400,height=210)

def main():
    global label_bot, root, input_code, output_file
    root.title("EAN-13 [by Dipta Laksmana Baswara]")
    label_top = Label(root,text="Save barcode to PS file [eg:EAN13.eps]:",font = "Calibri 14",width=50)
    label_top.pack()
    output_file = entry(30,"Calibri 14","center")
    label_mid = Label(root,text="Enter code (first 12 decimal digits):",font = "Calibri 14",width=50)
    label_mid.pack()
    input_code = entry(30,"Calibri 14","center")
    label_bot = Label(root,text="Hello",font = "Calibri 14",width=50)
    label_bot.pack()
    root.bind("<Return>",process)
    root.mainloop()

if __name__ == "__main__":
    main()
    
