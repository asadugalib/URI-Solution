#1070
num = int(input())

i = num+1
count = 0

while True:
    
    if i % 2 != 0:
        print(i)
        count += 1

    if count >= 6:
        break

    i = i + 1
