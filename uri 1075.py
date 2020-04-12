#1075
n = int(input())

if n < 10000:

    for i in range(1,10000):

        if i % n == 2:

            print(i)
