#1188 Inferior Area

array = []
operation = input()
sm = 0
count = 0
for i in range(12):
    sub_array = []
    for j in range(12):
        sub_array.append(float(input()))
    array.append(sub_array)
for row in range(7,12):
    for column in range(12-row,row):
        sm += array[row][column]
        count += 1

if operation == "S":
    print("%0.1f"%sm)
elif operation == "M":
    print("%0.1f"%(sm/count))
