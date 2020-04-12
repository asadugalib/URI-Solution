#1144
N = int(input())
a = 1

for i in range(N):
    
    print("{} {} {}".format(a, a**2, a**3))
    print("{} {} {}".format(a, 1+a**2, 1+a**3))
    a += 1
