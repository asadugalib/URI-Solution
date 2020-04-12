#1071
x = int(input())
y = int(input())

if x < y:
    temp = x
    x = y
    y = temp

odd_sum = 0
y = y+1

while y < x:

    if y % 2 != 0:
        odd_sum += y

    y += 1

print(odd_sum)
