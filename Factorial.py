def Factorial(y) :
    if y == 1 :
        return 1
    elif y==0 :
        return 1
    else :
        return y*Factorial(y-1)

x = int(input("Masukkan bilangan factorial : "))
print(Factorial(x))
