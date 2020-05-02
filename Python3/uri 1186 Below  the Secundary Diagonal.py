#1186 Below the Secundary Diagonal

array = []
operation = input()
sm = 0
count = 0

for i in range(12):
    sub_array = []
    for j in range(12):
        sub_array.append(float(input()))
    array.append(sub_array)
for i in range(1,12):
    for j in range(i):
        sm += array[i][-1-j]
        count += 1

if operation == "S":
    print("%0.1f"%sm)
elif operation == "M":
    print("%0.1f"%(sm/count))
