#1072
num = int(input())

values = []
inn = 0
out = 0

if num < 10000:

    for i in range(num):
        val = int(input())

        if -10**7 < val < 10**7:
            values.append(val)

    for i in values:

        if 10 <= i <=20:
            inn += 1
        else:
            out += 1

    print("{} in\n{} out".format(inn,out))
