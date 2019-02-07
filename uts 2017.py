## no 1
##def k_sum_pairs(lst,k):
##    listhasil = []
##    for i in lst:
##        for j in lst:
##            hasil = i+j
##            if hasil == k:
##                listhasil.append((i,j))
##    listhasil.sort()
##    return listhasil

##no 2
##def find_modus(lst):
##    counter = lst.count(lst[0])
##    angka = lst[0]
##    for i in lst:
##        if lst.count(i)>counter:
##            counter = lst.count(i)
##            angka = i
##    return angka

##def find_modus(lst):
##    return max([lst.count(i),i]for i in lst)[1]

##no3
##def max_cap(s):
##    max_cap = None
##    for i in s:
##        if i.isupper() and (max_cp == None or i>max_cp):
##            max_cp = i
##    return max_cp
            
    
##no4
##[1,2,3] None

##no5
##for i in range(4,53,3):
##    if i % 7 == 1:
##        return (i-1)

##no7
##1111 1111 1011 0110
##f     f     b    6
##001 111 111 110 110 110
##1    7   7    6  6   6

##no8
##def is_factor(a,b):
##    if b%a == 0:
##        return True
##    return False

##no 12
##a = bn + k
##k selalu positif
## -15 = 7*(-3) + 6 (yang -15 // b)

a_str ='Donald  Knuth'
print(a_str [-1:-4:-2] + a_str [ -4::2])
