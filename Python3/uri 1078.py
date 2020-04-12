#1078
n = int(input())

if 1 < n < 10000:

    for i in range(1, 11):

        print("{} x {} = {}".format(i, n, i*n))
