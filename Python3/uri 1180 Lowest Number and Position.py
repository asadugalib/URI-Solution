#1180 Lowest Number and Position

limit = int(input())
array = list(map(int, input().split()[:limit]))
min = min(array)
print("Menor valor: {}\nPosicao: {}".format(min,array.index(min)))
