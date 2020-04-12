#1150 Exceeding Z

x = int(input())
z = int(input())

while x >= z:
    
    z = int(input())

sm = 0
count = 0

while sm < z:

    sm += x
    x += 1
    count += 1
    
print(count)
