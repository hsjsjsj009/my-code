
x = int(input("Masukkan basis 10 : "))

temp = str(x%2)
x = x//2
while x > 0 :
    temp = str(x%2) + temp
    x = x//2

print(temp)

