class Perpustakaan: #class perpustakaan
    def data(self):
        self.dict_buku = {} #untuk menyimpan data awal buku
        self.dict_pinjam_buku = {} # untuk menyimpan data peminjam buku
        self.dict_histori_pinjam_buku = {} #untuk histori peminjaman buku 

    def tambah(self,kodebuku,judulbuku,penulis): #fungsi untuk menambahkan buku
        if kodebuku in self.dict_buku :
            print(("Buku {} gagal disimpan ke dalam sistem karena kode buku sudah terdaftar sebelumnya.").format(judulbuku))
        else :
            self.dict_buku[kodebuku] = [judulbuku,penulis]
            print(("Buku {} berhasil disimpan ke dalam sistem.").format(judulbuku))
        
    def info(self,kodebuku): #fungsi untuk mengetahui info buku
        if kodebuku in self.dict_buku:
            print(("{} - {}").format(self.dict_buku[kodebuku][0],self.dict_buku[kodebuku][1]))
            if kodebuku not in self.dict_pinjam_buku:
                print("Buku ini tidak sedang dipinjam.")
            else :
                print(("Buku ini sedang dipinjam oleh {}.").format(self.dict_pinjam_buku[kodebuku]))
            if kodebuku not in self.dict_histori_pinjam_buku:
                print("Buku ini tidak pernah dipinjam oleh siapa pun.")
            else :
                print(("Buku ini pernah dipinjam oleh {}.").format(",".join(self.dict_histori_pinjam_buku[kodebuku])))
        else :
            print(("Tidak ada buku dengan kode {} di sistem perpustakaan.").format(kodebuku))
    def pinjambuku(self,kodebuku,peminjambuku): # fungsi untuk meminjam buku
        if kodebuku not in self.dict_buku:
            print(("Tidak ada buku dengan kode {} di sistem perpustakaan.").format(kodebuku))
        else :
            if kodebuku not in self.dict_pinjam_buku:
                print(("Buku {} berhasil dipinjam oleh {}.").format(self.dict_buku[kodebuku][0],peminjambuku))
                self.dict_pinjam_buku[kodebuku] = peminjambuku
                if kodebuku not in self.dict_histori_pinjam_buku:
                    self.dict_histori_pinjam_buku[kodebuku] = [peminjambuku]
                else :
                    self.dict_histori_pinjam_buku[kodebuku].append(peminjambuku)
            else : 
                print(("Maaf, buku {} sedang dipinjam oleh {}.").format(self.dict_buku[kodebuku][0],self.dict_pinjam_buku[kodebuku]))
    
    def kembalikan(self,kodebuku,pengembali): #fungsi untuk mengembalikan buku
        if kodebuku not in self.dict_buku :
            print(("Tidak ada buku dengan kode {} di sistem perpustakaan.").format(kodebuku))
        else :
            if pengembali != self.dict_pinjam_buku[kodebuku]:
                print(("Maaf, buku {} harus dikembalikan oleh {}.").format(self.dict_buku[kodebuku][0],self.dict_pinjam_buku[kodebuku]))
            else :
                print(("Buku {} telah dikembalikan oleh {}.").format(self.dict_buku[kodebuku][0],pengembali))
                self.dict_pinjam_buku.pop(kodebuku)


def main():
    try :
        pathfile = input("Masukkan path file :") #Memasukkan file
        openfile = open(pathfile,"r")
        readfile = openfile.readlines()
        perintah = ["INFO BUKU","PINJAM BUKU","KEMBALIKAN BUKU","KELUAR"]
        perpus = Perpustakaan()
        perpus.data() #membuat data untuk variabel tertentu
        openfile.close()
        for i in range(len(readfile)): #iterasi tiap line
                temp = readfile[i].split(";")
                temp[-1] = temp[-1].replace("\n","")
                perpus.tambah(temp[0],temp[1],temp[2])
        while True: #untuk terus menerus menjalankan program
            temp = input("Masukkan perintah : ")
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
            except KeyError: # menangani apabila ada data yang tidak ada
                print("Data tidak ada")
    except IOError: #menangani file tidak ada
        print("File tidak ada")

if __name__ == "__main__": #memastikan kalau menggunakan top-level module
    main()