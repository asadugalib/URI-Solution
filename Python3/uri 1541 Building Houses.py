#1541 Building Houses

while True:
    try:
        a, b, c = list(map(int, input().split()))
        truncated_area = int(((a*b*100)/c)**0.5)
        print(truncated_area)
    except:
        break
