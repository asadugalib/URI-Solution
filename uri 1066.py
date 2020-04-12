#1066

number= []
pos=0
neg=0
even=0
odd=0

for i in range(5):
    number.append(int(input()))

for i in range(len(number)):
    if number[i]%2 == 0:
        even+=1
    else:
        odd+=1
    if number[i]>0:
        pos+=1
    elif number[i]<0:
        neg+=1

print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)".format(even,odd,pos,neg))
