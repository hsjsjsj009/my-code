def palindrome(k):
    import string
    k = k.translate(str.maketrans(string.punctuation,32*" "))
    k = k.replace(" ","")
    k=k.lower()
    if k[0] == k[-1] and len(k) > 1:
        return palindrome(k[1:-1])
    elif len(k) == 1:
        return True
    else :
        return False

def kodok(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        return kodok(n-3)+kodok(n-2)+kodok(n-1)

print(kodok(1000))
