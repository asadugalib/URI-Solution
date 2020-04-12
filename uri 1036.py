#1036
data = input().split(" ")
a,b,c = float(data[0]),float(data[1]),float(data[2])

try:
    root = (b**2-4*a*c)**0.5
    r1 = (-b+root)/(2*a)
    r2 = (-b-root)/(2*a)
    print("R1 = {:0.5f}\nR2 = {:0.5f}".format(r1,r2))
except:
    print("Impossivel calcular")
