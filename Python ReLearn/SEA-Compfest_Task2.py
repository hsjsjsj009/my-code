case = int(input())
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
                try:
                    str_temp = h
                    for a in range(sdx+1,sdx+len(word)):
                        str_temp += temp_array[idx][a]
                    if(str_temp == word):
                        counter += 1
                except IndexError:
                    None
                try:
                    str_temp = h
                    for a in range(idx+1,idx+len(word)):
                        str_temp += temp_array[a][sdx]
                    if(str_temp == word):
                        counter+=1
                except IndexError:
                    None
                try:
                    str_temp = h
                    counter_temp = 1
                    for a in range(idx+1,idx+len(word)):
                        str_temp += temp_array[a][sdx+counter_temp]
                        counter_temp += 1
                    if(str_temp == word):
                        counter+= 1
                except IndexError:
                    None
                try:
                    str_temp = h
                    counter_temp = 1
                    for a in range(idx+1,idx+len(word)):
                        if(sdx-(counter_temp) < 0):
                            continue
                        str_temp += temp_array[a][sdx-(counter_temp)]
                        counter_temp += 1
                    if(str_temp == word):
                        counter+= 1
                except IndexError:
                    None
            elif(h == word[-1]):
                try:
                    str_temp = h
                    for a in range(sdx+1,sdx+len(word)):
                        str_temp += temp_array[idx][a]
                    if(str_temp == word[::-1]):
                        counter += 1
                except IndexError:
                    None
                try:
                    str_temp = h
                    for a in range(idx+1,idx+len(word)):
                        str_temp += temp_array[a][sdx]
                    if(str_temp == word[::-1]):
                        counter+=1
                except IndexError:
                    None
                try:
                    str_temp = h
                    counter_temp = 1
                    for a in range(idx+1,idx+len(word)):
                        str_temp += temp_array[a][sdx+counter_temp]
                        counter_temp += 1
                    if(str_temp == word[::-1]):
                        counter+= 1
                except IndexError:
                    None
                try:
                    str_temp = h
                    counter_temp = 1
                    for a in range(idx+1,idx+len(word)):
                        if(sdx-(counter_temp) < 0):
                            continue
                        str_temp += temp_array[a][sdx-(counter_temp)]
                        counter_temp += 1
                    if(str_temp == word[::-1]):
                        counter+= 1
                except IndexError:
                    None


    print("Case {}: {}".format(i,counter))