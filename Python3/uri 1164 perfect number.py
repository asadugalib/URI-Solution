#1164 perfect number

test = int(input())
count = 0

while count < test:
    
    number = int(input())
    sm = 0
    
    for i in range(1,number):
        
        if number%i == 0:

            sm += i

    if sm == number:

        print("%d eh perfeito"%number)

    else:
        
        print("%d nao eh perfeito"%number)

    count += 1
