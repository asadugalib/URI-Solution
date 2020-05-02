#1478 Square Matrix II

while True:
    num = int(input())
    if num <= 0:
        break
    array = [[1 for i in range(num)] for j in range(num)]
    for i in range(num):
        up_val = 1
        low_val = i + 1
        for j in range(num):
            if i < j:
                up_val += 1
                array[i][j] = up_val
            elif i > j:
                array[i][j] = low_val
                low_val = low_val - 1
            else:
                up_val = 1
                pass

    for i in range(num):
        text = ""
        for j in range(num):
            text += " %3d"%(array[i][j])
        print(text[1:])
    print("")
