#1065
number= []
even=0

for i in range(5):
    number.append(int(input()))

for i in range(len(number)):
    if number[i]%2 == 0:
        even+=1

print("{} valores pares".format(even))
