#1038

price = {1:4, 2:4.50, 3:5.00, 4:2.00, 5:1.50}
x,y= list(map(int,input().split(" ")))

value = price[x] *y

print ("Total: R$ {:0.2f}".format(value))
