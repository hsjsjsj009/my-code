def digit_representation(k):
    def multiplies(l):
        if l<10:
            return l
        else :
            return (l%10)*multiplies(l//10)
    if multiplies(k)>9 :
        return digit_representation(multiplies(k))
    else :
        return multiplies(k)

print (digit_representation(375))