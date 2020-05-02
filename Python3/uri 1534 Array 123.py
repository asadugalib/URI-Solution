#1534 Array 123

while True:
    try:
        num = int(input())
        array = [["3" for row in range(num)] for column in range(num)]
        col = num-1
        for i in range(num):
            array[i][i] = "1"
            array[i][col] = "2"
            col -= 1
            text = "".join(array[i])
            print(text)
    except EOFError:
        break
