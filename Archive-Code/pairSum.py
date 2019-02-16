def pairSum(lst1,maxvalue) :
    temp = lst1.copy()
    j = []
    for i in range(len(temp)) :
        k = 1+i
        for k in range(len(temp)) :
            if (temp[i]+temp[k]) == maxvalue :
                if not(i in j) :
                    print(i," ",k)
                    j.append(k)
            

pairSum([7, 8, 5, 3, 4, 6], 11)