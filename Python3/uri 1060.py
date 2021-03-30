#1060

number= []
pos=0

for i in range(6):
    number.append(float(input()))

for i in number:
    if i > 0:
        pos+=1

    
print("{} valores positivos".format(pos))
