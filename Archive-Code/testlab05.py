
path = input("Masukkan alamat file : ")
f_read = open("katalogsetan.txt","r").readlines()
temp_str =  f_read[0]
table = str.maketrans(',-_',3*' ')
temp_str = temp_str.translate(table).split().lower()
print (temp_str)