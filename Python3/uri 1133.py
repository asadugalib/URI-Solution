#1133
mn  = int(input())
mx = int(input())

if mn > mx:
    
    temp = mn
    mn = mx
    mx = temp
    
for i in range(mn+1, mx):
    
    if i % 5 == 2 or i % 5 == 3:

        print(i)
