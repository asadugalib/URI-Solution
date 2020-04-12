#1160 Population Increase

test = int(input())
count1 = 0

while count1 < test:
    
    data = input().split()
    
    pa,pb,ga,gb = int(data[0]),int(data[1]),float(data[2]),float(data[3])
    count = 0
    
    while True:
        
        count += 1
        pa += int(pa * (ga/100))
        pb += int(pb * (gb/100))
        
        if count > 100:

            print("Mais de 1 seculo.")
            break

        if pa > pb:

            print("%d anos."%count)
            break

    count1 += 1
