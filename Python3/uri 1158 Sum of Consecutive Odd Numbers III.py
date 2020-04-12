#1158 Sum of Consecutive Odd Numbers III

test = int(input())

count = 0

while count < test:
    
    x, y = list(map(int, input().split()))

    odd_sum = 0
    
    while y > 0:

        if x % 2 != 0:

            odd_sum += x

        else:

            odd_sum += x+1

        y -= 1
        x += 2

    print(odd_sum)

    count += 1
