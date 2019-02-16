def k_sum_pairs(a_list,k):
    a_list.sort()
    hasil = [(a_list[i],a_list[l]) for i in range(len(a_list)) for l in range(len(a_list)) if a_list[i]+a_list[l] == k]
    '''
    for i in range(len(a_list)):
        for l in range(i+1,len(a_list)):
            if i+l == k :
                hasil.append([i,l])
    '''
    return hasil

def find_modus(a_list):
    max = 0
    temp = 0
    for i in a_list:
        if a_list.count(i)>=max:
            temp = i
            max = a_list.count(i)
    return temp

def max_cap(s):
    max=0
    temp=""
    for i in s:
            if i == i.upper() :
                    if ord(i) >= max :
                        max = ord(i)
                        temp = i
    if len(temp)>0:
            return temp
'''
for i in range(1,50,3):
    if i %7 == 1:
        print(i-1)
'''
def count(n):
        hasil =[]
        total=0
        for i in range(1,n):
                total += i
                if total <= n:
                        if total == n :
                                hasil.append(str(i))
                                break
                        else :
                                hasil.append(str(i))
                else :
                        break
        if total > n :
                return 'Tidak ada'
        else :
                s = "+"
                s=s.join(hasil)
                return s
print(count(10))