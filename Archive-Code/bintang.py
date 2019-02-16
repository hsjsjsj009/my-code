def bintang(l):
    global k
    if l>0:
        bintang(l-2)
        print((((k-l)//2)*" ")+(l*"*")+(((k-l)//2)*" "),end="\n")
k=201
bintang(k)