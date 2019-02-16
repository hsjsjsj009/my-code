def pixels(lst) :
    temp = 0
    for i in lst :
        for k in i :
            if k != 0 :
                temp += 1
    return temp
print(pixels([[0, 156, 0, 0], [34, 0, 0, 0], [23, 123, 0, 34]]))