berat = float(input("Masukkan berat peserta : ")) #input berat peserta

susunan_beban = []
temp = []
if berat < 56 : #untuk pembagian kategori peserta
    kategori = "56"
elif berat >= 56 and berat < 62 :
    kategori = "62"
elif berat >= 62 and berat < 69 :
    kategori = "69"
elif berat >= 69 and berat < 77 :
    kategori = "77"
elif berat >= 77 and berat < 85 :
    kategori = "85"
elif berat >= 85 and berat < 94 :
    kategori = "94"
elif berat >= 94 and berat < 105 :
    kategori = "105"
elif berat >= 105 :
    kategori = "105+"
print("Bermain di kategori", kategori)
berat_angkat = float(input("Masukkan berat angkat : ")) #input berat beban
berat_angkat = int((berat_angkat - 25) / 2)
susunan_beban.append("bar")

if berat_angkat >= 25 :   
    pelat_25kg = (berat_angkat//25)*"Merah" #digunakan untuk menghitung jumlah pelat
    susunan_beban.append(pelat_25kg) #digunakan untuk memasukkan data ke list
    temp.append(pelat_25kg)
    berat_angkat = berat_angkat % 25
elif berat_angkat >= 20 : #digunakan untuk mengecek keperluan pelat
    pelat_20kg = (berat_angkat//20)*"Biru"
    susunan_beban.append(pelat_20kg)
    temp.append(pelat_20kg)
    berat_angkat = berat_angkat % 20
elif berat_angkat >= 15 :
    pelat_15kg = (berat_angkat//15)*"Kuning"
    susunan_beban.append(pelat_15kg)
    temp.append(pelat_15kg)
    berat_angkat = berat_angkat % 15
elif berat_angkat >= 10 :
    pelat_10kg = (berat_angkat//10)*"Hijau"
    susunan_beban.append(pelat_10kg)
    temp.append(pelat_10kg)
    berat_angkat = berat_angkat % 10
elif berat_angkat >= 5 and ((berat_angkat % 5) == 0 ) :
    pelat_5kg = (berat_angkat//5)*"Putih"
    susunan_beban.append(pelat_5kg)
    temp.append(pelat_5kg)
    berat_angkat = berat_angkat % 5
elif berat_angkat >= 2.5 and ((berat_angkat % 2.5) == 0 ):
    pelat_2setkg = int(berat_angkat//2.5)*"Merah"
    susunan_beban.append(pelat_2setkg)
    temp.append(pelat_2setkg)
    berat_angkat = berat_angkat % 2.5
elif berat_angkat >= 2  and ((berat_angkat % 2) == 0 ):
    pelat_2kg = (berat_angkat//2)*"Biru"
    susunan_beban.append(pelat_2kg)
    temp.append(pelat_2kg)
    berat_angkat = berat_angkat % 2
elif berat_angkat >= 1.5 and ((berat_angkat % 1.5) == 0 ) :
    pelat_1setkg = int((berat_angkat//1.5))*"Kuning"
    susunan_beban.append(pelat_1setkg)
    temp.append(pelat_1setkg)
    berat_angkat = berat_angkat % 1.5
elif berat_angkat >= 1 and ((berat_angkat % 1) == 0 ):
    pelat_1kg = (berat_angkat//1)*"Hijau"
    susunan_beban.append(pelat_1kg)
    temp.append(pelat_1kg)
    berat_angkat = berat_angkat % 1
elif berat_angkat >= 0.5 and ((berat_angkat % 0.5) == 0 ) :
    pelat_setkg = int((berat_angkat//0.5))*"Putih"
    susunan_beban.append(pelat_setkg)
    temp.append(pelat_setkg)
    berat_angkat = berat_angkat % 0.5
elif berat_angkat == 25 :
    susunan_beban.append("bar")        
list.reverse(temp) #memebalik posisi list
print(temp)
print(susunan_beban)
