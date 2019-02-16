import tkinter
from tkinter import filedialog
from tkinter import messagebox
from turtle import *
temp_nama = ""
#fungsi untuk membuat polygon
def dimension2 (x,y,pixel,segi) : 
            showturtle()
            penup()
            goto(int(x),int(y))
            pendown()
            sudut = 360/segi
            for i in range(segi) :
                forward(int(pixel))
                right(sudut)
            penup()
#fungsi untuk menutup aplikasi
def close() :
    root_window.destroy()
    exitonclick()

#fungsi untuk mengecek data merupakan angka atau tidak
def check_number(d):
        try :
            d = int(d)
        except :
            return True
        return False

#fungsi untuk mengecek error pada input file
def check_error(test,k) :
    global temp_nama
    global check_number
    try :
        test1 = True
        p = 1
        shape = ["square","pentagon","hexagon","circle","octagon"]
        if test[0] == "color" :
                while p < 4 :
                    d = test[p]
                    if check_number(test[p]) :
                        temp_nama += ("Line {} {} {} No alphabet allowed\n").format(k+1,test[0],test[p])
                        test1 = False 
                    elif  not ((int(test[p])<256) and (int(test[p])>-1)) :#untuk mnegecek range r g b
                        temp_nama += ("Line {} {} {} Out of range\n").format(k+1,test[0],test[p])
                        test1 = False
                    p += 1
        elif test[0] in shape :
            while p < 4 :
                    d = test[p] 
                    if check_number(test[p]) :
                        temp_nama += ("Line {} {} {} No alphabet allowed\n").format(k+1,test[0],test[p])
                        test1 = False
                    p += 1
        elif test[0] == "rectangle" :
            while p < 5 :
                    d=test[p] 
                    if check_number(test[p]) :
                        temp_nama += ("Line {} {} {} No alphabet allowed\n").format(k+1,test[0],test[p])
                        test1 = False
                    p += 1
        return test1
    except :
        temp_nama += ("Line {} {} Not enough data\n").format(k+1,test[0])
        return False

#fungsi untuk mengecek data merupakan npm atau bukan
def check_npm(lst) :
    condition  = 0
    for i in lst[-1] :
        if not check_number(i) :
            condition += 1
    if condition >= (len(lst[-1])//2) :
        return True
    else :
        return False
#untuk memanggil fungsi Tk
root_window = tkinter.Tk()
root_window.withdraw()
#proses utama
def main() :
    global temp_nama
    temp_judul=""
    try : 
        #untuk membuka filedialog
        nama_file = filedialog.askopenfilename()
        print("Selected file : %s" %nama_file)
        open_file = open(nama_file,"r")
        f_read = open_file.readlines()
        open_file.close()
        if len(f_read)>0 :
            Screen = getscreen()
            Screen.colormode(255)
            speed(10.5)
            hideturtle()
            color(0,0,0)
            #proses slicing dan penentuan perintah
            for i in range(len(f_read)) :
                    if i == len(f_read)-1 :
                        length = len(f_read[i])
                    else :
                        length = len(f_read[i]) - 1
                    f_read[i] = f_read[i][0:length].split()
                    #untuk menentukan perintah
                    if not len(f_read[i]) == 0:
                        if i == 0 : #untuk menuliskan nama title
                            if check_npm(f_read[i]) :
                                if check_number(f_read[i][-1]) :
                                    for k in range(len(f_read[i])-1):
                                        temp_judul += f_read[i][k] +" "
                                    title(temp_judul + "| " + "NPM Error")
                                    temp_nama += ("Line 1 {} No alphabet allowed\n").format(f_read[i][-1])
                                else :    
                                    for k in range(len(f_read[i])-1):
                                        temp_judul += f_read[i][k] +" "
                                    title(temp_judul + "| " + f_read[i][len(f_read[i])-1])
                                    temp_nama += ""
                            else :
                                if len(f_read[i]) < 2 :
                                    title(f_read[i][0] +" | " +"No Npm")
                                else :
                                    for k in range(len(f_read[i])):
                                            temp_judul += f_read[i][k] +" "
                                    title(temp_judul + "| " + "No Npm")
                                temp_nama += ("Line 1 No Npm\n")
                        elif f_read[i][0].lower() == "color" :
                            if check_error(f_read[i],i) :  
                                r = int(f_read[i][1])
                                g = int(f_read[i][2])
                                b = int(f_read[i][3])
                                color(r,g,b)
                        elif f_read[i][0].lower() == "square" : 
                            if check_error(f_read[i],i) :
                                dimension2(f_read[i][1],f_read[i][2],f_read[i][3],4)
                        elif f_read[i][0].lower() == "rectangle" : 
                            if check_error(f_read[i],i) :
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
                        elif f_read[i][0].lower() == "circle" :
                            if check_error(f_read[i],i) :
                                showturtle()
                                penup()
                                goto(int(f_read[i][1]),int(f_read[i][2]))
                                pendown()
                                circle(int(f_read[i][3]))
                                penup()
                        elif f_read[i][0].lower() == "octagon" :
                            if check_error(f_read[i],i):
                                dimension2(f_read[i][1],f_read[i][2],f_read[i][3],8)
                        elif f_read[i][0].lower() == "hexagon" : 
                            if check_error(f_read[i],i): 
                                dimension2(f_read[i][1],f_read[i][2],f_read[i][3],6)
                        elif f_read[i][0].lower() == "pentagon" : 
                            if check_error(f_read[i],i) :
                                dimension2(f_read[i][1],f_read[i][2],f_read[i][3],5)
                        else :
                            temp_nama += "Line {} {} No shape in database\n".format(i+1,f_read[i][0])
                    else:
                        temp_nama += "Line {} No data\n".format(i+1)
            hideturtle()
            #untuk mencetak error
            if len(temp_nama) == 0 and len(f_read) > 1:
                if messagebox.showinfo("Info","No Error") == "ok" :
                    close()
                exitonclick()
            elif len(temp_nama) != 0 :
                if messagebox.showerror("Error","Error in :\n" + temp_nama) == "ok" :
                    close()
                exitonclick()
            elif len(f_read) == 1 :
                if messagebox.showerror("Error",temp_nama) == "ok" :
                    close()
                exitonclick()
        elif len(f_read) == 0 :
            if messagebox.showerror("Error","No data") == "ok" :
                main()
    except (UnicodeDecodeError,ValueError) : #untuk respon error file bukan .txt
        if messagebox.showerror("Error","Only support .txt file") == "ok" :    
            main()
    except FileNotFoundError : #untuk respon tidak ada input
        if messagebox.showerror ("Error","No input file") == "ok" :
            close()
main()


