from tkinter import * #import seluruh fungsi di 

class entry(Entry): #class untuk memproses data entry
    def __init__(self,width,font,side,root): #fungsi inisiasi object
        super().__init__(root,width=width,font=font,justify=side) #inisiasi ke super kelas
        self.pack()

    def getdata_input(self,root): #fungsi untuk memanggil dan mengecek input barcode
        self.data = self.get()
        if len(self.data) > 0:
            if self.data.isdigit() and len(self.data) == 12:
                root.label_bot.config(text="Code Accepted")
                root.label_bot.update()
                return True
            elif not self.data.isdigit():
                root.label_bot.config(text="Not Numerik")
                root.label_bot.update()
                return False
            elif not len(self.data) == 12:
                root.label_bot.config(text="Not 12 Digit")
                root.label_bot.update()
                return False
        else :
            root.label_bot.config(text="No Data")
            root.label_bot.update()
    def getdata_output(self,root): #fungsi untuk mengelola outputan file
        if len(self.get()) > 0:
            if ".eps" not in self.get():
                root.label_bot.config(text="Wrong File Extension")
                root.label_bot.update()
                return False
            else :
                self.data = self.get()
            return True
        else :
            root.label_bot.config(text="No file")
            root.label_bot.update()
            return False
    
class Barcode(Canvas): #class untuk membuat barcode 
    g =("0100111","0110011","0011011","0100001","0011101","0111001","0000101","0010001","0001001","0010111")
    FirstGroup = ("LLLLLL","LLGLGG","LLGGLG","LLGGGL","LGLLGG","LGGLLG","LGGGLL","LGLGLG","LGLGGL","LGGLGL")
    def __init__(self,root,colormode,width,height,background): #untuk inisiasi object barcode
        super().__init__(root,width=width,height=height,background=background) #inisiasi super kelas
        self.left_binary = str()
        self.right_binary = str()
        self.final_code = str()
        self.width= width
        self.height= height
        self.colormode= colormode

    def checksum(self): #memproses checksum
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

    def start(self): #memulai pembentukan kode barcode menjadi binary
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
    
    def create_new(self,barcode,address): #membentuk barcode baru
        self.left_binary = str()
        self.right_binary = str()
        self.final_code = str()
        self.number = str(barcode)
        self.output = address

    def draw(self): #menggambar barcode
            self.start()
            counter = 0
            self.delete("all")
            self.create_text(205,20,fill="black",font="Calibri 14 bold",text="EAN-13 Barcode :")
            for i in self.final_code:
                if i == "3":
                    self.create_rectangle(65+counter,50,68+counter,150,fill="blue",outline="")
                    counter += 3
                elif i == "2":
                    self.create_rectangle(65+counter,50,68+counter,150,fill="white",outline="")
                    counter += 3
                elif i == "1":
                    self.create_rectangle(65+counter,50,68+counter,130,fill="black",outline="")
                    counter += 3
                elif i == "0":
                    self.create_rectangle(65+counter,50,68+counter,130,fill="white",outline="")
                    counter += 3
            self.create_text(58,140,fill="black",font="Calibri 14 bold",text=str(self.barcode[0]))
            counter = 0
            for i in range(1,len(self.barcode)):
                if i >= 7:
                    self.create_text(90+counter,140,fill="black",font="Calibri 14 bold",text=str(self.barcode[i]))
                    counter += 22
                else :
                    self.create_text(83+counter,140,fill="black",font="Calibri 14 bold",text=str(self.barcode[i]))
                    counter += 22
            self.create_text(205,180,fill="blue",font="Calibri 14 bold",text="Check Digit : {}".format(self.barcode[-1]))
            self.pack()
            self.postscript(file=self.output,height=self.height,width=self.width,colormode=self.colormode)

    def L(self,number): #fungsi untuk binary L
        temp = list(Barcode.g[number])
        temp.reverse()
        for i in range(len(temp)):
            if int(temp[i]):
                temp[i] = "0"
            else :
                temp[i] = "1"
        return "".join(temp)

    def G(self,number):#fungsi untuk binary G
        return Barcode.g[number]

    def R(self,number):#fungsi untuk binary R
        return Barcode.g[number][::-1]

class App(Frame): #class untuk tempat entry dan label
    def __init__(self,root,side=None): #fungsi inisiasi dan membentuk gui
        super().__init__(root)
        self.pack(side=side)
        label_top = Label(self,text="Save barcode to PS file [eg:EAN13.eps]:",font = "Calibri 14",width=50)
        label_top.pack()
        self.output_file = entry(30,"Calibri 14","center",self)
        label_mid = Label(self,text="Enter code (first 12 decimal digits):",font = "Calibri 14",width=50)
        label_mid.pack()
        self.input_code = entry(30,"Calibri 14","center",self)
        self.input_code.pack()
        self.label_bot = Label(self,text="Hello",font = "Calibri 14",width=50)
        self.label_bot.pack()
        self.output_file.bind("<Return>",self.process)
        self.input_code.bind("<Return>",self.process)
        self.a = Barcode(root=self,colormode="color",width=400,height=210,background="white")

    def process(self,event): #fungsi melaksanakan event based gui
            if self.output_file.getdata_output(self) and self.input_code.getdata_input(self) :
                    address_file = self.output_file.data
                    barcode = self.input_code.data
                    self.a.create_new(barcode,address_file)
                    self.a.draw()

def main(): #fungsi main
    root = Tk()
    root.title("EAN-13 [by Dipta Laksmana Baswara]")
    app = App(root)
    root.mainloop()

if __name__ == "__main__": #pengecekan top level module
    main()
    
