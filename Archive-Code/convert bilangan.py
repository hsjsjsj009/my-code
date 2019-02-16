hasil = []

def dectohex(y) :
    hasiltemp = " "
    while y > 0 :
        temp = x%16
        if temp > 9 :
            indikator = temp-10
            hasiltemp = y[indikator] + hasil
        else :
            hasiltemp = str(temp) + hasil
        x = x//16
    return hasiltemp

def dectobin(y) :
    temp = str(x%2)
    x = x//2
    while x > 0 :
        temp = str(x%2) + temp
        x = x//2


x = input("Masukkan radix : ")
y = input("Masukkan angka : ")
