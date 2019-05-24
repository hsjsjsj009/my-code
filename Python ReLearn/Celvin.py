inputan  = input()
inputan = inputan.split()
hour = int(inputan[0])
mins = int(inputan[1])
duration = int(inputan[2])

minsTemp = (duration + mins) % 60
hour = (hour + ((duration + mins) // 60)) % 24


print("{}:{}".format(hour,minsTemp))
print("test")