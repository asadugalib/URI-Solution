#1827 Square Array IV

def first_stage(number):
    arr = [[0 for i in range(number)] for j in range(number)]
    for i in range(number):
        arr[i][i] = 2
        arr[i][number - 1 - i] = 3
    return arr


def one(arr, start, end):
    for row in range(start, end):
        for col in range(start, end):
            arr[row][col] = 1


def output(arr):
    for lis in arr:
        text = ""
        for item in lis:
            text += str(item)
        print(text)
    print("")


while True:
    try:
        num = int(input())
        if 5 <= num <= 101:
            if num % 2 == 1:
                array = first_stage(num)
                st = num//3
                ed = num-st
                one(array, st, ed)
                mid = num//2
                array[mid][mid] = 4
                output(array)
    except:
        break
