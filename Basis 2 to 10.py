
x = input("Masukkan basis 2 : ")

length = len(x)
x = int(x)
temp = 0
for i in range(length):
    temp += ((x % (10)) * (2**i))
    x = x//10
print(temp)
