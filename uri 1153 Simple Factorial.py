#1153 Simple Factorial

num = int(input())

factorial = 1

for i in range(num):
    
    factorial *= num
    num -= 1

print(factorial)
