x = int(input("Masukkan angka : "))
y = ["A","B","C","D","E","F"]

hasil = " "
while x > 0 :
    temp = x%16
    if temp > 9 :
        indikator = temp-10
        hasil = y[indikator] + hasil
    else :
        hasil = str(temp) + hasil
    x = x//16
print (hasil)