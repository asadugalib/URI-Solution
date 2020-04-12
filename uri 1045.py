#1045
x = list(map(float,input().split()))

x.sort(reverse= True)

a,b,c = x

if a>= (b+c):
    print("NAO FORMA TRIANGULO")
else:
    if a*a == (b*b+c*c):
        print("TRIANGULO RETANGULO")
    elif a*a > (b*b+c*c):
        print ("TRIANGULO OBTUSANGULO")
    elif a*a < (b*b+c*c):
        print ("TRIANGULO ACUTANGULO")
    if a==b==c:
        print("TRIANGULO EQUILATERO")
    elif (a==b and c!=a) or (b==c and a!=b)  or (c==a and b!=c):
        print("TRIANGULO ISOSCELES")
