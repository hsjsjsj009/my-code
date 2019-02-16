x = input("Masukkan basis 16 : ")
y = ["A","B","C","D","E","F","a","b","c","d","e","f"]
l = [10,11,12,13,14,15]

length = len(x)
hasil = 0
pangkat = length
for numb in range(length) :
    pangkat -= 1
    if x[numb] in y :
        for i in range(12) :
            if x[numb] == y[i] :
                if i > 5 :
                    temp = i%6
                    hasil += l[temp] * (16**pangkat)
                else :
                    hasil += l[i] * (16**pangkat)
    else :
        temp = int(x[numb])
        hasil += temp * (16**pangkat)
print(hasil)