N = int(input("Enter number : "))
if N % 4 == 0:
    N += 1
    print(N)
else:
    N -= 1
    print(N)