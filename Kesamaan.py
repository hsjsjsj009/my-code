def inBoth(lst1,lst2) :
    boolean = False
    for i in lst1 :
            if i in lst2 :
                boolean = True
    return boolean

print(inBoth([3,2,4,5,7],[9,0,1,3]))
    