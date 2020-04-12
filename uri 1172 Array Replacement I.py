#1172 Array Replacement I

x = []

for i in range(10):
    
    j = int(input())
    
    if j > 0:
        
        x.append(j)

    else:
        
        x.append(1)

for i in range(10):

    y = x[i]
    print("X[%d] = %d"%(i,y))
