#1182 Column in Array

array = []
column = int(input())
operation = input()
sum = 0
for i in range(12):
    sub_array = []
    for j in range(12):
        sub_array.append(float(input()))
    array.append(sub_array)
for i in range(12):
    sum += array[i][column]
if operation == "S":
    print("%0.1f"%sum)
elif operation == "M":
    print("%0.1f"%(sum/12))
