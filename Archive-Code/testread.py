import tkinter
from tkinter import filedialog

def codex(lst):
    global code,excel_file
    open_file = open(lst,"r")
    f_read = open_file.readlines()
    open_file.close()
    stopwords = ["And","br","register","strong","div","using","this","code","body","html"]
    for i in range(30,178,3) :
        table = str.maketrans("</:>",4*" ")
        f_read[i] = f_read[i].translate(table).split()
        for k in f_read[i] :
            if k not in stopwords :
                code.append(k)

def excel_process(lst):
    import openpyxl
    global excel_file,column
    xfile = openpyxl.load_workbook(excel_file)
    sheet = xfile['Lembar1']
    for i in range(len(lst)) :
        sheet[column+str(i+2)] = lst[i]
    xfile.save(excel_file)

root_window = tkinter.Tk()
root_window.withdraw()
nama_file = filedialog.askopenfilenames(title="Choose HTML file")
nama_file = root_window.tk.splitlist(nama_file)
excel_file = filedialog.askopenfilename(title="Choose Excel file")
column = input("Column of the code: ")
code = []
for i in range(len(nama_file)) :
    codex(nama_file[i])

excel_process(code)
    
