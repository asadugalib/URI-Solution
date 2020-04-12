#1159 Sum of Consecutive Even Numbers

while True:
    
    num = int(input())
    
    if num != 0:
        
        even_sum = 0
        count = 0
        
        while count < 5:
            
            if num % 2 == 0:

                even_sum += num

            else:

                even_sum += num+1

            num += 2
            count += 1
            
        print(even_sum)

    else:

        break
