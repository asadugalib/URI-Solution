#1181 Line in Array

array = []
index = int(input())
operation = input()

for i in range(12):
    sub_array =[]
    for j in range(12):
        sub_array.append(float(input()))
    array.append(sub_array)

if operation == "S":
    print("%0.1f"%(sum(array[index])))
elif operation == "M":
    print("%0.1f"%((sum(array[index]))/12))
