#1145
x, y = list(map(int, input().split()))

count = 1

for i in range((y//x)):
    
    line = ""
    
    for j in range(x):
        
        line += str(count) + " "
        count += 1

    print(line[:-1])
