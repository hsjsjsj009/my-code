

case = int(input())
for i in range(1,case+1):
    a = int(input())
    b = int(input())
    k = int(input())
    calculation = 0
    for g in range(a,b+1):
        if(g % k == 0):
            calculation += 1
    print("Case {}: {}".format(i,calculation))

