#untuk menghilangkan huruf yang sama
def nomor_kendaraan(k):
    length = len(k)
    global check_angka
    if length>1:
            if  not k[0] == k[1] :
                return k[0] + nomor_kendaraan(k[1:length])
            else :
                return nomor_kendaraan(k[1:length])
    else :
            return k[0]
        
#untuk check angka atau tidak
def check_angka(i):
    try :
        i = int(i)
        return True
    except :
        return False
#untuk proses pengurutan
def pengurutan(s):
    length = len(s)
    global check_angka
    global angka
    global huruf
    if length>0:
        if check_angka(s[0]):
            angka += int(s[0]) 
            s = s[1:length]
            return pengurutan(s)
        else :
            huruf.append(s[0])
            s = s[1:length]
            return pengurutan(s)
#untuk check digit
def penjumlahan(l):
    if l>9 :
        return l%10+penjumlahan(l//10)
    else :
        return l

def check_digit(k) :
    if k>9:
        return check_digit(penjumlahan(k))
    else :
        return k
        
        
#untuk input
nomor = input("Masukkan nomor kendaraan : ")
angka = 0
huruf = []
pengurutan(nomor)
#pengecekan apa angka saja atau tidak
if check_angka(nomor) :
    hasil_akhir = check_digit(angka)
elif angka != 0:
    hasil_akhir = nomor_kendaraan(huruf) + str(check_digit(angka))
else:
    hasil_akhir = nomor_kendaraan(huruf)
print(hasil_akhir)
