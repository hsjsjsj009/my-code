def digit_representation(x):
    temp = 1
    if x<10:
        return x
    else :
        while x>0:
           temp *= x%10
           x =x//10 
        return digit_representation(temp)

print(digit_representation(397))