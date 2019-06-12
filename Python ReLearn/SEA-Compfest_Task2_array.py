case = int(input())
array = []
for i in range(1,case+1):
    temp_array=[]
    n = int(input())
    m = int(input())
    counter = 0
    for k in range(n):
        temp_array.append(input())
    word = input()
    for idx,j in enumerate(temp_array):
        for sdx,h in enumerate(temp_array[idx]):
            if(h == word[0]):
                    str_temp = h
                    str_temp1= h
                    str_temp2= h
                    str_temp3= h
                    for a in range(1,len(word)):
                        try:
                            str_temp += temp_array[idx][sdx+a]
                        except:
                            None
                        try:
                            str_temp1 += temp_array[idx+a][sdx]
                        except:
                            None
                        try:
                            str_temp2 += temp_array[idx+a][sdx+a]
                        except IndexError:
                            None
                        try:
                            if(sdx-a >= 0):
                                str_temp3 += temp_array[idx+a][sdx-a]
                        except IndexError:
                            None
                    if(str_temp == word):
                        counter += 1
                    if(str_temp1 == word):
                        counter += 1
                    if(str_temp2 == word):
                        counter += 1
                    if(str_temp3 == word):
                        counter += 1
            elif(h == word[-1]):
                    str_temp = h
                    str_temp1= h
                    str_temp2= h
                    str_temp3= h
                    for a in range(1,len(word)):
                        try:
                            str_temp += temp_array[idx][sdx+a]
                        except:
                            None
                        try:
                            str_temp1 += temp_array[idx+a][sdx]
                        except:
                            None
                        try:
                            str_temp2 += temp_array[idx+a][sdx+a]
                        except IndexError:
                            None
                        try:
                            if(sdx-a >= 0):
                                str_temp3 += temp_array[idx+a][sdx-a]
                        except IndexError:
                            None
                    if(str_temp == word[::-1]):
                        counter += 1
                    if(str_temp1 == word[::-1]):
                        counter += 1
                    if(str_temp2 == word[::-1]):
                        counter += 1
                    if(str_temp3 == word[::-1]):
                        counter += 1

    array.append("Case {}: {}".format(i,counter))

for i in array:
    print(i)