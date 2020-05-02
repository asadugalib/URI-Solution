#1435 Square Matrix I

while True:
    num = int(input())
    if num <= 0:
        break
    array = [[1 for i in range(num)] for j in range(num)]
    value = num//2
    if num % 2 == 1:
        value += 1
    start = 1
    end = num-1
    for i in range(2, value+1):
        for j in range(start, end):
            for k in range(start, end):
                array[j][k] = i
        start += 1
        end -= 1
    for i in range(num):
        text = ""
        for j in range(num):
            text += " %3d"%(array[i][j])
        print(text[1:])
    print("")
