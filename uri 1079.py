#1079
num = int(input())

values = []
sm = 0
weight = [2, 3, 5]

for i in range(num):

    values.append(list(map(float,input().split())))

for i in values:

    sm = 0

    for j in range(3):

        sm = sm + i[j]*weight[j]

    avg = sm / 10

    print("{:.1f}".format(avg))
