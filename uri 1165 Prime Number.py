#1165 Prime Number

import math

def prime(number):
    
    if number > 2:
        
        for i in range(2,int(math.sqrt(number))+1):
            
            if number%i == 0:
                
                return "%d nao eh primo"%number

        return "%d eh primo"%number

    return "%d eh primo"%number

test = int(input())

for i in range(test):
    
    print(prime(int(input())))
