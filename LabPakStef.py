import string
class Encrypt:    
    def make_dictionary(self,start):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.dictionary = {}
        started = alphabet.index(start)
        for i in alphabet:
            if started == 26  :
                started = started-26
            self.dictionary[i]=alphabet[started]
            started += 1

    def run(self,huruf):
        return self.dictionary[huruf]

class Decrypt:
    def make_dictionary(self,start):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.dictionary = {}
        started = alphabet.index(start)
        for i in alphabet:
            if started == 26  :
                started = started-26
            self.dictionary[alphabet[started]]=i
            started += 1
    
    def run(self,huruf):
        return self.dictionary[huruf]


dict_key = {}
key = input("Masukkan key : ").upper()
text = input("Masukkan text : ").upper()
perintah = input("D(Decrypt) or E(Encrypt)? ")
if perintah.upper() == "E":
    for k in key:
            dict_key[k]= Encrypt()
            dict_key[k].make_dictionary(k)

    for k in range(len(text)):
        if text[k] == " " or text[k] in string.punctuation:
            print(text[k],end="")
        else :
            temp = k % len(key)
            print(dict_key[key[temp]].run(text[k]),end="")
elif perintah.upper() == "D" :
    for k in key:
            dict_key[k]= Decrypt()
            dict_key[k].make_dictionary(k)
    for k in range(len(text)):
        if text[k] == " " or text[k] in string.punctuation:
            print(text[k],end="")
        else :
            temp = k % len(key)
            print(dict_key[key[temp]].run(text[k]),end="")
else :
    print('Tidak ada Perintah')
