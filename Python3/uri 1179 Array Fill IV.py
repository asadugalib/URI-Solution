#1179 Array Fill IV

def arrayprint(ty,array):
    for i in range(len(array)):
        print("%s[%d] = %d"%(ty, i, array[i]))
    array.clear()

count = 0
odd = []
even = []

while count < 15:
    num = int(input())
    if num % 2 != 0:
        odd.append(num)
        if len(odd) == 5:
            arrayprint("impar", odd)
            #odd.clear()
    else:
        even.append(num)
        if len(even) == 5:
            arrayprint("par", even)
            #even.clear()
    count += 1
    
arrayprint("impar", odd)
arrayprint("par", even)
