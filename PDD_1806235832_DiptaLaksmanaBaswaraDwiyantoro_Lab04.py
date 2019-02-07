pesan       = input("Pesan : ") #input pesan
key         = input("Key : ") #input key
key_angka   = int(key.split(" ")[0]) #pengambilan data key angka
if len(key.split(" ")) == 2 : #pengecekan ada tidaknya key huruf  
    key_huruf   = key.split(" ")[1]
else :
    key_huruf   = ""
temp_pesan = ""

if len(pesan) % key_angka == 0 : #pengecekan kondisi panjang pesan
    iterasi = len(pesan)//key_angka
else :
    iterasi = (len(pesan)+key_angka)//key_angka
for numb in range(iterasi): #pemrosesan data
    temp_pesan += pesan[numb*key_angka : (key_angka)+key_angka*numb][::-1] + key_huruf

print(temp_pesan.strip())#penulisan data yang telah di proses, strip di gunakan untuk menghilangkan spasi di depan atau di belakang kalimat

