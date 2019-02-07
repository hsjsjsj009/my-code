kolom = int(input("Masukkan kolom : "))
baris = int(input("Masukkan baris : "))
matrix = []
for numb in range(kolom) :
    input_baris = input("")
    matrix.append(baris.split())

for i in range(baris) :
    for numb in range(kolom) :
        print(matrix[numb][i],matrix[numb+])
