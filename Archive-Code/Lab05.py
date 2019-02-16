try:# untuk mengecek error
        path = input("Masukkan alamat file : ") #untuk input alamat file
        f_read = open(path,"r") #untuk membuka file
        temp_str =  f_read.readlines()[0] #untuk membaca file dan mengambil data
        hal_yang_dihilangkan = str.maketrans('_,-',3*' ') #untuk menghilangkan tanda tidak berguna
        temp_str = temp_str.translate(hal_yang_dihilangkan).split() #untuk menerjemahkan kode maketrans dan mensplit kalimat
        dict = [["pocong",0],["kuyang",0],["kuntilanak",0],["tuyul",0]]
        for i in range(len(temp_str)): # untuk membuat huruf seluruh list menjadi lowercase
            temp_str[i] = temp_str[i].lower()

        for i in range(4): #untuk menghitung jumlah kata
            dict[i][1] = temp_str.count(dict[i][0])

        print("Welcome!")
        def main():
            try : #untuk mengecek error
                while True: #agar program tetap berjalan
                    inputan = int(input("1:\tLihat isi file\n2:\tTambahkan isi file\n3:\tExit\n"))
                    if inputan == 1 :
                        print('Daftar Setan:\n')
                        for i in range(4):
                            print(("{:10} = {:4} ").format(dict[i][0].capitalize(),dict[i][1])) #untuk mencetak daftar setan
                    elif inputan == 2 :
                        boolean = False
                        inputan_baru = input("")
                        inputan_baru = inputan_baru.split()
                        inputan_baru[0] = inputan_baru[0].lower()
                        for k in range(4):
                            if inputan_baru[0] == dict[k][0] :
                                boolean = True
                                temp = k
                        if boolean :
                            dict[temp][1] += int(inputan_baru[1])
                        else :
                            print("Jenis setan tidak terdaftar dalam file!")

                    elif inputan == 3 :
                        f_read.close() #untuk menutup file
                        exit() #untuk menutup aplikasi
                    else :
                        print("Perintah salah")
                    print("\n")
            except IndexError :
                print("Tidak ada masukkan angka!")
                main()
            except ValueError :
                print("Harap masukkan angka, bukan huruf!")
                main()
        main()
except FileNotFoundError :
    print("File tidak ada!")

