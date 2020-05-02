#1175 Array change I

n = []

for i in range(20):
    n.append(int(input()))
for i in range(19,-1,-1):
    j = 19-i
    print("N[%d] = %d"%(j,n[i]))
