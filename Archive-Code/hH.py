text = input("masukkan text : ")
temp = 0
for i in range(len(text)):
    if temp == 1 and text[i] == "h":
        print("H",end="")
    elif temp == 0 and text[i] == "h":
        print("h",end="")
        temp +=1
    else :
        print(text[i],end="")