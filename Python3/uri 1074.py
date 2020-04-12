#1074
n = int(input())

if n < 10000:

    x = []
    
    for i in range(n):

        value = int(input())

        if -10**7 < value < 10**7:
            x.append(value)

    for i in x:

        if i == 0:
            print("NULL")

        elif i > 0:
            num = "POSITIVE"

            if i % 2 == 0:
                print("EVEN", num)
            else:
                print("ODD", num)

        elif i < 0:
            num = "NEGATIVE"

            if i % 2 == 0:
                print("EVEN", num)
            else:
                print("ODD", num)
