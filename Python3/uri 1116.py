#1116
num = int(input())

for i in range(num):
    
    x, y = list(map(int,input().split()))

    try:
        div = x/y
        print("{:0.1f}".format(div))

    except:
        print("divisao impossivel")
