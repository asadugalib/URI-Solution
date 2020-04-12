#1173 Array fill I

number = int(input())

array = []

for i in range(10):
    
    array.append(number)
    print("N[%d] = %d"%(i, number))
    number *= 2
