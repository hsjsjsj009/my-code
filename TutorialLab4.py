pesan       = input("Pesan : ")
key         = input("Key : ")
key_angka   = int(key.split(" ")[0])
if len(key.split(" ")) == 2 :  
    key_huruf   = key.split(" ")[1]
else :
    key_huruf   = ""
hasil_akhir = " "
awal = 0
for numb in range(key_angka,len(pesan)+key_angka,key_angka):
    temp_pesan = pesan[awal:numb][::-1]
    temp_pesan += key_huruf
    hasil_akhir += temp_pesan
    awal += key_angka

print(hasil_akhir.strip())

