#1051
salary= float(input())

if 0<= salary <=2000:
    print("Isento")

elif 2000< salary <=3000:
    tax = (salary-2000)*.08
    print("R$ {:.2f}".format(tax))

elif 3000 < salary <= 4500:
    tax = (1000*.08)+(salary-3000)*.18
    print("R$ {:.2f}".format(tax))

elif salary > 4500:
    tax = (1000*.08)+(1500*.18)+(salary-4500)*.28
    print("R$ {:.2f}".format(tax))
