#1149 Summing Consecutive Integers

something = input().split()

x = int(something[0])
y = int(something[-1])

sm = 0

for i in range(y):

    sm += x
    x += 1

print(sm)
