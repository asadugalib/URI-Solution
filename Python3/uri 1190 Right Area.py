#1190 Right Area

array = []
operation = input()
sm = 0
count = 0

for i in range(12):
    sub_array = []
    for j in range(12):
        sub_array.append(float(input()))
    array.append(sub_array)

for col in range(11,6,-1):
    for row in range(12-col,col):
        sm += array[row][col]
        count += 1

if operation == "S":
    print("%0.1f"%sm)
elif operation == "M":
    print("%0.1f"%(sm/count))

#alternative way
    
array = []
operation = input()
sm = 0
count = 0
for i in range(12):
    sub_array = []
    for j in range(12):
        sub_array.append(float(input()))
    array.append(sub_array)
for col in range(1,6):
    for row in range(col):
        sm += array[5+row][6+col] + array[6+row][6+col]
        count += 2
if operation == "S":
    print("%0.1f"%sm)
elif operation == "M":
    print("%0.1f"%(sm/count))
