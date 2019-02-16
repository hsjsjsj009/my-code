dict_buku = {} #untuk menyimpan data awal buku
dict_pinjam_buku = {} # untuk menyimpan data peminjam buku
dict_histori_pinjam_buku = {} #untuk histori peminjaman buku 
class Perpustakaan: #class perpustakaan
    def tambah(self,arg1,arg2,arg3): #fungsi untuk menambahkan buku
        global dict_buku
        if arg1 in dict_buku :
            print(("Buku {} gagal disimpan ke dalam sistem karena kode buku sudah terdaftar sebelumnya.").format(arg2))
        else :
            dict_buku[arg1] = [arg2,arg3]
            print(("Buku {} berhasil disimpan ke dalam sistem.").format(arg2))
        
    def info(self,arg1): #fungsi untuk mengetahui info buku
        global dict_buku
        global dict_pinjam_buku
        global dict_histori_pinjam_buku
        if arg1 in dict_buku:
            print(("{} - {}").format(dict_buku[arg1][0],dict_buku[arg1][1]))
            if arg1 not in dict_pinjam_buku:
                print("Buku ini tidak sedang dipinjam.")
            else :
                print(("Buku ini sedang dipinjam oleh {}.").format(dict_pinjam_buku[arg1]))
            if arg1 not in dict_histori_pinjam_buku:
                print("Buku ini tidak pernah dipinjam oleh siapa pun.")
            else :
                print(("Buku ini pernah dipinjam oleh {}.").format(",".join(dict_histori_pinjam_buku[arg1])))
        else :
            print(("Tidak ada buku dengan kode {} di sistem perpustakaan.").format(arg1))
    def pinjambuku(self,arg1,arg2): # fungsi untuk meminjam buku
        global dict_buku
        global dict_pinjam_buku
        global dict_histori_pinjam_buku
        if arg1 not in dict_buku:
            print(("Tidak ada buku dengan kode {} di sistem perpustakaan.").format(arg1))
        else :
            if arg1 not in dict_pinjam_buku:
                print(("Buku {} berhasil dipinjam oleh {}.").format(dict_buku[arg1][0],arg2))
                dict_pinjam_buku[arg1] = arg2
                if arg1 not in dict_histori_pinjam_buku:
                    dict_histori_pinjam_buku[arg1] = [arg2]
                else :
                    dict_histori_pinjam_buku[arg1].append(arg2)
            else : 
                print(("Maaf, buku {} sedang dipinjam oleh {}.").format(dict_buku[arg1][0],dict_pinjam_buku[arg1]))
    
    def kembalikan(self,arg1,arg2): #fungsi untuk mengembalikan buku
        global dict_buku
        global dict_pinjam_buku
        global dict_histori_pinjam_buku
        if arg1 not in dict_buku :
            print(("Tidak ada buku dengan kode {} di sistem perpustakaan.").format(arg1))
        else :
            if arg2 != dict_pinjam_buku[arg1]:
                print(("Maaf, buku {} harus dikembalikan oleh {}.").format(dict_buku[arg1][0],dict_pinjam_buku[arg1]))
            else :
                print(("Buku {} telah dikembalikan oleh {}.").format(dict_buku[arg1][0],arg2))
                dict_pinjam_buku.pop(arg1)


def main():
    try :
        pathfile = input("Masukkan path file :") #Memasukkan file
        openfile = open(pathfile,"r")
        readfile = openfile.readlines()
        perintah = ["INFO BUKU","PINJAM BUKU","KEMBALIKAN BUKU","KELUAR"]
        perpus = Perpustakaan()
        openfile.close()
        for i in range(len(readfile)): #iterasi tiap line
                temp = readfile[i].split(";")
                temp[-1] = temp[-1].replace("\n","")
                perpus.tambah(temp[0],temp[1],temp[2])
        while True: #untuk terus menerus menjalankan program
            temp = input()
            temp = temp.split(";")
            try :
                if temp[0] == perintah[0]: #pemilihan perintah
                    perpus.info(temp[1])
                elif temp[0] == perintah[1]:
                    perpus.pinjambuku(temp[1],temp[2])
                elif temp[0] == perintah[2]:
                    perpus.kembalikan(temp[1],temp[2])
                elif temp[0] == perintah[3]:
                    print("Goodbye!")
                    exit()
                else :
                    print("Perintah tidak ada!")
            except IndexError: #menangani apabila ada data yang kurang
                print("Data kurang")
    except IOError: #menangani file tidak ada
        print("File tidak ada")

if __name__ == "__main__": #memastikan kalau menggunakan top-level module
    main()