#1043

a, b, c = list(map(float, input().split()))

if a < (b+c) and a > abs(b-c):
    p = a+b+c
    print ("Perimetro = {:0.1f}".format(p))
else:
    area = c*(a+b)/2
    print("Area = {:0.1f}".format(area))
