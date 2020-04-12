#1060

number= []
pos=0

for i in range(6):
    number.append(float(input()))

for i in range(len(number)):
    test = 0+number[i]
    if test > 0:
        pos+=1
    test = 0
    
print("{} valores positivos".format(pos))
