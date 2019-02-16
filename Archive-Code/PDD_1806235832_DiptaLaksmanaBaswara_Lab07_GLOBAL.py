try :
    fx = input("Masukkan fungsi f(x): ") #input untuk fungsi fx
    gx = input("Masukkan fungsi g(x): ") #input untuk fungsi gx
    x = eval(input("Masukkan angka x: ")) #input untuk nilai x
    def calculation(function): # fungsi untuk menghitung fungsi dan nilai x
        global x               # untuk membuat variabel x menjadi global dan bisa digunakan di fungsi ini
        x = eval(function)     # untuk mengubah nilai variabel x yang global menjadi hasil kalkulasi dari fungsi dengan variabel x global sebelumnya
        # namespace pada fungsi ini mengikuti variabel x yang ada di seluruh kode 
        # fungsi ini tidak menggunakan parameter x karena sudah mengambil variabel x dari luar fungsi dengan pendeklarasian global x
        # fungsi ini tidak menggunakan return karena sudah merubah variabel x keseluruhan
    calculation(gx) # namespace yang digunakan adalah variabel x yang di input (x --> x awal)
    calculation(fx) # namespace yang digunakan adalah variabel x hasil dari kalkulasi oleh calculation(gx) (x--> calculation(gx))
    print("Hasil komposisi (f o g)(x) adalah:",x)
except :
    print("Input salah")