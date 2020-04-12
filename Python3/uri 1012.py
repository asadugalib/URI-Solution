#1012
data = (input().split(" "))
a,b,c = float(data[0]),float(data[1]),float(data[2])

rect = 0.5*a*c
cir = 3.14159*c*c

trp = c*(a+b)/2
quad = b*b
rectan = a*b

print("TRIANGULO: {:0.3f}\nCIRCULO: {:0.3f}\nTRAPEZIO: {:0.3f}\nQUADRADO: {:0.3f}\nRETANGULO: {:0.3f}" .format(rect,cir,trp,quad,rectan))
