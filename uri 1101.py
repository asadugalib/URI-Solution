#1101

while True:
    
    x, y = list(map(int, input().split()))
    
    if x < 1 or y < 1:
        
        break

    if x > y:
        
        temp = x
        x = y
        y = temp

    sm = 0
    
    while x <= y:
        
        print(x, end=" ")
        sm += x
        x += 1
        
    print("Sum={}".format(sm))
