from tkinter import * #untuk import module tkinter
from tkinter.messagebox import * # untuk import module messagebox
nasabah = {} #uuntuk menampung nama nasabah
test = 1 # untuk indikator error
class Akun: #class untuk mengelola akun
    global root,label
    def __init__(self, pemilik, saldo): #fungsi untuk inisiasi class
        self.pemilik = pemilik
        self.saldo = int(saldo)

    def deposit(self, nominal): #fungsi untuk deposit
        self.saldo += nominal
        label.config(text="Saldo sekarang {}!".format(self.saldo))
        label.update()

    def tarik(self, nominal): #fungsi untuk tarik tunai
        if self.saldo >= nominal:
            self.saldo -= nominal
            label.config(text="Saldo sekarang {}!".format(self.saldo))
            label.update()
        else: #kondisi saldo tidak cukup
            label.config(text="Saldo Tidak Cukup!")
            label.update()

class Gold(Akun): #class akun gold
    global root,label
    def transfer(self,tujuan,nominal): #fungsi untuk mentransfer
        if self.saldo >= (nominal + 50000) :
            self.saldo -= nominal + 50000
            tujuan.saldo += nominal
            label.config(text="Saldo sekarang {}!".format(self.saldo))
            label.update()
        else: #kondisi saldo kurang
            label.config(text="Saldo Tidak Cukup!")
            label.update()
class Silver(Akun): #class akun gold
    global root,label
    def transfer(self,tujuan,nominal):#fungsi untuk mentransfer
        if self.saldo >= (nominal + 10000):
            self.saldo-= nominal + 10000
            tujuan.saldo += nominal
            label.config(text="Saldo sekarang {}!".format(self.saldo))
            label.update()
        else:#kondisi saldo kurang
            label.config(text="Saldo Tidak Cukup!")
            label.update()

def deposit(): #fungsi deposit button
    global nasabah,akun_entry,nominal_entry,label
    nama = str(akun_entry.get()).lower()
    if nama not in nasabah:
            label.config(text="Akun Invalid!")
            label.update()
    else :
        nominal = int(nominal_entry.get())
        nasabah[nama].deposit(nominal)
def tarik(): #fungsi tarik button
    global nasabah,akun_entry,nominal_entry,label
    nama = str(akun_entry.get()).lower()
    if nama not in nasabah:
            label.config(text="Akun Invalid!")
            label.update()
    else:
        nominal = int(nominal_entry.get())
        nasabah[nama].tarik(nominal)
def transfer():  #fungsi transfer button
    global nasabah,akun_entry,nominal_entry,label,tujuan_entry
    nama = str(akun_entry.get()).lower()
    nama_tujuan = str(tujuan_entry.get()).lower()
    if nama not in nasabah: #pengecekan keanggotaan
            label.config(text="Akun Invalid!")
            label.update()
    elif nama_tujuan not in nasabah: #pengecekan keanggotaan
            label.config(text="Akun Tujuan Invalid!")
            label.update()
    else: #Pengecekan tipe akun
        if type(nasabah[nama]) == type(nasabah[nama_tujuan]):
            nominal = int(nominal_entry.get())
            nasabah[nama].transfer(nasabah[nama_tujuan],nominal)
        else :
            label.config(text="Tipe akun berbeda")
            label.update()

try: #pengecekan error pengambilan file
    read_file = open("listnasabah.txt","r")
    read_file = read_file.readlines()
    for baris in read_file:
        baris = baris.split()
        if baris[0] == "SILVER":
            nasabah[baris[1].lower()] = Silver(baris[1].lower(),baris[2])
        elif baris[0] == "GOLD":
            nasabah[baris[1].lower()] = Gold(baris[1].lower(),baris[2])
        else :
            error = "Data nasabah salah"
            test = 0
except IndexError: #error kurang data
    error = "Data nasabah kurang"
    test = 0
except: #error file tidak ada
    error = "File nasabah tidak ditemukan"
    test = 0

root = Tk()
root.configure(background="white")
if not test: #jika ada error
    if showerror("Virtual Bank",error) == "ok":
        root.destroy()
else : #proses utama
    root.title("Virtual Bank")
    label = Label(root,text="Selamat Datang!!",font=("Times New Roman",20),width=18,height=2,foreground="black",background="white")
    label.grid(row=0,column=0,columnspan=3)

    akun = Label(root,text="Akun:",font=("Times New Roman",20),width=18,height=2,foreground="black",background="white")
    akun.grid(row=1,column=0)

    akun_entry = Entry(root,width=25,font=("Times New Roman",20),foreground="white",background="black")
    akun_entry.grid(row=1,column=1)

    tujuan = Label(root,text="Tujuan:",font=("Times New Roman",20),width=18,height=2,foreground="black",background="white")
    tujuan.grid(row=2,column=0)

    tujuan_entry = Entry(root,width=25,font=("Times New Roman",20),foreground="white",background="black")
    tujuan_entry.grid(row=2,column=1)

    nominal = Label(root,text="Nominal:",font=("Times New Roman",20),width=18,height = 2,foreground="black",background="white")
    nominal.grid(row=3,column=0)

    nominal_entry = Entry(root,width=25,font=("Times New Roman",20),foreground="white",background="black")
    nominal_entry.grid(row=3,column=1)

    deposit = Button(root,text="Deposit",font=("Times New Roman",20),command=deposit,width=18,height=2,relief=RAISED,foreground="white",background="green")
    deposit.grid(row=4,column=0)

    tarik = Button(root,text="Tarik",font=("Times New Roman",20),command=tarik,width=18,height=2,relief=RAISED,foreground="white",background="red")
    tarik.grid(row=4,column=1)

    transfer = Button(root,text="Transfer",font=("Times New Roman",20),command=transfer,width=18,height=2,relief=RAISED,foreground="white",background="blue")
    transfer.grid(row=4,column=2)
    root.mainloop()
