#1113

while True:
    
    x, y = list(map(int, input().split()))

    if x == y:
        break

    elif x > y:
        print("Decrescente")

    else:
        print("Crescente")
