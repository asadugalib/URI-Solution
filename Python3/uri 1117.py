#1117
count = 0
sum = 0

while True:
    
    score = float(input())
    
    if score > 10 or score < 0:
        
        print("nota invalida")

    else:
        
        count += 1
        sum += score
        if count == 2:
            break

print("media = {:0.2f}".format(sum/2))
