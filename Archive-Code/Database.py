nama = input("Silahkan masukkan nama Anda: ") #input buat nama operator
if nama.lower() == "jack" : #untuk mengecek ketersediaan operator
    opsi = int(input("Silahkan masukkan opsi Anda (1. Penyimpanan Data, 2. Pengambilan Data): ")) #input buat opsi
    if opsi == 1 : # pengecekan opsi
        angka=int(input("Silahkan masukkan angka yang akan disimpan: ")) # input untuk angka
        temp = str(angka%2) # pengkonversian dari decimal ke angka biner
        angka = angka//2
        while angka > 0 :
            temp = str(angka%2) + temp
            angka = angka//2
        print("Angka yang disimpan di dalam database adalah",temp)
    elif opsi == 2 :
        angka=input("Silahkan masukkan angka yang akan diambil: ")
        length = len(angka)
        angka = int(angka)
        temp = 0
        for i in range(length): #pengkonversian dari biner ke decimal
            temp += ((angka % (10)) * (2**i))
            angka = angka//10
        print("Angka yang diambil di dalam database adalah",temp)
    else :
        print("Perintah tidak dikenal!") #pesan bila opsi tidak ada
elif nama.lower() == "benny" :
    opsi = int(input("Silahkan masukkan opsi Anda (1. Penyimpanan Data, 2. Pengambilan Data): "))
    if opsi == 1 :
        angka=int(input("Silahkan masukkan angka yang akan disimpan: "))
        temp = str(angka%4) #pengkonversian angka decimal ke quantal
        angka = angka//4
        while angka > 0 :
            temp = str(angka%4) + temp
            angka = angka//4
        print("Angka yang disimpan di dalam database adalah",temp)
    elif opsi == 2 :
        angka=input("Silahkan masukkan angka yang akan diambil: ")
        length = len(angka)
        angka = int(angka)
        temp = 0
        for i in range(length): #pengkonversian angka quantal ke decimal
            temp += ((angka % (10)) * (4**i))
            angka = angka//10
        print("Angka yang diambil di dalam database adalah",temp)    
    else :
        print("Perintah tidak dikenal!")
else :
    print("Tidak ada operator yang bernama",nama) #pesan apabila operator tidak tersedia