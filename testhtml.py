import tkinter
from tkinter import filedialog

root_window = tkinter.Tk()
root_window.withdraw()
nama_file = filedialog.askopenfilename()
open_file = open(nama_file,"r")
f_read = open_file.readlines()
open_file.close()
stopwords = ["And","br","register","strong","div","using","this","code"]
code = []
for i in range(30,178,3) :
    table = str.maketrans("</:>",4*" ")
    f_read[i] = f_read[i].translate(table).split()
    for k in f_read[i] :
        if k not in stopwords :
            code.append(k)  
    