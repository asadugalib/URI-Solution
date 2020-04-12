#1099

num = int(input())
output = []

for i in range(num):
    
    x,y = list(map(int, input().split()))
    
    if x > y:
        temp = x
        x = y
        y = temp

    sm = 0
    
    for i in range(x+1, y):
        
        if i % 2 != 0:
            
            sm += i

    output.append(sm)

for i in output:

    print(i)
