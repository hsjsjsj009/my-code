import tkinter
from tkinter import filedialog

root_window = tkinter.Tk()
root_window.withdraw()
nama_file = filedialog.askopenfilename(title="Choose HTML file")
f_read = open(nama_file,"rb")
f_read = f_read.readlines()
