def negative(lst):+
    i = len(lst)
    temp = 0
    while temp<i :
        if lst[temp] < 0 :
            return temp
            break
        else :
            temp += 1
    return -1

print(negative([1, 2, 3]))
