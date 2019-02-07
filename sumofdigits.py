def sum_of_digits(l):
    if l>9:
        return (l%10) + sum_of_digits(l//10)
    else :
        return l

print(sum_of_digits(17854))