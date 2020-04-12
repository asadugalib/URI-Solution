#1080

number = []

for i in range(100):

    number.append(int(input()))

print(max(number))

print(number.index(max(number))+1)
