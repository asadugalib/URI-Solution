#1010
product_1 = input().split(" ")
product_2 = input().split(" ")
value = int(product_1[1])*float(product_1[2]) + int(product_2[1])*float(product_2[2])

print("VALOR A PAGAR: R$ %0.2f" %value)
