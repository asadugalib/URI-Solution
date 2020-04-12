#1098
i = 0
c = 0

while i <= 2:
    
    for j in range(1,4):
        
        if i == 0 or i == 1:
            
            print("I={:.0f} J={:.0f}".format(i,j+i))

        elif c == 10:
            
            i = 2
            print("I={:.0f} J={:.0f}".format(i,j+i))

        else:
            
            print("I={:0.1f} J={:.1f}".format(i,j+i))

    i += 0.2
    c += 1
