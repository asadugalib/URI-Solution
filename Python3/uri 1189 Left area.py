#1189 Left area

array = []
operation = input()
sm = 0
count = 0

for i in range(12):
    sub_array = []
    for j in range(12):
        sub_array.append(float(input()))
    array.append(sub_array)
for col in range(5):
    for row in range(col+1,11-col):
        sm += array[row][col]
        count += 1

if operation == "S":
    print("%0.1f"%sm)
elif operation == "M":
    print("%0.1f"%(sm/count))
