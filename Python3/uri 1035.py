#1035
data = input().split(" ")
a,b,c,d = int(data[0]),int(data[1]),int(data[2]),int(data[3])

if b > c and d>a and c+d>a+b and c>0 and d>0 and a%2==0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
