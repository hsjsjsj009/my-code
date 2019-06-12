case = int(input())
array = []
for i in range(case):
    row = int(input())
    character = int(input())
    for k in range(row):
        array.append(input())
    for k in range(row):
        for j in array[k]:
            if(j == "."):
                