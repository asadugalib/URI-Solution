#1064
number= []
pos=0
s=0

for i in range(6):
    number.append(float(input()))

for i in range(len(number)):
    test = 0+number[i]
    if test > 0:
        pos+=1
        s+= number[i]
    test = 0

avg = s/pos

print("{} valores positivos\n{:.1f}".format(pos,avg))
