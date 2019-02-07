    
#LOKAL
try :        
    fx = input("Masukkan fungsi f(x): ") #input untuk fungsi fx
    gx = input("Masukkan fungsi g(x): ") #input untuk fungsi gx
    x = int(input("Masukkan angka x: ")) #input untuk nilai x
    def calculation(func,x): # fungsi untuk menghitung fungsi dan nilai x
        x = eval(func)       # fungsi ini menggunakan variabel x yang bersifat lokal karena berlaku hanya pada fungsi ini, dapat ditunjukkan dengan adanya pemasukkan parameter bervariabel x pada fungsi
        #method eval digunakan untuk mengkonversi dari string menjadi suatu formula perhitungan yang dapat dioperasikan di python
        return x             # namespace pada fungsi ini adalah variabel x dan func yang sesuai parameter yang dimasukkan, variabel x pada fungsi ini tidak mengikuti variabel x pada luar fungsi       
        # fungsi ini menggunakan parameter x karena tidak menggunakan variabel x secara global
        # fungsi ini menggunakan return karena perlu adanya nilai yang di kembalikan dari pemrosesan variabel x dengan function, kalau tidak menggunakan return tidak ada hasil yang dikembalikan untuk diproses selanjutnya
    x=calculation(gx,x)      # namespace pada pemanggilan fungsi ini ialah x yang sesuai input (x-->x awal)     
    print("Hasil komposisi (f o g)(x) adalah:",calculation(fx,x)) # namespace pada pemanggilan ini merupakan kalkulasi nilai x dan fungsi gx (x-->calculation(gx,x)) 
except :
    print("Input Salah")    