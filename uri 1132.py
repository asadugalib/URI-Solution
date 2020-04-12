#1132
mn  = int(input())
mx = int(input())

sm = 0

if mn > mx:

    temp = mn
    mn = mx
    mx = temp
    
for i in range(mn, mx+1):

    if i % 13 != 0:
        sm += i

print(sm)
