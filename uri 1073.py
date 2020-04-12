#1073
N = int(input())

if 5 < N < 2000:
    i = 1
    
    while i <= N:

        if i % 2 == 0:
            res = i**2
            print("{}^2 = {}".format(i, res))

        i += 1
